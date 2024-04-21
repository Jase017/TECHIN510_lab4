import requests
from bs4 import BeautifulSoup
import sqlite3

def create_db():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            rating TEXT NOT NULL,
            url TEXT NOT NULL,
            image_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def scrape_and_store(base_url="http://books.toscrape.com"):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    page = 1

    while True:
        url = f"{base_url}/catalogue/page-{page}.html"
        response = requests.get(url)
        if response.status_code != 200:
            break  # Stop if no more pages are available

        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = book.h3.a.get('title')
            price = book.find('p', class_='price_color').text[1:]  # Strip the pound sign
            rating = book.find('p').get('class')[1]  # Rating class e.g., 'Three'
            relative_url = book.h3.a.get('href')
            full_url = f"{base_url}/catalogue/{relative_url}"
            image_relative_url = book.div.img.get('src')
            image_full_url = f"{base_url}/{image_relative_url}"

            c.execute('INSERT INTO books (title, price, rating, url, image_url) VALUES (?, ?, ?, ?, ?)', 
                      (title, float(price), rating, full_url, image_full_url))
        
        page += 1
        conn.commit()

    conn.close()

# Example usage:
create_db()
scrape_and_store()