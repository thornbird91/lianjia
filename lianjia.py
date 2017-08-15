import requests
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
}

lj_url    = 'https://hz.lianjia.com/ershoufang/'
lj_r      = requests.get(url=lj_url, headers=headers)
lj_html   = lj_r.content
lj        = BeautifulSoup(lj_html, 'html.parser')
lj_num_ct = lj.find('div', attrs = {'class' : 'resultDes clear'})
lj_num    = lj_num_ct.span.string

print(lj_num)

wawj_url     = 'http://hz.5i5j.com/exchange'
wawj_r       = requests.get(url=wawj_url, headers=headers)
wawj_html    = wawj_r.content
wawj         = BeautifulSoup(wawj_html, 'html.parser')
wawj_num_cnt = wawj.find('font', attrs = {'class' : 'font-houseNum'})
wawj_num     = wawj_num_cnt.string

print(wawj_num)

