def get_books():
  conn = sqlite3.connect('books.db')
  c = conn.cursor()
  try:
    c.execute(''' SELECT * FROM books''')
    allBooks = c.fetchall()
    return allBooks
  except Exception as e:
    print(f'An unexpected error occured: {e}')
  finally:
    conn.close()
