import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {
    'over18': '1'
}
resp = requests.get(url, cookies=cookies)
print(resp.text)
soup = BeautifulSoup(resp.text, 'html5lib')
arts = soup.find_all('div', class_='r-ent')
for art in arts:
    title = art.find('div', class_='title').getText().strip()
    link = 'https://www.ptt.cc' + art.find('div', class_='title').a['href'].strip()
    author = art.find('div', class_='author').getText().strip()
    print(f'title: {title}\nlink: {link}\nauthor: {author}')
