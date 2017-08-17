import datetime
import requests
from bs4 import BeautifulSoup
import pylab as pl
import matplotlib.pyplot as plt

lj_hs = open('lj_hs.txt', 'a')
wj_hs = open('wj_hs.txt', 'a')
date = open('date.txt', 'a')

def get_hs():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
    }

    lj_url = 'https://hz.lianjia.com/ershoufang/'
    lj_r = requests.get(url=lj_url, headers=headers)
    lj_html = lj_r.content
    lj = BeautifulSoup(lj_html, 'html.parser')
    lj_num_ct = lj.find('div', attrs={'class': 'resultDes clear'})
    lj_num = lj_num_ct.span.string.strip()
    lj_hs.write(lj_num + ' ')
    lj_hs.close()

    #print(lj_num)

    wawj_url = 'http://hz.5i5j.com/exchange'
    wawj_r = requests.get(url=wawj_url, headers=headers)
    wawj_html = wawj_r.content
    wawj = BeautifulSoup(wawj_html, 'html.parser')
    wawj_num_cnt = wawj.find('font', attrs={'class': 'font-houseNum'})
    wawj_num = wawj_num_cnt.string.strip()
    wj_hs.write(wawj_num + ' ')
    wj_hs.close()

    #print(wawj_num)


def get_time():
    now_time = datetime.datetime.now()
    today_time = now_time.strftime('%m/%d')
    date.write(today_time + ' ')
    date.close()

def fig_plot():
    global date_list
    lj_hs_rd = open('lj_hs.txt', 'r')
    wj_hs_rd = open('wj_hs.txt', 'r')
    date_rd  = open('date.txt', 'r')

    lj_ay = []
    wj_ay = []
    dt_ay = []

    for lj_line in lj_hs_rd.readlines():
        lj_list = lj_line.split(' ')
        for i in range(len(lj_list)-1):
            aa = int(lj_list[i])
            lj_ay.append(aa)

    for wj_line in wj_hs_rd.readlines():
        wj_list = wj_line.split(' ')
        for j in range(len(wj_list)-1):
            bb = int(wj_list[j])
            wj_ay.append(bb)

    for date_line in date_rd.readlines():
        date_list = date_line.split(' ')
        dt_list = date_list.pop()
        for k in range(len(date_list)-1):
            print(date_list[k])
            dt = datetime.datetime.strptime(date_list[k], '%m/%d')
            print(dt, type(dt))


    #dt = datetime.datetime.strptime(dt_list)

    #print(lj_ay)
    #print(wj_ay)
    #print(dt_list, type(dt_list))

    pl.plot_date(pl.date2num(dt_ay),lj_ay, label = 'lj hosue number')
    pl.plot_date(pl.date2num(dt_ay),wj_ay, label = 'wawj house number')
    plt.xlabel('date')
    plt.ylabel('house number')
    plt.grid(True)
    plt.legend(loc = 'upper left')
    plt.show()


if __name__ == '__main__':
    get_hs()
    get_time()
    fig_plot()

#x = [1,2,3,4,5]
#y = [1,4,9,16,25]
#z = [1,1,2,4,8]
#
#plot1 = plt.plot(x,y, label = 'lj hosue number')
#plot2 = plt.plot(x,z, label = 'wawj house number')
#plt.xlabel('date')
#plt.ylabel('house number')
#plt.grid(True)
#plt.legend(loc = 'upper left')

#plt.show()

