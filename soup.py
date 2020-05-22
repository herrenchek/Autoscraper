import csv, requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.reuters.com/subjects/autos', headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

soup = BeautifulSoup(resp.text, 'html.parser')

p = soup.select('#content > section:nth-child(4) > div > div.column1.col.col-10 > section:nth-child(2) > section > div > article:nth-child(15) > div.story-content > p')
summary = p[0].text.strip()

file = open('autonews.csv', 'w')

writer = csv.writer(file)
# Write header rows
writer.writerow(['Title', 'Summary'])
writer.writerow([summary])

file.close()