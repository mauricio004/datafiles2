__author__ = 'mflores1'

from bs4 import BeautifulSoup
import requests, os, csv

r = requests.get('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')
soup = BeautifulSoup(r.text, 'html5lib')
letters = soup.find_all('div', class_='ec_statements')

lobbying = {}

for element in letters:
    lobbying[element.a.get_text()] = {}

prefix = 'ww.aflcio.org'

for element in letters:
    lobbying[element.a.get_text()]['link'] = prefix + element.a['href']

for element in letters:
    date = element.find(id='legalert_date').get_text()
    lobbying[element.a.get_text()]['date'] = date

# for k, v in lobbying.iteritems():
#     print k

# Writing to file
# os.chdir('c://Users/mflores1/dropbox/Mauricio')

with open('lobbying.csv', 'w') as toWrite:
    writer = csv.writer(toWrite, delimiter=',')
    writer.writerow(['name', 'link', 'date'])
    for a in lobbying.keys():
        writer.writerow([a.encode('utf8', 'ignore'), lobbying[a]['link'], lobbying[a]['date']])








