from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = "https://olimpbet.kz/betting/soccer"
session = HTMLSession()
res = session.get(url)
res.html.render()

soup = BeautifulSoup(res.html.html, 'html.parser')
matches = []
for row in soup.find_all('tr'):
    link = row.find('a')
    checkbox = row.find('input', {'class', 'selchamp'})
    if link and checkbox:
        match_data = {
            'title':link.text.strip(),
            'url': link['href'],
            'check_box': checkbox['value']
        }
        matches.append(match_data)

for match in matches:
    print(f"Title: {match['title']}, URL: {match['url']}, Checkbox Value: ")


