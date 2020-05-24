import csv, requests
from bs4 import BeautifulSoup

# News source
url = 'https://www.reuters.com/subjects/autos'
resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

soup = BeautifulSoup(resp.text, 'html.parser')

# Reuters news section
# Returns list containing each article
# articles = soup.find('div', {'class': 'column1'}).findAll('article', {'class': 'story'})

# Article titles
titles = soup.find('div', {'class': 'column1'}).findAll(True, {'class': 'story-title'})
title = titles[0].text.strip()

# Article summaries
summaries = soup.find('div', {'class': 'column1'}).findAll('p')
summary = summaries[0].text.strip()

file = open('autonews.csv', 'w')

writer = csv.writer(file)
# Write header rows
writer.writerow(['Source', 'Title', 'Summary'])

writer.writerow([url, title, summary])

file.close()