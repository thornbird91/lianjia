import datetime
import requests
from bs4 import BeautifulSoup
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib import pylab


def get_hs():
    lj_hs = open('lj_hs.txt', 'a')
    wj_hs = open('wj_hs.txt', 'a')

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
    date = open('date.txt', 'a')
    now_time = datetime.datetime.now()
    today_time = now_time.strftime('%m/%d')
    date.write(today_time + ' ')
    date.close()

def fig_plot():
    lj_hs_rd = open('lj_hs.txt', 'r')
    wj_hs_rd = open('wj_hs.txt', 'r')
    date_rd  = open('date.txt', 'r')

    lj_ay = []
    wj_ay = []
    dt_ay = []

    for lj_line in lj_hs_rd.readlines():
        lj_list = lj_line.strip().split(' ')
        for i in range(len(lj_list)):
            aa = int(lj_list[i])
            lj_ay.append(aa)

    for wj_line in wj_hs_rd.readlines():
        wj_list = wj_line.strip().split(' ')
        for j in range(len(wj_list)):
            bb = int(wj_list[j])
            wj_ay.append(bb)

    for date_line in date_rd.readlines():
        date_list = date_line.strip().split(' ')
        for k in range(len(date_list)):
            dt = datetime.datetime.strptime(date_list[k], '%m/%d')
            dt_ay.append(dt)
    dt_fl = pl.date2num(dt_ay)


    plt.figure(1)
    pl.gca().xaxis.set_major_formatter(mdate.DateFormatter('%m/%d'))
    pl.gca().xaxis.set_major_locator(mdate.DayLocator())
    pl.plot_date(dt_fl,lj_ay, label = 'lj hosue number', linestyle='-')
    pl.plot_date(dt_fl,wj_ay, label = 'wawj house number', linestyle='-')
    plt.xlabel('date')
    plt.ylabel('house number')
    plt.grid(True)
    plt.legend(loc = 'upper left')
    #plt.show()
    plt.savefig('line_plot.png')

    plt.figure(2)
    total_width, n=0.8,2
    width = total_width/n
    plt.bar(dt_fl, lj_ay, width=width, label = 'lj')
    plt.bar(dt_fl+width, wj_ay,width=width, label = 'wj')
    plt.legend()
    #plt.show()
    plt.savefig('bar_plot.png')



if __name__ == '__main__':
    #get_hs()
    #get_time()
    fig_plot()


