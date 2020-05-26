import csv, requests
from bs4 import BeautifulSoup

# Reuters news section
url = 'https://www.reuters.com/subjects/autos'
resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})

resp.raise_for_status()

# HTML parsing
soup = BeautifulSoup(resp.text, 'html.parser')

# Returns list containing each Reuters article
divs = soup.find('div', {'class': 'column1'}).findAll('div', {'class': 'story-content'})
# Article titles
# titles = soup.find('div', {'class': 'column1'}).findAll(True, {'class': 'story-title'})
# Article summaries
# summaries = soup.find('div', {'class': 'column1'}).findAll('p')

file = open('autonews.csv', 'w')

writer = csv.writer(file)
# Write header rows
writer.writerow(['Source', 'Title', 'Summary'])

# Iterating through each article in the list
for div in divs:
    # Article URL
    source = url + div.a['href']
    # Article title
    title = div.a.text.strip()
    # Article summary
    summary = div.text.strip()

    writer.writerow([source, title, summary])

file.close()