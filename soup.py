import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.reuters.com/subjects/autos', headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

soup = BeautifulSoup(resp.text, 'html.parser')

summary = soup.select('#content > section:nth-child(4) > div > div.column1.col.col-10 > section:nth-child(2) > section > div > article:nth-child(15) > div.story-content > p')
print(summary[0].text)