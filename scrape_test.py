from os import write
from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
quotes = soup.find_all('span', attrs={'class': 'text'})
authors = soup.find_all('small', attrs={'class': 'author'})

file = open("scraped_quotes.csv", mode='w')
writer = csv.writer(file)

writer.writerow(['Quote', 'Author'])

for quote, author in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)
    print('---')
    writer.writerow([quote.text, author.text])
file.close()