import sqlite3
conn=sqlite3.connect('database.db')
cursor=conn.cursor()
cursor.execute("SELECT * FROM student")
r=cursor.fetchall()
print (r)
cursor.execute("SELECT * FROM issueReturn")
r=cursor.fetchall()
print(r)


cursor.execute("""select student.name,issueReturn.book_id, issueReturn.book_name,issueReturn.issued,issueReturn.returned from student inner join issueReturn ON student.enrollment = issuereturn.enrollment""")
r = cursor.fetchall()
print(r)

conn.close()