import requests as req
import bs4 as bs

url = 'https://www.google.co.in/'

res = req.get(url)

soup = bs.BeautifulSoup(res.text,'lxml')

for i in soup.find_all('input',{'name':'btnI'}):
    print(i.get('value'))