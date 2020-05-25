import csv, requests
from bs4 import BeautifulSoup

# Reuters news section
url = 'https://www.reuters.com/subjects/autos'
resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

# HTML parsing
soup = BeautifulSoup(resp.text, 'html.parser')

# Returns list containing each Reuters article
articles = soup.find('div', {'class': 'column1'}).findAll('article', {'class': 'story'})

# Article URL
source = url + articles[1].div.a['href']

# Article titles
titles = soup.find('div', {'class': 'column1'}).findAll(True, {'class': 'story-title'})
title = titles[1].text.strip()

# Article summaries
summaries = soup.find('div', {'class': 'column1'}).findAll('p')
summary = summaries[0].text.strip()

file = open('autonews.csv', 'w')

writer = csv.writer(file)
# Write header rows
writer.writerow(['Source', 'Title', 'Summary'])

writer.writerow([source, title, summary])

file.close()