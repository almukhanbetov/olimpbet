from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = "https://olimpbet.kz/betting/soccer"

session = HTMLSession()
res = session.get(url)
res.html.render()

soup = BeautifulSoup(res.html.html, 'html.parser')

titles = soup.find_all('a')
for title in titles:
    print(title.text)










