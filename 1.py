import logging
from distutils.command.install import value
from requests import session
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import psycopg2
db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Zxcvbnm123",
    dbname="mydatabase",
    port=5432
)
cursor = db.cursor()
url = "https://olimpbet.kz/betting/soccer"
session = HTMLSession()
res = session.get(url)
res.html.render()
soup = BeautifulSoup(res.html.html, 'html.parser')
table = soup.find('table', class_='live_main_table')
if table:
    rows = table.find_all('tr')
    for row in rows:
        link = row.find('a')
        if link:
            text = link.text.strip()
            href = link.get('href')
            query = "INSERT INTO events(event_name, event_link) VALUES(%s, %s)"
            values = (text, href)
            cursor.execute(query,values)
            print(f"Событие: {text}, Ссылка: {href}")
    db.commit()
else:
    print("Таблица не найдена")

cursor.close()
db.close()
