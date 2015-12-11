__author__ = 'mflores1'

from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')
soup = BeautifulSoup(r.text, 'html5lib')
letters = soup.find_all('div', class_='ec_statements')
lobbying = {}

for element in letters:
    lobbying[element.a.get_text()] = {}

prefix = 'ww.aflcio.org'

for element in letters:
    lobbying[element.a.get_text()]['link'] = prefix + element.a['href']
print lobbying



x = 5


