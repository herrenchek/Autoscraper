import csv, requests
from bs4 import BeautifulSoup

# Reuters news section
url = 'https://www.reuters.com/subjects/autos'
resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

# HTML parsing
soup = BeautifulSoup(resp.text, 'html.parser')

# Returns list containing each Reuters article
divs = soup.find('div', {'class': 'column1'}).find_all('div', {'class': 'story-content'})

# Article titles
# titles = soup.find('div', {'class': 'column1'}).find_all(True, {'class': 'story-title'})
# Article summaries
# summaries = soup.find('div', {'class': 'column1'}).find_all('p')

file = open('autonews.csv', 'w')

writer = csv.writer(file)
# Write header rows
writer.writerow(['Source', 'Title', 'Summary'])

# Iterating through each Reuters div in the list
for div in divs:
    # Article URL
    source = url + div.a['href']
    # Article title
    title = div.a.text.strip()
    # Article summary
    summary = div.p

    writer.writerow([source, title, summary])

# Edmunds RSS feed
ed_r = requests.get('https://www.edmunds.com/feeds/rss/car-news.xml', headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4'})

ed_r.raise_for_status()

ed_soup = BeautifulSoup(ed_r.content, 'html5lib')

# Returns list containing each item in the Edmunds XML feed
items = ed_soup.find_all('item')

# Iterating through each Edmunds item
for item in items:
    source = item.guid.text
    title = item.title.text

    writer.writerow([source, title])

file.close()