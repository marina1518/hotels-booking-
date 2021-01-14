from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import datetime
import sqlite3
import SQLiteDB_Design
import project2

import sys

MainUI,_ = loadUiType('BOOKING.ui')

class MainBookingPage(QMainWindow , MainUI):
    def __init__(self,STATUSOFUSER,HotelName,UserName ,parent=None):
        super(MainBookingPage, self). __init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")
        self.Transation()
        self.Booking_ConnectDB()
        self.showCostbtn.setCheckable(True)
        self.CostDisplay.setReadOnly(True)
        self.stateofuser=STATUSOFUSER
        self.HotelName=HotelName
        self.UserName=UserName
        #print(self.UserName)
        self.setGeometry(600,300,1000,600)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())           

    def Booking_ConnectDB(Self):
        Self.conn=sqlite3.connect('projectDB.db')
        Self.c=Self.conn.cursor()        

    def Transation(Self):
        Self.pushButton_4.clicked.connect(Self.Filling_Booking_Data)
        Self.pushButton.clicked.connect(Self.LogOut)
        Self.pushButton_5.clicked.connect(Self.Check_Booking_Request_Status)
        Self.showCostbtn.clicked.connect(Self.showCost)    
        
        
    def LogOut(Self):
        Self.MainPageObject=project2.Intro_Main(0,"")
        query=("UPDATE GuestInfo SET SignedStatus=? WHERE Username=?")
        entry=(0,Self.UserName)
        Self.c.execute(query,entry)
        Self.conn.commit()
        Self.MainPageObject.show()
        Self.close()         
