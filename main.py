import time
from bs4 import BeautifulSoup
import psycopg2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)
db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Zxcvbnm123",
    dbname="mydatabase",
    port=5432
)
driver.get("https://google.com")
time.sleep(5)