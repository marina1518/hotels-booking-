from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
from os import path


import sqlite3
import SQLiteDB_Design
import project2

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"signuptrial.ui"))



class App_WindowSU(QMainWindow , FORM_CLASS):
    def __init__(self,parent=None):
        super(App_WindowSU, self).__init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.Handle_Ui()
        self.SignUp_connect_DB()
        self.Handle_buttons()

    def SignUp_connect_DB(self):
        self.conn=sqlite3.connect('projectDB.db')
        self.c=self.conn.cursor()

    def Handle_Ui(self) :
        self.setWindowTitle('Signup')   

    def Handle_buttons(self) :
        self.pushButton.clicked.connect(self.Fill_SignUpData)
        self.pushButton_2.clicked.connect(self.Back)

    def Back(self):
        self.MainPageObject=project2.Intro_Main(0,"")
        self.MainPageObject.SignBtn.setVisible(False)
        self.MainPageObject.show()
        self.close()  
        

            
    def Fill_SignUpData(self):
        guestEmail=self.lineEdit.text()
        guestUsername=self.lineEdit_2.text()
        guestPass=self.lineEdit_3.text()
        guestPassConf=self.lineEdit_4.text()
        misseddataflag=0
        if guestEmail=="":
            misseddataflag=1
        if guestPass=="":
            misseddataflag=1
        if guestPassConf=="":
            misseddataflag=1
        if guestPassConf=="":
            misseddataflag=1
        if misseddataflag==1:
            QMessageBox.warning(self,"missed data","All filed are required")
        else:
            SignUpguestStatus=1
            if guestPass == guestPassConf:
                SignUpEntry=(guestEmail,guestUsername,guestPass,SignUpguestStatus)
                queryxx=(""" INSERT OR IGNORE INTO GuestInfo 
                                (Email,Username,Password,SignedStatus) VALUES (?,?,?,?)""")
                self.c.execute(queryxx,SignUpEntry)
                self.conn.commit()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.BackTOMainObject=project2.Intro_Main(SignUpguestStatus,guestUsername)
                self.BackTOMainObject.pushButton.setVisible(False)
                self.BackTOMainObject.pushButton_2.setVisible(False)
                self.BackTOMainObject.SignBtn.setVisible(True)
                self.BackTOMainObject.SignBtn.setText(guestUsername)
                self.BackTOMainObject.show()
                self.close()
            else:
                QMessageBox.warning(self,"Incorrect Password","Please enter the same password to sign up successfully!")
                self.lineEdit_4.setText("")  
        
def main():
    app = QApplication(sys.argv)
    window = App_WindowSU()
    window.show()
    app.exec_()
   
if __name__ == "__main__":
    main()