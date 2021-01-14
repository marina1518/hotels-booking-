from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
from os import path

import sqlite3
import SQLiteDB_Design

import index
from botros import *
import project2
from check_in import *


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"login1.ui"))

class App_Window(QMainWindow , FORM_CLASS):
    def __init__(self,name,parent=None):
        super(App_Window,self).__init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.Handle_Ui()
        self.Transition()
        self.LIconnect_DB()
        self.guestname=name
        self.setGeometry(600,300,1000,600)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())      


    def LIconnect_DB(self):
        self.conn=sqlite3.connect('projectDB.db')
        self.c=self.conn.cursor()

    def Handle_Ui(self) :
        self.setWindowTitle('LOGIN')

    def Transition(self):
        self.pushButton_2.clicked.connect(self.Open_Admin)
        self.pushButton_4.clicked.connect(self.open_Staff)
        self.pushButton.clicked.connect(self.open_Guest)
        self.pushButton_3.clicked.connect(self.Back)

    def Back(Self):
        Self.MainPageObject=project2.Intro_Main(0,"")
        Self.MainPageObject.SignBtn.setVisible(False)
        Self.MainPageObject.show()
        Self.close()  


    # def open_Guest(self):
    #     EnteredUsername=self.lineEdit.text()
    #     EnteredPassword=self.lineEdit_2.text()
    #     emptyflag=0
    #     if self.lineEdit.text()=="":
    #         QMessageBox.warning(self,"empty filed","enter all data")
    #     if self.lineEdit_2.text()=="":
    #         QMessageBox.warning(self,"empty filed","enter all data")
    #     queryusers=("SELECT Username FROM GuestInfo")
    #     self.c.execute(queryusers)
    #     self.conn.commit()
    #     record=self.c.fetchall()
    #     for names in record:
    #         for name in names:
    #             if EnteredUsername ==name:
    #                 query=(""" SELECT Password FROM GuestInfo WHERE Username = ?""" )
    #                 self.c.execute(query,(EnteredUsername,))
    #                 self.conn.commit()
    #                 passes=self.c.fetchall()
    #                 for passwords in passes:
    #                     for password in passwords:
    #                         if EnteredPassword ==password:
    #                             querystatus=("SELECT Booked FROM GuestInfo WHERE Username =?")
    #                             self.c.execute(querystatus,(EnteredUsername,))
    #                             self.conn.commit()
    #                             somestates=self.c.fetchall()
    #                             for states in somestates:
    #                                 for mystatus in states:
    #                                     if mystatus==1:
    #                                         self.checkinpageobj=Checkin_Main(bookingstatus,EnteredUsername)
    #                                         self.checkinpageobj.pushButton_8.setVisible(True)
    #                                         self.checkinpageobj.show()
    #                                         self.close()
    #                                     else:    
    #                                         statusQuery=("SELECT SignedStatus FROM GuestInfo WHERE Username=? AND Password=?")
    #                                         self.c.execute(statusQuery, (EnteredUsername,EnteredPassword))
    #                                         self.conn.commit()
    #                                         signedstates=self.c.fetchall()
    #                                         for signedusers in signedstates:
    #                                             for statususer in signedusers:
    #                                                 if statususer ==1:
    #                                                     self.browseObj=project2.Intro_Main(1,EnteredUsername)
    #                                                     self.browseObj.pushButton.setVisible(True)
    #                                                     self.browseObj.pushButton_2.setVisible(True)
    #                                                     self.browseObj.SignBtn.setText(EnteredUsername)
    #                                                     self.browseObj.show()
    #                                                     self.close()
    #                                                 else:
    #                                                     self.browseObj=project2.Intro_Main(0,EnteredUsername)    
    #                                                     self.browseObj.SignBtn.setVisible(True)
    #                                                     self.browseObj.SignBtn.setEnabled(True)            
    #                                                     self.close()
    #                         else:
    #                             QMessageBox.warning(self,"Wrong pass","enter the right password")
    #             else:
    #                 QMessageBox.warning(self,"not registered","Create a new account first")                
    #     #print(rightPass)    


    def open_Guest(self):
        EnteredUsername=self.lineEdit.text()
        EnteredPassword=self.lineEdit_2.text()
        query=(""" SELECT Password FROM GuestInfo WHERE Username = ?""" )
        queryforcheckinpage=("SELECT Booked FROM GuestInfo WHERE Username=?")

        self.c.execute(query,(EnteredUsername,))
        self.conn.commit()
        rightPass=self.c.fetchall()
        mypass=""
        for passwords in rightPass:
            for item in passwords:
                mypass=item

        self.c.execute(queryforcheckinpage,(EnteredUsername,))
        self.conn.commit()
        bookingstatus=self.c.fetchall()[0][0]

        if mypass==EnteredPassword:
            if bookingstatus==1:
                self.checkinpageobj=Checkin_Main(bookingstatus,EnteredUsername)
                self.checkinpageobj.pushButton_8.setVisible(True)
                self.checkinpageobj.show()
                self.close()
            else:    
                statusQuery=("SELECT SignedStatus FROM GuestInfo WHERE Username=? AND Password=?")
                self.c.execute(statusQuery, (EnteredUsername,EnteredPassword))
                self.conn.commit()
                userstatus=self.c.fetchall()[0][0]
                self.browseObj=project2.Intro_Main(userstatus,EnteredUsername)
                if userstatus==1:
                    self.browseObj.pushButton.setVisible(False)
                    self.browseObj.pushButton_2.setVisible(False)
                self.browseObj.show()
                self.browseObj.SignBtn.setVisible(True)
                self.browseObj.SignBtn.setText(EnteredUsername)
                self.browseObj.SignBtn.setEnabled(False)            
                self.close()
        else:
            QMessageBox.warning(self,"Incorrect Password","Please enter the right password")
            self.lineEdit_2.setText("")    
        #print(rightPass)  






    # def open_Guest(self):
    #     flag=0
    #     EnteredUsername=self.lineEdit.text()
    #     EnteredPassword=self.lineEdit_2.text()
    #     emptydataflag=0
    #     if EnteredPassword=="":
    #         emptydataflag=1
    #     if EnteredUsername=="":
    #         emptydataflag=1    
    #     if emptydataflag==1:
    #         QMessageBox.warning(self,"Missed Data !!","All Field are requiered")
    #     else:
    #         self.c.execute("SELECT Username FROM GuestInfo")
    #         self.conn.commit()
    #         names=self.c.fetchall()
    #         for usernames in names:
    #             for username in names:
                    
    #                 if EnteredUsername==username:
    #                     self.c.execute("SELECT Password FROM GuestInfo WHERE Username=?",(EnteredUsername,))
    #                     self.conn.commit()
    #                     passcheck=self.c.fetchone()
    #                     if EnteredPassword != passcheck[0]:
    #                         QMessageBox.warning(self,"Wrong Password","Enter the right Password")
    #                     else:
    #                         queryforcheckinpage=("SELECT Booked FROM GuestInfo WHERE Username=?")
    #                         self.c.execute(queryforcheckinpage,(EnteredUsername,))
    #                         self.conn.commit()
    #                         bookingstatus=self.c.fetchall()[0][0]
    #                         if bookingstatus==1:
    #                             self.checkinpageobj=Checkin_Main(1,EnteredUsername)
    #                             self.checkinpageobj.pushButton_8.setVisible(True)
    #                             self.checkinpageobj.show()
    #                             self.close()
    #                         else:    
    #                             statusQuery=("SELECT SignedStatus FROM GuestInfo WHERE Username=? AND Password=?")
    #                             self.c.execute(statusQuery, (EnteredUsername,EnteredPassword))
    #                             self.conn.commit()
    #                             userstatus=self.c.fetchall()[0][0]
    #                             self.browseObj=project2.Intro_Main(userstatus,EnteredUsername)
    #                             if userstatus==1:
    #                                 self.browseObj.pushButton.setVisible(False)
    #                                 self.browseObj.pushButton_2.setVisible(False)
    #                                 self.browseObj.show()
    #                                 self.browseObj.SignBtn.setVisible(True)
    #                                 self.browseObj.SignBtn.setText(EnteredUsername)
    #                                 self.browseObj.SignBtn.setEnabled(False)            
    #                                 self.close()
    #                 else:
    #                     QMessageBox.about(self,"not registered","Create account first") 


    def Open_Admin(self):
        if self.lineEdit_3.text()=="PureLifeAdmin" and self.lineEdit_4.text()=="PureLifeAdmin":
            self.obj=index.MainApp()
            self.obj.show()
            self.close()
        else:
            QMessageBox.about(self,"Un-Avalible Access!!!","Enter the right data for accessing!")    
            
        
    def open_Staff(self):
        staffUser=self.lineEdit_5.text()
        staffPass=self.lineEdit_6.text()
        query=("SELECT Password FROM EmployeeInfo WHERE Name =?")
        self.c.execute(query,(staffUser,))
        self.conn.commit()
        sure=self.c.fetchall()[0][0]
        if sure==staffPass:
            self.staffObj=Botros(staffUser)
            self.staffObj.show()
            self.close()
        else:
            QMessageBox.warning(self,"Incorrect Password","Please enter the right password")
            self.lineEdit_6.setText("")                         
        
        
def main():
    app = QApplication(sys.argv)
    window = App_Window("")
    window.show()
    app.exec_()
   
if __name__ == "__main__":
    main()