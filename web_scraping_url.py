from bs4 import BeautifulSoup
import requests

user_currency = input('>'')


html_text = requests.get('https://www.about.me/kiuzzaxk').text
soup = BeautifulSoup(html_text, 'lxml')
cryptos = soup.find_all('li', class_ = 'crypto')
