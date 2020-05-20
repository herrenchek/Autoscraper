import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.reuters.com/subjects/autos')
soup = BeautifulSoup(resp.text, 'html.parser')

summary = soup.select('#content > section:nth-child(4) > div > div.column1.col.col-10 > section:nth-child(2) > section > div > article:nth-child(15) > div.story-content > p')
print(summary[0].text.strip())