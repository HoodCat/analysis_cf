from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
request = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'

resp = urlopen(request)
html = resp.read().decode('cp949')

# print(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

tags = soup.find_all('div', attrs={'class': 'tit3'})
# print(tags)

for index, tag in enumerate(tags):
    # print(tag.a.text)
    print(index, tag.a.string, tag.a['href'], sep='\t|\t')
