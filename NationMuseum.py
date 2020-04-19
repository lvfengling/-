from bs4 import BeautifulSoup
import requests

URL = "http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/index.html"
headers = {
     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
 }
html = requests.get(URL,headers=headers).text
#print(html)
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul')

url1="http://www.chnmus.net"
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = url1+img['src']
        print(url)
        r = requests.get(url, stream=True,headers=headers)
        image_name = url.split('/')[-1]
        with open('F:/img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
 

