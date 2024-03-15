def get_book_by_id(id):
  conn = sqlite3.connect('books.db')
  c = conn.cursor()
  try:
    c.execute('''SELECT * FROM books WHERE id=?''',(id,))
    book = c.fetchone()
    return book
  except Exception as e:
    print(f'An error occurred: {e}')
  finally:
    conn.close()  
