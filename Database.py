import sqlite3
class Database:
    def __init__(self):
        self.conn=sqlite3.connect('database.db')
        self.cursor=self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS book(
                book_id TEXT PRIMARY KEY,
                book_name TEXT,
                enrollment TEXT,
                how_many INTEGER,
                date_buyed DATE,
                balance INTEGER
                )
            """
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS student (
                enrollment TEXT PRIMARY KEY,
                name TEXT,
                branch TEXT,
                year TEXT
            )
            """
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS issueReturn(
                book_id FORGIEN KEY,
                enrollment FORGIEN KEY,
                book_name TEXT,
                issued DATE,
                returned DATE
            )
            """
        )
    
    def insertToBook(self, **k):
        self.cursor.execute(
            """INSERT INTO book(book_id,book_name,enrollment,how_many,date_buyed, balance)VALUES(?,?,?,?,?,?)""",(k['i'],k['n'],k['e'],k['h'],k['w'],k['h'])
            )
        print("Student saved")

    def insertToStudent(self, **k):
        self.cursor.execute(
            """INSERT INTO student(enrollment,name,branch,year)VALUES(?,?,?,?)""",(k['e'],k['n'],k['b'],k['y'])
            )
        print("Student saved")

    def insertToIssueReturn(self, **k):
        self.cursor.execute(
            """INSERT INTO issueReturn(book_id,enrollment,book_name,issued)VALUES(?,?,?,?)""",(k['i'],k['e'],k['n'],k['iss'])
        )
        print("saved") 
    def returnTo(self,**r):
        self.cursor.execute(
            """INSERT INTO issueReturn(book_id,enrollment,book_name,returned)VALUES(?,?,?,?)""",(r['i'],r['e'],r['n'],r['ret'])
        )
        print("saved") 
    def  enrollmentdetails(self,r):
        self.cursor.execute("""select student.name,issueReturn.book_id, issueReturn.book_name,issueReturn.issued,issueReturn.returned from student inner join issueReturn ON student.enrollment = issuereturn.enrollment""")
        r = self.cursor.fetchall()
        return r
    def search(self,bi,bn):
        self.cursor.execute("""SELECT book_id,book_name FROM issueReturn""")
        r=self.cursor.fetchall()
        return r

        
    def __del__(self):
        self.conn.commit()
        self.conn.close()