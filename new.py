import sqlite3
import Home 
class Authentication:
    def __init__(self,username='',name='',password='',mobile=''):
        self.conn=sqlite3.connect('data_auther.db')
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(20) PRIMARY KEY,name TEXT,password TEXT,mobile INTEGER)")
        self.username=username
        self.name=name
        self.password=password
        self.mobile=mobile
    def adduser(self): 
        self.cursor.execute('INSERT INTO users(username,name,password,mobile)VALUES(?,?,?,?)',(self.username,self.name,self.password,self.mobile))
    def showall(self):
        self.cursor.execute('SELECT * FROM users')
        r=self.cursor.fetchall()
        return r
    def student(self,enrollment_no="",name="",branch="",year=""):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student(enrollment_no TEXT,name TEXT,branch TEXT,year INTEGER)")
        self.en=enrollment_no
        self.n=name
        self.branch=branch
        self.year=year
        self.stdt()
    def stdt(self):
        self.cursor.execute("INSERT INTO student(enrollment_no,name,branch,year)VALUES(?,?,?,?)",(self.en,self.n,self.branch,self.year))
        print("added successfully")
    def bokks(self,enrollment_no="",id="",bkname="",howmany="",issueddate="",returneddate="",when_buy=""):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books(enrollment_no TEXT,book_id TEXT,book_name TEXT,how_many INTEGER,issued DATE,returned DATE,when_book_buyed DATE)")
        self.en=enrollment_no
        self.bookid=id
        self.book_name=bkname
        self.how_many=howmany
        self.issued=issueddate
        self.returned=returneddate
        self.when_book_buyed=when_buy
        self.issueddd()
    def issueddd(self): 
        self.cursor.execute("INSERT INTO books(enrollment_no,book_id,book_name,how_many,issued)VALUES(?,?,?,?,?)",(self.en,self.bookid,self.book_name,self.how_many,self.issued))
        print('data saved successfully') 
    def returnbk(self):
        self.cursor.execute('INSERT INTO books(enrollment_no,book_id,book_name,returned)VALUES(?,?,?,?)',(self.en,self.bookid,self.book_name,self.returned))
        print("data")
    def addbk(self):
        self.cursor.execute('INSERT INTO books(book_id,book_name,how_many,when_book_buyed)VALUES(?,?,?,?)',(self.bookid,self.book_name,self.how_many,self.when_book_buyed))
        print("books added")
    def edit(self):
        self.cursor.execute('UPDATE INTO books SET new_id=? WHERE enrollment_no=?',(self.new_id,self.id))
        print("ID CHANGED")
    def enrollmentdetails(self):
        pass
        
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()