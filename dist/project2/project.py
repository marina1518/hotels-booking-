from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
from PyQt5.uic.properties import QtWidgets
######################################## import another pages ########################################
import booking_before_edit 
import project2
#####################################################################################################

MainUI,_ = loadUiType('hotel2.ui')
class MainDahab(QMainWindow, MainUI):
    def __init__(self,guestStatus,HotelName,UserName ,parent=None):
        super(MainDahab, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")
        self.Transation()
        self.guestStatus=guestStatus
        self.HotelName=HotelName
        self.UserName=UserName
        self.setGeometry(600,300,1000,600)

    def Transation(self):
        self.book_button1.clicked.connect(self.open_Booking)
        self.pushButton.clicked.connect(self.Back_To_MainPage)

    def open_Booking(self):
        if self.guestStatus==1:
            self.BookPageObj=booking_before_edit.MainBookingPage(self.guestStatus,self.HotelName,self.UserName)
            self.BookPageObj.show()
            self.close()
        else:
            QMessageBox.warning(self,"Not Signed yet","You can't Book without being signed in, please if you have an account use it to log in or create a new account, Have a nice day!")    
            self.IntroObj=project2.Intro_Main(0,"")
            self.IntroObj.show()
            self.close()
    def Back_To_MainPage(self):
        if self.guestStatus==1:
            self.introObject=project2.Intro_Main(self.guestStatus,self.UserName)
            self.introObject.show()            
            self.introObject.pushButton.setVisible(False)
            self.introObject.pushButton_2.setVisible(False)
            self.close()
        else:
            self.MainPageObj=project2.Intro_Main(self.guestStatus,self.UserName)
            self.MainPageObj.show()
            self.MainPageObj.pushButton.setVisible(True)
            self.MainPageObj.pushButton_2.setVisible(True)
            self.close()    
    






def main():
    app = QApplication(sys.argv)
    window = MainDahab(0,"","")
    window.show()
    app.exec_()

if __name__ == '__main__' :
    main()
