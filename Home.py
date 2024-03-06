import sys
import new
import Database as dbs
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,QHeaderView,
    QTableWidget,
    QFrame, QLabel,QMessageBox,
    QTableWidgetItem,
)
import new as db
from PyQt5 import  QtGui, QtCore
from PyQt5.QtGui import QFont

class Window(QWidget):
    expression = ''
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('Home-Login')
        self.setStyleSheet("background-color: black")
        self.mainFrame()
        self.showMaximized()

    
    def mainFrame(self):
        self.win = QFrame(self)
        self.win.setStyleSheet(
            "background-color: gray;" "border-radius: 8px;"
        )
        layout = QGridLayout(self.win)

        title = QLabel("Login")
        title.setStyleSheet("height: 60px;" "font-size: 60px;" "text-align: center;")
        layout.addWidget(title, 0,0,1,2)

        ulabel = QLabel("Username")
        layout.addWidget(ulabel, 1,0)

        ufield = QLineEdit()
        ufield.setPlaceholderText('Username')
        ufield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(ufield, 1,1)

        plabel = QLabel("Password")
        layout.addWidget(plabel, 2,0)

        pfield = QLineEdit()
        pfield.setPlaceholderText('Password')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(pfield, 2,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(lambda : self.validatetodb(ufield.text(),pfield.text()))
        layout.addWidget(sbtn, 3,1)
        
        sbtn = QPushButton("Sign up here")
        sbtn.setStyleSheet("background-color: None;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(self.show_signup_window)
        layout.addWidget(sbtn, 4,1)

    def studentdb(self,e,n,b,y):
        obj = dbs.Database()
        obj.insertToStudent(e=e, n=n,b=b,y=y)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle("Success")
        mb.setText("Data saved successfully")
        mb.setStandardButtons(QMessageBox.Ok)
        retval = mb.exec_()

    def  showdetails(self,en1):
        obj=dbs.Database()
        data=obj.enrollmentdetails(en1=en1)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle("Success")
        mb.setText("Data saved successfully")
        mb.setStandardButtons(QMessageBox.Ok)
        retval = mb.exec_()


    def validatetodb(self, u, p):
            obj = db.Authentication()
            data = obj.showall()
            for user in data:
                if user[0] == u:
                    if user[2] == p:
                        self.window()
                        break
                    else:
                        mb = QMessageBox()
                        mb.setIcon(QMessageBox.Critical)
                        mb.setWindowTitle("Invalid")
                        mb.setText("Invalid Password")
                        mb.setStandardButtons(QMessageBox.Ok)
                        retval = mb.exec_()
            else:
                mb = QMessageBox()
                mb.setIcon(QMessageBox.Critical)
                mb.setWindowTitle("Invalid")
                mb.setText("Invalid Username")
                mb.setStandardButtons(QMessageBox.Ok)
                retval = mb.exec_()    

    def createtable(self):
        self.table=QTableWidget()
        self.table.setRowCount()
        self.table.setColumnCount()


    def issuebook(self,i,e,n,iss):
        obj=dbs.Database()
        data=obj.insertToIssueReturn(i=i,n=n,e=e,iss=iss)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle("SAVED")  
        mb.setText("ISSUED SUCCESSFULLY")
        mb.setStandardButtons(QMessageBox.Ok)
        retval=mb.exec_() 
    def returnnbook(self,e,i,n,ret):
        obj=dbs.Database()
        data=obj.returnTo(i=i,n=n,e=e,ret=ret)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle("SAVED")  
        mb.setText("RETURNED SUCCESSFULLY")
        mb.setStandardButtons(QMessageBox.Ok)
        retval=mb.exec_()  

    def addboook(self,i,n,en,howmany,whenbuy):
        obj=dbs.Database()
        data=obj.insertToBook(i=i,n=n,e=en,h=howmany,w=whenbuy)
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle("SAVED")  
        mb.setText("ADDED SUCCESSFULLY")
        mb.setStandardButtons(QMessageBox.Ok)
        retval=mb.exec_()   
    def resizeEvent(self, event):
        self.win.setGeometry(int(self.frameGeometry().width()//4.2), self.frameGeometry().width()//8,self.frameGeometry().width()//2, self.frameGeometry().height()//2)

    def window(self):
        self.setWindowTitle("QHBoxLayout Example")
        # Create a QHBoxLayout instance
        self.layout = QHBoxLayout()
        
        f2=QFrame()
        self.layout.addWidget(f2, 0)
        f2.setStyleSheet('background-color:black;')

        self.addframe=QFrame()
        self.iss=QFrame()
        self.ret=QFrame()
        self.books=QFrame()
        self.edits=QFrame()
        self.dltbk=QFrame()
        self.searchbk=QFrame()
        self.sks=QFrame()
        self.windoww=QFrame()
        self.adds()
        # Set the layout on the application's window

        buttonBox= QGridLayout(f2)

        btn=QPushButton("ADD STUDENT")
        buttonBox.addWidget(btn,1,1) 
        btn.setStyleSheet('background-color:solid white;''color:ack;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn.clicked.connect(self.adds)

        f2.setLayout(buttonBox)
        
        btn2=QPushButton("ISSUED BOOKS")
        buttonBox.addWidget(btn2,2,1)
        btn2.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn2.clicked.connect(self.issu)
        btn3=QPushButton("RETURNED BOOKS")
        buttonBox.addWidget(btn3,3,1)
        btn3.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn3.clicked.connect(self.returnBook)
        btn4=QPushButton("ADD BOOKS")
        buttonBox.addWidget(btn4,4,1)
        btn4.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn4.clicked.connect(self.addbook)
        btn5=QPushButton("EDIT BOOKS")
        buttonBox.addWidget(btn5,5,1)
        btn5.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn5.clicked.connect(self.editbook)
        btn6=QPushButton("DELETE BOOKS")
        buttonBox.addWidget(btn6,6,1)
        btn6.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn6.clicked.connect(self.dltbook)
        btn7=QPushButton("SEARCH BOOKS")
        buttonBox.addWidget(btn7,7,1)
        btn7.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn7.clicked.connect(self.searchboook)
        btn8=QPushButton("SHOW STUDENT DETAILS")
        buttonBox.addWidget(btn8,8,1) 
        btn8.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn8.clicked.connect(self.showbook)
        btn9=QPushButton("EXIT")
        buttonBox.addWidget(btn9,9,1)
        btn9.setStyleSheet('background-color:solid white;''color:black;''font-size:20px;''margin-left:40px;''margin-right:40px;''padding:10px;')
        btn9.clicked.connect(exit)
        self.setLayout(self.layout)
        print(self.children())
    def adds(self):
        self.clrLayout()
        self.addframe=QFrame()
        self.layout.addWidget(self.addframe, 2)
        self.addframe.setStyleSheet('background-color:grey;')
        addGrid = QGridLayout()

        ulabel = QLabel("ADD STUDENT INFORMATION")
        addGrid.addWidget(ulabel, 1,0)
        ulabel.setStyleSheet('font-size:45px;')



        en = QLabel("ENROLLMENT NUMBER")
        addGrid.addWidget(en, 2,0)
        en.setStyleSheet('font-size:20px;')


        en2 = QLineEdit()
        en2.setPlaceholderText('ENROLLMENT NUMBER')
        en2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addGrid.addWidget(en2, 2,1)

        n = QLabel("STUDENT NAME")
        addGrid.addWidget(n, 3,0)
        n.setStyleSheet('font-size:20px;')


        n2 = QLineEdit()
        n2.setPlaceholderText('STUDENT NAME')
        n2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addGrid.addWidget(n2, 3,1)

        branch = QLabel("BRANCH")
        addGrid.addWidget(branch, 4,0)
        branch.setStyleSheet('font-size:20px;')
        
        branch2 = QLineEdit()
        branch2.setPlaceholderText('BRANCH')
        branch2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addGrid.addWidget(branch2, 4,1)

        year = QLabel("YEAR")
        addGrid.addWidget(year, 5,0)
        year.setStyleSheet('font-size:20px;')


        year2 = QLineEdit()
        year2.setPlaceholderText('YEAR')
        year2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addGrid.addWidget(year2, 5,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addGrid.addWidget(sbtn, 6,1)
        sbtn.clicked.connect(lambda:self.studentdb(en2.text(),n2.text(),branch2.text(),year2.text()))

        self.addframe.setLayout(addGrid)
    def issu(self):
        
        self.clrLayout()
        self.iss=QFrame()
        self.layout.addWidget(self.iss,2)
        self.iss.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()

        
        plabel = QLabel("ISSUED DETAILS")
        addfr.addWidget(plabel, 1,0)
        plabel.setStyleSheet('font-size:25px;')

        bkid = QLabel("BOOK ID")
        addfr.addWidget(bkid, 2,0)
        bkid.setStyleSheet('font-size:20px;')
        
        bkid2 = QLineEdit()
        bkid2.setPlaceholderText('BOOK ID')
        bkid2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(bkid2, 2,1)

        bkname = QLabel("BOOK NAME")
        addfr.addWidget(bkname, 3,0)
        bkname.setStyleSheet('font-size:20px;')


        bkname2 = QLineEdit()
        bkname2.setPlaceholderText('BOOK NAME')
        bkname2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(bkname2, 3,1)

        issued1 = QLabel("ISSUED DATE")
        addfr.addWidget(issued1, 4,0)
        issued1.setStyleSheet('font-size:20px;')


        issued2 = QLineEdit()
        issued2.setPlaceholderText('ISSUED DATE')
        issued2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(issued2, 4,1)

        en = QLabel("ENTER ENROLLMENT NO")
        addfr.addWidget(en, 5,0)
        en.setStyleSheet('font-size:20px;')

        nen = QLineEdit()
        nen.setPlaceholderText('ENROLLMENT NO')
        nen.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(nen, 5,1)


        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addfr.addWidget(sbtn, 6,1)
        sbtn.clicked.connect(lambda:self.issuebook(bkid2.text(),nen.text(),bkname2.text(),issued2.text()))
        self.iss.setLayout(addfr)

    def returnBook(self):
        
        self.clrLayout()
        self.ret=QFrame()
        self.layout.addWidget(self.ret,2)
        self.ret.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()

        plabel = QLabel("RETURNED DETAILS")
        addfr.addWidget(plabel, 1,0)
        plabel.setStyleSheet('font-size:25px;')

        bookid1 = QLabel("BOOK ID")
        addfr.addWidget(bookid1, 2,0)
        bookid1.setStyleSheet('font-size:20px;')
        
        bookid2 = QLineEdit()
        bookid2.setPlaceholderText('BOOK ID')
        bookid2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(bookid2, 2,1)

        bookname1 = QLabel("BOOK NAME")
        addfr.addWidget(bookname1, 3,0)
        bookname1.setStyleSheet('font-size:20px;')


        bookname2 = QLineEdit()
        bookname2.setPlaceholderText('BOOK NAME')
        bookname2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(bookname2, 3,1)

        
        en2 = QLabel("ENROLLMENT NUMBER")
        addfr.addWidget(en2, 4,0)
        en2.setStyleSheet('font-size:20px;')


        en3 = QLineEdit()
        en3.setPlaceholderText('ENROLLMENT NUMBER')
        en3.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(en3, 4,1)

        returneddd1 = QLabel("RETURNED DATE")
        addfr.addWidget(returneddd1, 5,0)
        returneddd1.setStyleSheet('font-size:20px;')


        returneddd = QLineEdit()
        returneddd.setPlaceholderText('RETURNED DATE')
        returneddd.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(returneddd, 5,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addfr.addWidget(sbtn, 6,1)
        sbtn.clicked.connect(lambda:self.returnnbook(bookid2.text(),bookname2.text(),en3.text(),returneddd.text()))

        
        self.ret.setLayout(addfr)
    def addbook(self):
        self.clrLayout()
        self.books=QFrame()
        self.layout.addWidget(self.books,2)
        self.books.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()

        plabel = QLabel("ADD NEW BOOKS")
        addfr.addWidget(plabel, 1,0)
        plabel.setStyleSheet('font-size:25px;')

        newbk = QLabel("ENTER NEW BOOK ID")
        addfr.addWidget(newbk, 2,0)
        newbk.setStyleSheet('font-size:20px;')

        newbk2 = QLineEdit()
        newbk2.setPlaceholderText('BOOK ID')
        newbk2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(newbk2, 2,1)

        newbkname = QLabel("ENTER BOOK NAME")
        addfr.addWidget(newbkname, 3,0)
        newbkname.setStyleSheet('font-size:20px;')
        newbkname2 = QLineEdit()
        newbkname2.setPlaceholderText('BOOK NAME')
        newbkname2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(newbkname2, 3,1)


        howmanyy = QLabel("HOW MANY BOOKS YOU BUYED")
        addfr.addWidget(howmanyy, 4,0)
        howmanyy.setStyleSheet('font-size:20px;')

        howmanyy1 = QLineEdit()
        howmanyy1.setPlaceholderText('COUNT NUMBER OF BOOKS')
        howmanyy1.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(howmanyy1, 4,1)
        

        
        whenbuyy = QLabel("WHEN BOOK BUYED")
        addfr.addWidget(whenbuyy, 5,0)
        whenbuyy.setStyleSheet('font-size:20px;')

        whenbuyy1 = QLineEdit()
        whenbuyy1.setPlaceholderText('BUY DATE')
        whenbuyy1.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(whenbuyy1, 5,1)

       
        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addfr.addWidget(sbtn, 6,1)
        sbtn.clicked.connect(lambda:self.addboook(newbk2.text(),newbkname2.text(),howmanyy1.text(),whenbuyy1.text()))
      
        self.books.setLayout(addfr)
    
    def editbook(self):
        self.clrLayout()
        self.edits=QFrame()
        self.layout.addWidget(self.edits,2)
        self.edits.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()

        plabel = QLabel("EDIT BOOKS")
        addfr.addWidget(plabel, 1,0)
        plabel.setStyleSheet('font-size:25px;')

        plabel = QLabel("ENTER OLD BOOK ID")
        addfr.addWidget(plabel, 2,0)
        plabel.setStyleSheet('font-size:20px;')

        pfield = QLineEdit()
        pfield.setPlaceholderText('OLD BOOK ID')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(pfield, 2,1)

        plabel = QLabel("CHANGE BOOK ID")
        addfr.addWidget(plabel, 3,0)
        plabel.setStyleSheet('font-size:20px;')

        pfield = QLineEdit()
        pfield.setPlaceholderText('NEW BOOK ID')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(pfield, 3,1)
       
        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addfr.addWidget(sbtn, 4,1)


        self.edits.setLayout(addfr)
    def dltbook(self):
        self.clrLayout()
        self.dltbk=QFrame()
        self.layout.addWidget(self.dltbk,2)
        self.dltbk.setStyleSheet('background-color:grey;') 
        addfr=QGridLayout()

        
        plabel = QLabel("DELETE BOOK DETAILS FROM LIBRARY")
        addfr.addWidget(plabel, 1,0)
        plabel.setStyleSheet('font-size:35px;')

        plabel = QLabel("ENTER BOOK ID")
        addfr.addWidget(plabel, 2,0)
        plabel.setStyleSheet('font-size:20px;')

        pfield = QLineEdit()
        pfield.setPlaceholderText('BOOK ID')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(pfield, 2,1)
       
        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        addfr.addWidget(sbtn, 3,1)



        self.dltbk.setLayout(addfr)
    def searchbook(self):
        self.clrLayout()
        self.searchbk=QFrame()
        self.layout.addWidget(self.searchbk,2)
        self.searchbk.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()
       

        self.searchbk.setLayout(addfr)    
    def showbook(self):
        self.clrLayout()
        self.sks=QFrame()
        self.layout.addWidget(self.sks,2)
        self.sks.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()

        enroll = QLabel("ENROLLMENT NUMBER")
        addfr.addWidget(enroll, 1,0)

        enroll1 = QLineEdit()
        enroll1.setPlaceholderText('ENROLLMENT')
        enroll1.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(enroll1, 1,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(lambda : self.showStudents(enroll1.text()))
        addfr.addWidget(sbtn, 2,1)

        self.sks.setLayout(addfr)

    def showStudents(self, r):
        obj=dbs.Database() 
        data=obj.enrollmentdetails(r=r)
        # print(data)
        self.next_window(r,data)
    
    def next_window(self, d,i):
        self.sks = TableWin(d,i)
        self.sks.show()
           
    def clrLayout(self):
        self.addframe.hide()
        self.iss.hide()
        self.ret.hide()
        self.books.hide()
        self.edits.hide()
        self.dltbk.hide()
        self.searchbk.hide()
        self.sks.hide()
        self.windoww.hide() 
       

    def secondwindow(self):    
        self.w = QFrame(self)
        self.w.setStyleSheet(
            "background-color: gray;" "border-radius: 8px;""text-align: center;"
        )
        layout = QGridLayout(self.w)

        title = QLabel("SIGN UP")
        title.setStyleSheet("height: 50px;" "font-size: 55px;" "text-align: center;")
        layout.addWidget(title, 0,0,1,2)

        ulabel = QLabel("USERNAME")
        layout.addWidget(ulabel, 1,0)

        ufield = QLineEdit()
        ufield.setPlaceholderText('USERNAME')
        ufield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(ufield, 1,1)

        plabel = QLabel("NAME")
        layout.addWidget(plabel, 2,0)

        pfield = QLineEdit()
        pfield.setPlaceholderText('NAME')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(pfield, 2,1)
        
        plabel = QLabel("PASSWORD")
        layout.addWidget(plabel, 3,0)

        pfield = QLineEdit()
        pfield.setPlaceholderText('PASSWORD')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(pfield, 3,1)

        plabel = QLabel("RE-ENTER YOUR PASSWORD")
        layout.addWidget(plabel, 4,0)

        pfield = QLineEdit()
        pfield.setPlaceholderText('PASSWORD')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(pfield, 4,1)
        
        plabel = QLabel("MOBILE NUMBER")
        layout.addWidget(plabel, 5,0)

        pfield = QLineEdit()
        pfield.setPlaceholderText('MOBILE NUMBER')
        pfield.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(pfield, 5,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(self.window)
        layout.addWidget(sbtn, 6,1)

    def resizeEvent(self, event):
        self.win.setGeometry(int(self.frameGeometry().width()//4.2), self.frameGeometry().width()//8,self.frameGeometry().width()//2, self.frameGeometry().height()//2)

    def show_signup_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()
    def searchboook(self):
        self.clrLayout()
        self.windoww=QFrame()
        self.layout.addWidget(self.windoww,2)
        self.windoww.setStyleSheet('background-color:grey;')
        addfr=QGridLayout()
       
        la= QLabel("SEARCH BOOK")
        addfr.addWidget(la, 1,0)
        la.setStyleSheet("font-size:35px")

        e = QLabel("BOOK ID")
        addfr.addWidget(e, 2,0)

        e2 = QLineEdit()
        e2.setPlaceholderText('BOOK ID')
        e2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(e2, 2,1)

        B = QLabel("BOOK NAME")
        addfr.addWidget(B, 3,0)
        
        eB = QLineEdit()
        eB.setPlaceholderText('BOOK NAME')
        eB.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        addfr.addWidget(eB, 3,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(lambda:self.search(e2.text(),eB.text()))
        addfr.addWidget(sbtn, 4,1)

        self.windoww.setLayout(addfr)
    def search(self,bi,bn):
        obj=dbs.Database()
        data=obj.search(bi=bi,bn=bn)
        self.sks = TableWin1(bi,data)
        self.sks.show()
        
        

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setStyleSheet('background-color:black;')   
        self.w = QFrame(self)
        self.showMaximized()
        self.w.setStyleSheet(
            "background-color: gray;" "border-radius: 8px;""text-align: center;"
        )
        layout = QGridLayout(self.w)

        title = QLabel("SIGN UP")
        title.setStyleSheet("height: 50px;" "font-size: 55px;" "text-align: center;")
        layout.addWidget(title, 0,0,1,2)

        user = QLabel("USERNAME")
        layout.addWidget(user, 1,0)

        user2 = QLineEdit()
        user2.setPlaceholderText('USERNAME')
        user2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(user2, 1,1)

        name= QLabel("NAME")
        layout.addWidget(name, 2,0)

        name2 = QLineEdit()
        name2.setPlaceholderText('NAME')
        name2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(name2, 2,1)
        
        password = QLabel("PASSWORD")
        layout.addWidget(password, 3,0)

        password2 = QLineEdit()
        password2.setPlaceholderText('PASSWORD')
        password2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(password2, 3,1)

        passwordre = QLabel("RE-ENTER YOUR PASSWORD")
        layout.addWidget(passwordre, 4,0)

        passwordre2 = QLineEdit()
        passwordre2.setPlaceholderText('PASSWORD')
        passwordre2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(passwordre2, 4,1)
        
        mobile = QLabel("MOBILE NUMBER")
        layout.addWidget(mobile, 5,0)

        mobile2 = QLineEdit()
        mobile2.setPlaceholderText('MOBILE NUMBER')
        mobile2.setStyleSheet("background-color: white;" "border: 1px solid green; height: 50px;")
        layout.addWidget(mobile2, 5,1)

        sbtn = QPushButton("Submit")
        sbtn.setStyleSheet("background-color: blue;" "color: white;" "font-size: 18px;" "height: 50px;")
        sbtn.clicked.connect(lambda: self.savetodb(user2.text(),name2.text(),password2.text(),passwordre2.text(),mobile2.text()))
        layout.addWidget(sbtn, 6,1)

    def savetodb(self,u,n,p,r,m):
        
        if(p==r):
            obj = db.Authentication(u,n,p,m)
            obj.adduser()
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle("Success")
            mb.setText("Data saved successfully")
            mb.setStandardButtons(QMessageBox.Ok)
            retval = mb.exec_()

        # self.exitthis
        # pass
    
         


    def resizeEvent(self, event):
        self.w.setGeometry(int(self.frameGeometry().width()//4.2), self.frameGeometry().width()//8,self.frameGeometry().width()//2, self.frameGeometry().height()//2)
    def exitthis(self):
        self.close()



class TableWin(QWidget):
    def __init__(self,i, d):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setStyleSheet('background-color:white;')   
        self.w = QFrame(self)
        self.showMaximized()
        # print(d)
        i=int(i)
        filteredList=[]
        for data in d:
            if i in data:
                filteredList.append(data)
        
        print(filteredList)
        self.table=QTableWidget()
        self.table.setRowCount(len(filteredList)+1)
        self.table.setColumnCount(5)
        self.table.setItem(0,0,QTableWidgetItem("NAME"))
        self.table.setItem(0,1,QTableWidgetItem("BOOK ID"))
        self.table.setItem(0,2,QTableWidgetItem("BOOK NAME"))
        self.table.setItem(0,3,QTableWidgetItem("ISSUE DATE"))
        self.table.setItem(0,4,QTableWidgetItem("RETURN DATE"))
        print('d is',d)
        row=1
        for data in filteredList:
            self.table.setItem(row,0,QTableWidgetItem(str(data[0])))
            self.table.setItem(row,1,QTableWidgetItem(str(data[1])))
            self.table.setItem(row,2,QTableWidgetItem(data[2]))
            self.table.setItem(row,3,QTableWidgetItem(data[3]))
            self.table.setItem(row,4,QTableWidgetItem(str(data[4])))
            row+=1


       
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        self.setLayout(layout)

class TableWin1(QWidget):
    def __init__(self,i, d):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setStyleSheet('background-color:white;')   
        self.w = QFrame(self)
        self.showMaximized()
        # print(d)
        # self.table.setItem(0,2,QTableWidgetItem("BOOK NAME"))
        # self.table.setItem(0,3,QTableWidgetItem("ISSUE DATE"))
        # self.table.setItem(0,4,QTableWidgetItem("RETURN DATE"))
        # print('d is', d)
        # print('i is', i)
        i=int(i)
        filteredList=[]
        for data in d:
            if i in data:
                filteredList.append(data)
        
        print(filteredList)

        self.table=QTableWidget()
        self.table.setRowCount(len(filteredList)+1)
        self.table.setColumnCount(2)
        self.table.setItem(0,0,QTableWidgetItem("BOOK ID"))
        self.table.setItem(0,1,QTableWidgetItem("Book NAME"))
        row=1
        for data in filteredList:
            self.table.setItem(row,0,QTableWidgetItem(str(data[0])))
            self.table.setItem(row,1,QTableWidgetItem(data[1]))
            # self.table.setItem(row,2,QTableWidget(data[2]))
            row+=1

       
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        self.setLayout(layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
