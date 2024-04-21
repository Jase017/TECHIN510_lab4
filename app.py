import streamlit as st
import sqlite3

def fetch_books(query, filter_by=None):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    
    query = f"%{query}%"
    # Start with basic SQL query including wildcard search
    sql = 'SELECT * FROM books WHERE title LIKE ? OR rating LIKE ?'
    
    # Conditional logic to modify the SQL based on user input
    if filter_by == 'Price':
        sql += ' ORDER BY price'
    elif filter_by == 'Rating':
        sql += ' ORDER BY rating DESC'
    else:
        # Default to sorting alphabetically by title if no filter is selected
        sql += ' ORDER BY title'
    
    c.execute(sql, (query, query))
    books = c.fetchall()
    conn.close()
    return books

st.title('📕Go find the book you want!📘')
st.subheader('📚Here is a web scraping website that scrapes books from "http://books.toscrape.com"')
st.subheader('You can easily search and filter books on this website!', divider='rainbow')

# Use columns to better organize inputs
col1, col2, col3 = st.columns(3)
with col1:
    search_query = st.text_input('Search by book name or rating:')
with col2:
    # Add default sorting option
    filter_by = st.selectbox('Order by:', ['Default', 'Price', 'Rating'])
with col3:
    if st.button('Search'):
        results = fetch_books(search_query, filter_by if filter_by != 'Default' else None)

# Display results in a more structured way
if 'results' in locals():
    if results:
        for result in results:
            with st.expander(f"{result[1]} - £{result[2]} - Rating: {result[3]}"):
                st.image(result[5], width=100)  # Display book image
                st.write(f"**Title:** {result[1]}")
                st.write(f"**Price:** £{result[2]}")
                st.write(f"**Rating:** {result[3]}")
                st.markdown(f"[More Details]({result[4]})")  # Provide a clickable link to the book details
    else:
        st.write("No books found matching your criteria.")