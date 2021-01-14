from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
from os import path

import sqlite3
import SQLiteDB_Design

######################################## connected pages : [1]Login  [2]SignUp  [3]dahab and hurghada hotel #########################
import tharwatlogin 
import tharwatsignup 
import project 
import tharwathotel 
import check_in
import index
import main
import booking_before_edit
import botros
import introconverted
import signuptrial
import botros_main
import BOOKINGconverted
import signupconverted
import nevencheckin_rc
import neven_rc
import botros_main
import botros_icons_rc
import tharwathotel
import tharwatloginconverted
import mariz_rc
######################################################################################################################################


from PyQt5.uic.properties import QtWidgets

MainUI,_ = loadUiType('intro2.ui')

class Intro_Main(QMainWindow, MainUI):
    def __init__(self, USERSTATUS,USERNAME ,parent=None):
        super(Intro_Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")
        ## to connect with database ##
        self.INTRO_connect_DB()
        self.UStatus=USERSTATUS
        self.UNAME=USERNAME
        ## to go to another page ##
        self.Transation()
        ## User account Button should be hidden by default ##
        if self.UNAME=="":
            self.SignBtn.setVisible(False)
        else:
            self.SignBtn.setText(self.UNAME)      
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())            

    def INTRO_connect_DB(self):
        self.conn=sqlite3.connect('projectDB.db')
        self.c=self.conn.cursor()

    def Transation(self):
        self.pushButton_2.clicked.connect(self.open_Login)
        self.pushButton.clicked.connect(self.open_Signup)
        self.pushButton_3.clicked.connect(self.open_DahabHotel)
        self.pushButton_4.clicked.connect(self.open_HurghadaHotel)
        self.SignBtn.clicked.connect(self.openYourAccount)

        
    def openYourAccount(self):
        queryaccount=("SELECT Booked FROM GuestInfo WHERE Username=? ")
        self.c.execute(queryaccount,(self.UNAME,))
        self.conn.commit()
        bookedstate=self.c.fetchall()[0][0]
        if bookedstate==1:
            self.checkinpageobject=check_in.Checkin_Main(self.UStatus,self.UNAME)
            self.checkinpageobject.show()
            self.close()
############################# TO Open Login page ########################        
    def open_Login(self):
        self.LoginObj=tharwatlogin.App_Window(self.UNAME)
        self.LoginObj.show()
        self.close()        
############################# TO Open Signup page ########################
    def open_Signup(self):
        self.signupObj=tharwatsignup.App_WindowSU()
        self.signupObj.show()
        self.close()    
############################ Browse Dahab Hotel ##########################

    def open_DahabHotel(self):
        self.DahabObj=project.MainDahab(self.UStatus,"Pure Life Dahab",self.UNAME)
        self.DahabObj.show()
        self.close()
########################### Browse Hurghada Hotel ########################
    def open_HurghadaHotel(self):
        self.HurghadaObj=tharwathotel.App_WindowHurghada(self.UStatus,"Pure Life Hurghada",self.UNAME)
        self.HurghadaObj.show()
        self.close()
            

def main():
    app = QApplication(sys.argv)
    window = Intro_Main(0,"")
    window.show()
    app.exec_()


if __name__ == '__main__' :
    main()