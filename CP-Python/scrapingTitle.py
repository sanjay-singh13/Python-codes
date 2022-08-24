import requests as req
import bs4 as bs

url = 'https://tweetdeck.twitter.com/'

res = req.get(url)

soup = bs.BeautifulSoup(res.text,'lxml')

title = soup.select('title')

print(title[0].getText())
    
