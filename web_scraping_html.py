"""
pip install beautifulsoup4
pip install lxml
"""

from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
  content = html_file.read()  # read whole html
  
  soup = BeautifulSoup(content, 'lxml')  # read the html content with lxml parser
  # print(soup.prettify())  # read in a pretty way
  
  # tags = soup.find('h5')  # reads first h5 tag in html
  # crypto_tags = soup.find_all('h5')  # reads all h5 tags in html
  # for crypto in crypto_tags:  # read each tag from the tags list
  #   print(crypto.text)
  
  crypto_cards = soup.find_all('div', class_='card')  # find all div of class card
  for crypto in crypto_cards:
    # print(crypto.h5)  # each h5 under the div of class card
    # print(crypto.h5.text)  # read as text
    crypto_name = crypto.h5.text
    crypto_price = crypto.a.text
    crypto_price = crypto.a.text.split()[-1]
