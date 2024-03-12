def get_book_by_id(id):
  conn = sqlite3.connect('books.db')
  c = conn.cursor()
  query = '''SELECT * FROM books WHERE id=?'''
  try:
    c.execute(query,(id,))
    book = c.fetchone()
    return book
  except Exception as e:
    print(f'An error occurred: {e}')   
  finally:    
    conn.close()
# Example usage
id = 1
book = get_book_by_id(id)
if book:
    print(book)
else:
    print("No book found with the given ID.")

