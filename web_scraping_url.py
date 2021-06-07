from bs4 import BeautifulSoup
import requests

user_currency = input('>'')

def crypto_value():
	html_text = requests.get('https://www.about.me/kiuzzaxk').text
	soup = BeautifulSoup(html_text, 'lxml')
