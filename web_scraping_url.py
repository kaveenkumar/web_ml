from bs4 import BeautifulSoup
import requests

user_currency = input('>'')

def crypto_value():
	html_text = requests.get('https://www.about.me/kiuzzaxk').text
 	soup = BeautifulSoup(html_text, 'lxml')
  	cryptos = soup.find_all('li', class_ = 'crypto')

  	for idx, crypto in enumerate(cryptos):
    		date = crypto.find('span', class_ = 'date_posted').span.text

if __name__ == '__main__':
  	while True:
		crypto_value()
		time_wait = 10
		print(f'waiting time {time_wait} minutes')
		time.sleep(time_wait * 60)
