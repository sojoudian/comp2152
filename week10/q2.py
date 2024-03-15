def get_students():
  conn = sqlite3.connect('school.db')
  c = conn.cursor()
  c.execute('''SELECT * FROM students''')
  students = c.fetchall()
  conn.close()  
  return students
