def add_student(name, age, email):
  conn = sqlite3.connect('school.db')
  c = conn.cursor()
  c.execute('''
  INSERT INTO students (name, age, email) VALUES(?, ?, ?)
  ''',(name, age, email))
  conn.commit()
  conn.close()
