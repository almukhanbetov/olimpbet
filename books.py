from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = "https://react-amazon-bestsellers-books-dy.netlify.app/"

session = HTMLSession()
res = session.get(url)
res.html.render()

print(res.html)
# print(res.html.find('article.book'))
soup = BeautifulSoup(res.html.html, 'html.parser')

books = soup.find_all('article', class_='book')
for book in books:
    print(book.find('h2').text)
