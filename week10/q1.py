def add_book(title, author_id, isbn, publication_year):
  conn = sqlite3.connect('books.db')
  c = conn.cursor()

  insertSQL = '''INSERT INTO books (title, author_id, isbn, publication_year) VALUES(?, ?, ?, ?)'''

  try:
    c.execute(insertSQL, (title, author_id, isbn, publication_year))
    conn.commit()
    print('Book added successfully.')
  except sqlite3.IntegrityError as e:
    print(f'Error adding the book: {e}')
  except Exception as e:
    print(f'An unexpected error occured: {e}')
  finally:
      conn.close()

