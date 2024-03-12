def get_books():
  conn = sqlite3.connect('books.db')
  c = conn.cursor()
  query = '''SELECT * FROM books'''
  try:
    c.execute(query)
    all_books = c.fetchall()
    return all_books
  except Exception as e:
    print(f'An unexpected error occured: {e}')
  finally:
    conn.close()
# Example usage
books = get_books()
for book in books:
   print(book)
#  conn = sqlite3.connect('school.db')
#  c = conn.cursor()
# 
#  c.execute(''' ''')
#  
#  conn.close()
