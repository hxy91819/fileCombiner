# 磁力链抓取
# 抓取一个页面中所有的磁力链接
# 只能针对不同的页面来抓取

# 使用requests发起http请求，使用BeautifulSoup解析页面

import requests
from bs4 import BeautifulSoup

url = 'https://www.dygod.net/html/tv/hytv/20200623/113340.html'
# url = 'http://www.baidu.com'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.135 Safari/537.36',
           # 'Referer': 'http://www.btbtdy2.com/btdy/dy26958.html',
           # 'Host': 'www.btbtdy2.com',
           # 'X-Request-With': 'XMLHttpRequest',
           # 'Cookie': 'Hm_lvt_99249fb41a838398a3cc1c3ad2258fe7=1598793718; '
           #           'Hm_lpvt_99249fb41a838398a3cc1c3ad2258fe7=1598884657; PHPSESSID=2rghe3g77hbo6nmrn4a690ld31; '
           #           'Hm_lvt_99249fb41a838398a3cc1c3ad2258fe7=1598793718; bdshare_firstime=1598884861699; '
           #           'Hm_lpvt_99249fb41a838398a3cc1c3ad2258fe7=1598970208 ',
           # 'Accept': '*/*'
           }

response = requests.get(url, headers)
# print(response)
# print(response.text)

response.encoding = 'gbk'
text = response.text

soup = BeautifulSoup(text, 'lxml')
for link in soup.find_all('a'):
    href = link.get('href')
    if not href.startswith('magnet'):
        continue
    print(href)
