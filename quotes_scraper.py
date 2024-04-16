import os
import requests

from bs4 import BeautifulSoup

URL = 'https://quotes.toscrape.com/page/{page}/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
quote_divs = soup.select('div,quote')

page = 1
while True:
    url = URL.format(page=page)
    response = requests.get(URL)
    if'No quotes found' in response.text:
        break
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    for quote_div in quote_divs:
        quote = {}
        quote['content'] = quote_div.select('span.text').text
        quote['author'] = quote_div.select('small.author').text
        quote['author_link'] = quote_div.select('span')[1].select('a')[0]
        quote['tags'] =[tag.text for tag in quote_div.select('a.tag')]
        quote['tag_links'] =[tag['herf'] for tag in quote_div.select('a.tag')]
        quotes.append(quote)
        page += 1