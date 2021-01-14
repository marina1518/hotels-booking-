from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sqlite3
import SQLiteDB_Design

import project2
import project
import tharwathotel
import sys

MainUI,_ = loadUiType('check in.ui')

class Checkin_Main(QMainWindow , MainUI):
    def __init__(self,statusofuser ,nameofuser,parent=None):
        super(Checkin_Main, self). __init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")
        self.CheckIn_ConnectDB()
        self.Transation()
        self.USERSTATE=statusofuser
        self.USERNAME=nameofuser
        self.extrafinalcost=0
        self.pushButton_8.setText(self.USERNAME)
        self.lineEdit_2.setText(str(600))
        self.lineEdit.setText(str(300))
        self.lineEdit_6.setText(str(450))
        self.lineEdit_3.setText(str(150))
        self.lineEdit_4.setText(str(700))
        self.lineEdit_5.setText("90-250-170")

    def CheckIn_ConnectDB(Self):
        Self.conn=sqlite3.connect('projectDB.db')
        Self.c=Self.conn.cursor()        

    def Transation(Self):
        Self.pushButton_2.clicked.connect(Self.LogOut)
        Self.pushButton_9.clicked.connect(Self.Calculate_Extra_Cost)
        Self.pushButton_10.clicked.connect(Self.BrowsingDahab)
        Self.pushButton_11.clicked.connect(Self.BrowsingHurghada)

    def BrowsingDahab(self):
        self.DahabObj=project.MainDahab(self.USERSTATE,"Pure Life Hurghada",self.USERNAME)
        self.DahabObj.show()
        self.close()
    def BrowsingHurghada(Self):
        Self.hurghObj=tharwathotel.App_WindowHurghada(Self.USERSTATE,"Pure Life Hurghada",Self.USERNAME)
        Self.hurghObj.show()
        Self.close()
    def LogOut(Self):
      Self.MainPageObject=project2.Intro_Main(0,Self.USERNAME)
      Self.MainPageObject.SignBtn.setVisible(False)
      Self.MainPageObject.show()
      Self.close()

    def Calculate_Extra_Cost(self):
        if self.radioButton_6.isChecked()==1:
            self.extrafinalcost=self.extrafinalcost+600
        if self.radioButton_9.isChecked()==1:
            self.extrafinalcost=self.extrafinalcost+400            
        if self.radioButton_16.isChecked()==1:
            self.extrafinalcost=self.extrafinalcost+400        
        if self.radioButton_15.isChecked()==1:
            self.extrafinalcost=self.extrafinalcost+450
        if self.radioButton_17.isChecked()==1:
            self.extrafinalcost=self.extrafinalcost+160
        if self.radioButton_8.isChecked()==1:
            if self.checkBox_3.isChecked()==1:
                self.extrafinalcost=self.extrafinalcost+250
            if self.checkBox.isChecked()==1:
                self.extrafinalcost=self.extrafinalcost+500                
            if self.checkBox_2.isChecked()==1:
                self.extrafinalcost=self.extrafinalcost+250
        query0=("SELECT BasicCost FROM GuestInfo WHERE Username=? ")
        self.c.execute(query0,(self.USERNAME,))
        self.conn.commit()
        oldcost=self.c.fetchall()[0][0]
        totalcost=oldcost+self.extrafinalcost        
        query=("UPDATE GuestInfo SET Cost_After_additionalServices = ? WHERE Username=? ")
        self.c.execute(query,(totalcost,self.USERNAME))
        self.conn.commit()
        self.lineEdit_7.setText(str(totalcost))



def main():
    app = QApplication(sys.argv)
    window = Checkin_Main(0,"")
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