####################################################################################################        
    SignleRoomPerNight=600
    DoubleRoomPerNight=450
    FamilyRoomPerNight=350
    Total_Price=float(0)
    BookUsername=""
    BookPassword=""
    BookEmail=""
    BookMobile=""
    BookAddress=""
    BookNationalId=""
    BookGender=""
    RoomType=""
    AdultsNo=0
    KidsNo=0
    TaxiRequest=0
    checkInDateDay=0
    checkOutDateDay=0

    def Filling_Booking_Data(Self):
        flag=1
        Self.BookUsername=Self.lineEdit_7.text()
        if Self.BookUsername=="":
            flag=0
        Self.BookPassword=Self.lineEdit_8.text()
        if Self.BookPassword=="":
            flag=0        
        Self.BookEmail=Self.lineEdit_11.text()
        if Self.BookEmail=="":
            flag=0
        Self.BookMobile=Self.lineEdit_12.text()
        x=str(Self.lineEdit_12.text())
        if x=="":
            flag=0
        Self.BookAddress=Self.lineEdit_9.text()
        if Self.BookAddress=="":
            flag=0
        Self.BookNationalId=Self.lineEdit_10.text()
        y=str(Self.lineEdit_10.text())
        if y=="":
            flag=0
        if Self.radioButton.isChecked():

            if Self.lineEdit_21.text()=="":
                flag=0
            if Self.lineEdit_14.text()=="":
                flag=0            
            if Self.lineEdit_15.text()=="":
                flag=0
            if Self.lineEdit_16.text()=="":
                flag=0
        elif Self.radioButton_2.isChecked():

            if Self.lineEdit_20.text()=="":
                flag=0
            if Self.lineEdit_13.text()=="":
                flag=0
            if Self.lineEdit_19.text()=="":
                flag=0
            if Self.lineEdit_17.text()=="":
                flag=0
            if Self.lineEdit_18.text()=="":
                flag=0                                                                        
        if flag==0:
            QMessageBox.about(Self,"Missing Data","All Data should be filled befor Booking!")
        else:    
            if Self.radioButton_7.isChecked()==True:
                Self.BookGender='Male'
            elif Self.radioButton_3.isChecked()==True:
                Self.BookGender="Female"    
            Self.RoomType=Self.comboBox_2.currentText()
            Self.AdultsNo=Self.spinBox_4.value()
            Self.KidsNo=Self.spinBox_3.value()
            if Self.radioButton_9.isChecked()==True:
                Self.TaxiRequest=1
            elif Self.radioButton_8.isChecked()==True:
                Self.TaxiRequest=0
            checkInDate=Self.dateEdit_4.date()
            checkInDate=checkInDate.toString()
            checkInDate=checkInDate.split()
            checkInDay=checkInDate[0]
            Self.checkInDateDay=int(checkInDate[2])
            checkInDateMonth=checkInDate[1]
            checkInDateYear=checkInDate[3]
            checkOutDate=Self.dateEdit_3.date()
            checkOutDate=checkOutDate.toString()
            checkOutDate=checkOutDate.split()
            checkOutDay=checkOutDate[0]
            Self.checkOutDateDay=int(checkOutDate[2])
            checkOutDateMonth=checkOutDate[1]
            checkOutDateYear=checkOutDate[3]
            if Self.RoomType=='Single':
                Self.Total_Price=Self.Total_Price+(Self.SignleRoomPerNight*(Self.checkOutDateDay-Self.checkInDateDay+1))
            elif Self.RoomType=='Double':
                Self.Total_Price=Self.Total_Price+(Self.DoubleRoomPerNight*(Self.checkOutDateDay-Self.checkInDateDay+1))
            elif Self.RoomType=='Family':
                Self.Total_Price=Self.Total_Price+(Self.FamilyRoomPerNight*(Self.checkOutDateDay-Self.checkInDateDay+1))
            if Self.TaxiRequest==1:
                Self.Total_Price=Self.Total_Price+200
            if Self.TaxiRequest==1:
                Self.Total_Price=Self.Total_Price+200
            Self.c.execute("SELECT Username FROM GuestInfo")
            Self.conn.commit()        
            for Atuple in Self.c.fetchall():
                for Ausername in Atuple:
                    if Self.BookUsername==Ausername:
                        newQuery=(""" UPDATE GuestInfo
                                        SET Mobile = ?,Address=?,NationalId=?,Gender=?,BasicCost=?,CheckInDay=?,CheckOutDay=?,
                                            CarRental=?,AdultsNo=?,KidsNo=?,RoomType=?,SignedStatus=?,Booked=?,Hotel=?
                                        WHERE Username=?  """)
                        Self.c.execute(newQuery,(Self.BookMobile,Self.BookAddress,Self.BookNationalId,Self.BookGender,Self.Total_Price,
                                                Self.checkInDateDay,Self.checkOutDateDay,Self.TaxiRequest,Self.AdultsNo,
                                                Self.KidsNo,Self.RoomType,1,1,Self.HotelName,Self.BookUsername))
                        Self.conn.commit()

    def showCost(self):
        Self.CostDisplay.setText(str(Self.Total_Price))

        # anotherquery=("SELECT * FROM GuestInfo WHERE Username=?")
        # Self.c.execute(anotherquery,(Self.BookUsername,))
        # Self.conn.commit()
        # for item in Self.c.fetchall():
        #     print(item)

    # def Check_Booking_Request_Status(self):
    #     queryForStatus=(""" SELECT BlackListed, Booked From GuestInfo WHERE Username=? """)
    #     self.c.execute(queryForStatus,(self.UserName,))
    #     self.conn.commit()
    #     x=self.c.fetchall()
    #     BlackListed,Booked = [list(c) for c in zip(*x)]
    #     BlackListedIndicator=BlackListed[0]
    #     BookedIndicator=Booked[0]
    #     # BlackListedStatus=self.c.fetchall()[0][0]
    #     # BookedStatus=self.c.fetchall()[0][1]
    #     print(self.c.fetchall())
    #     if BookedIndicator==1:
    #         if BlackListedIndicator!=1:
    #             QMessageBox.about(self,"Your Booking Request Status","Your Booking Request is confirmed, Thank you !")
    #         else:
    #             query=("UPDATE GuestInfo SET Booked=? WHERE Username=?")
    #             entry=(0,Self.UserName)
    #             Self.c.execute(query,entry)
    #             Self.conn.commit()
    #             QMessageBox.about(self,"Your Booking Request Status","we sorry to be late, you will know soon the status of your booking request, Have a nice day!")
    #     else:
    #         QMessageBox.about(self,"Your Booking Request Status","sorry but you are not booked yet!")


    #         Self.CostDisplay.setText(str(Self.Total_Price))
            
    #         QMessageBox.about(Self,"response","The total Cost is {}".format(self.Total_Price))
    #         msgbox.show()

            
    #         ## Now i will check if This User already Signed in or not to add to it the other data ##
    #         Self.c.execute("SELECT Username FROM GuestInfo")
    #         Self.conn.commit()        
    #         for Atuple in Self.c.fetchall():
    #             for Ausername in Atuple:
    #                 if Self.BookUsername==Ausername:
    #                     newQuery=(""" UPDATE GuestInfo
    #                                     SET Mobile = ?,Address=?,NationalId=?,Gender=?,BasicCost=?,CheckInDay=?,CheckOutDay=?,
    #                                         CarRental=?,AdultsNo=?,KidsNo=?,RoomType=?,SignedStatus=?,Booked=?,Hotel=?
    #                                     WHERE Username=?  """)
    #                     Self.c.execute(newQuery,(Self.BookMobile,Self.BookAddress,Self.BookNationalId,Self.BookGender,Self.Total_Price,
    #                                             Self.checkInDateDay,Self.checkOutDateDay,Self.TaxiRequest,Self.AdultsNo,
    #                                             Self.KidsNo,Self.RoomType,Self.stateofuser,'None',Self.HotelName,Self.BookUsername))
    #                     Self.conn.commit()


    #     # anotherquery=("SELECT * FROM GuestInfo WHERE Username=?")
    #     # Self.c.execute(anotherquery,(Self.BookUsername,))
    #     # Self.conn.commit()
    #     # for item in Self.c.fetchall():
    #     #     print(item)

    def Check_Booking_Request_Status(self):
        queryForStatus=(""" SELECT BlackListed, Booked From GuestInfo WHERE Username=? """)
        self.c.execute(queryForStatus,(self.UserName,))
        self.conn.commit()
        y=self.c.fetchall()
        BlackListedIndicator=0
        BookedIndicator=0
        for typ in y:
            (BlacklistedIndicator,BookedIndicator)=typ
        if BookedIndicator==1:
            if BlackListedIndicator!=1:
                QMessageBox.about(self,"Your Booking Request Status","we will let you know as soon as possible, Thank you !")
            elif BlacklistedIndicator==1:
                query=("UPDATE GuestInfo SET Booked=? WHERE Username=?")
                entry=(0,self.UserName)
                self.c.execute(query,entry)
                self.conn.commit()
                QMessageBox.about(self,"Your Booking Request Status","your booking request is refused")
        else:
            QMessageBox.about(self,"Your Booking Request Status","sorry but you are not booked yet!")

            ## Now i will check if This User already Signed in or not to add to it the other data ##
        self.c.execute("SELECT Username FROM GuestInfo")
        self.conn.commit()        
        for Atuple in self.c.fetchall():
            for Ausername in Atuple:
                if self.BookUsername==Ausername:
                    newQuery=(""" UPDATE GuestInfo
                                    SET Mobile = ?,Address=?,NationalId=?,Gender=?,BasicCost=?,CheckInDay=?,CheckOutDay=?,
                                        CarRental=?,AdultsNo=?,KidsNo=?,RoomType=?,SignedStatus=?,Booked=?,Hotel=?
                                    WHERE Username=?  """)
                    self.c.execute(newQuery,(self.BookMobile,self.BookAddress,self.BookNationalId,self.BookGender,self.Total_Price,
                                            self.checkInDateDay,self.checkOutDateDay,self.TaxiRequest,self.AdultsNo,
                                            self.KidsNo,self.RoomType,self.stateofuser,'None',self.HotelName,self.BookUsername))
                    self.conn.commit()                


        #     QMessageBox.warning(self," ","This User isn't found in our system")
        # else:
        #     query=(""" SELECT BlackListed, Booked FROM GuestInfo WHERE Username=? """)
        #     self.c.execute(query,(self.BookUsername,))
        #     conn.commit()
        #     x=c.fetchall()
        #     for tup in x:
        #         (BlackListedIndicator,BookedIndicator)=tup
        #     if BookedIndicator==1:
        #         if BlackListedIndicator==0:
        #             QMessageBox.about(self,"Your Booking Request Status","Your Booking Request is confirmed, Thank you !")
        #         else:
        #             if BlackListedIndicator==1:
        #                 query=("UPDATE GuestInfo SET Booked=? WHERE Username=?")
        #                 entry=(0,self.UserName)
        #                 Self.c.execute(query,entry)
        #                 Self.conn.commit()
        #                 QMessageBox.about(self,"Your Booking Request Status","Unfortunately,your booking request is refused!")
        #             else:
        #                 QMessageBox.about(Self,"Your Booking Request status","sorry to be late in response, we will respond as fast as possible!")
        #     else:
        #         QMessageBox.about(self,"Your Booking Request Status","sorry but you are not booked yet!")




    

        #Self.listView.addItem(Total_Price)
   

    # def get_Cost(Self):
    #     print(Self.Total_Price)    

    





def main():
    app = QApplication(sys.argv)
    window = MainBookingPage(0,"","")
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
