from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

                                                ########### For Database #############
import sqlite3
import SQLiteDB_Design

import project2

import sys
from os import path

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))

class MainApp(QMainWindow,FORM_CLASS):
   ### Constructor ###
   def __init__(self,parent=None):
      super(MainApp,self).__init__(parent)
      QMainWindow.__init__(self)
      self.setupUi(self)
      ##### Function will be called once program is opened #####
      self.connect_DB()
      self.Button_Actions()
      self.modify_Ui()
      self.tabWidget.tabBar().setVisible(False)
      self.setGeometry(400,250,1300,700)
      qtRectangle = self.frameGeometry()
      centerPoint = QDesktopWidget().availableGeometry().center()
      qtRectangle.moveCenter(centerPoint)
      self.move(qtRectangle.topLeft())         

      
      # self.get_Employees()

   def modify_Ui(self):
       self.tabWidget.tabBar().setVisible(True)

   def connect_DB(self):
      self.conn=sqlite3.connect('projectDB.db')
      self.c=self.conn.cursor()

   def Button_Actions(self):
      self.pushButton_61.clicked.connect(self.Remove_From_BlackList)
      ##### The following Section is to open different Pages when button clicked #######
      self.pushButton.clicked.connect(self.open_BookingTap)
      self.pushButton_31.clicked.connect(self.Show_Hotels)
      self.pushButton_13.clicked.connect(self.open_EmployeeTab)
      self.pushButton_49.clicked.connect(self.open_AddEmployee)
      # self.pushButton_14.clicked.connect(self.open_AddEmployee)
      # self.pushButton_21.clicked.connect(self.open_EditBookingTap)
      # self.pushButton_2.clicked.connect(self.open_EditBookingTap)
      self.pushButton_32.clicked.connect(self.open_BlacklistTab)
      self.pushButton_3.clicked.connect(self.open_newServicePage)
      self.pushButton_16.clicked.connect(self.Logout)
      # self.pushButton_10.clicked.connect(self.Display_newRoomForm)      
      ############# To Handle Process of Add new Employee ###############
      self.pushButton_15.clicked.connect(self.Add_Employee)
      ############ Hashelha #############################################
      # self.pushButton_2.clicked.connect(self.open_EditBookingTap)
      ############ EDIT BOOKING REQUEST #####################
      # self.pushButton_33.clicked.connect(self.Edit_Booking)
      ############# get list of guests ###############
      self.pushButton_40.clicked.connect(self.get_Guests)
      self.pushButton_29.clicked.connect(self.Remove_Tasks)
      ############ Search By ########################
      self.pushButton_69.clicked.connect(self.Search_By)
      ############ serch in blacklist tab ############
      self.pushButton_60.clicked.connect(self.Handle_BlackList)
      ############# add to blacklist ####################
      self.pushButton_24.clicked.connect(self.Add_To_BlackList)
      ############ add tasks ########################
      self.pushButton_28.clicked.connect(self.Add_Tasks)
      ############ Remove Tasks ####################
      self.pushButton_29.clicked.connect(self.Remove_Tasks)
      ############ open service page ################
      self.pushButton_6.clicked.connect(self.open_ServicesTap)
      ############Display All Services#############
      self.pushButton_30.clicked.connect(self.Display_Services)
      ########### Add new Service ################
      self.pushButton_20.clicked.connect(self.Add_newService)
      ########### open page of addign new service ########
      self.pushButton_19.clicked.connect(self.open_newServicePage)
      ############## Display Employee ################
      self.pushButton_39.clicked.connect(self.get_Employees)
      ########### Adding Discount #########################
      self.pushButton_8.clicked.connect(self.open_DiscountPage)
      ########### Insert Discount ########################
      self.pushButton_26.clicked.connect(self.insert_Discount)
      self.pushButton_5.clicked.connect(self.open_HotelsPageTab)

      self.pushButton_4.clicked.connect(self.open_roomsTap)
      self.pushButton_38.clicked.connect(self.Display_All_Rooms)
      self.pushButton_9.clicked.connect(self.Display_newRoomForm)
      self.pushButton_25.clicked.connect(self.open_TasksTap)
      self.pushButton_12.clicked.connect(self.Save_newRoom)
      self.pushButton_71.clicked.connect(self.Display_All_Tasks)
      self.pushButton_27.clicked.connect(self.open_Edit_TaskPage)
      self.pushButton_7.clicked.connect(self.open_AddHotelsPage)
      self.pushButton_34.clicked.connect(self.saveNewHotel)


####################### DONE ##################################################################
   def saveNewHotel(self):
      hotelid=self.lineEdit_27.text()
      hotelname=self.lineEdit_26.text()
      hotellocation=self.lineEdit_28.text()
      hotelrooms=self.lineEdit_29.text()
      query=(""" INSERT OR IGNORE INTO Hotels (ID,Name,Location,RoomsNo) VALUES (?,?,?,?)""")
      self.c.execute(query,(hotelid,hotelname,hotellocation,hotelrooms))
      self.conn.commit()
      self.lineEdit_27.setText("")
      self.lineEdit_26.setText("")
      self.lineEdit_28.setText("")
      self.lineEdit_29.setText("")

   def open_HotelsPageTab(self):
      self.tabWidget.setCurrentIndex(11)
   def open_AddHotelsPage(self):
      self.tabWidget.setCurrentIndex(12)      
   def Show_Hotels(Self):
      Entry1 = Self.conn.execute("SELECT ID, Name,Location,RoomsNo FROM Hotels")
      HotelData=Entry1.fetchall()
      counter=0
      for t in HotelData:
         counter+=1
      if Self.tableWidget_11.rowCount()<=counter:
         Self.tableWidget_11.insertRow(0)
         for row,form in enumerate(HotelData):
            for col,item in enumerate(form):
               Self.tableWidget_11.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=Self.tableWidget_11.rowCount()
            Self.tableWidget_11.insertRow(rowPosition)                     
##########################################################################################

   def open_Edit_TaskPage(self):
      self.tabWidget.setCurrentIndex(5)

   def Display_All_Tasks(self):
      DataQuery=("""SELECT ID,Date,Task,Status,Hotel,EmployeeName
                  FROM Tasks """)
      self.c.execute(DataQuery)
      self.conn.commit()
      Tasks=self.c.fetchall()
      if self.tableWidget_9.rowCount()<=len(Tasks):
         if len(Tasks)>0:
            empname=Tasks[0][5]
            getEMpQuery=("SELECT Position FROM EmployeeInfo WHERE Name=?")
            self.c.execute(getEMpQuery,(empname,))
            self.conn.commit()
            empposition=self.c.fetchall()[0][0]
            printedData=(Tasks[0][0],Tasks[0][1],Tasks[0][5],empposition,Tasks[0][4],Tasks[0][2],Tasks[0][3])
            counter=0
            for item in printedData:
               counter=counter+1
            if self.tableWidget_9.rowCount()<=counter:
               self.tableWidget_9.insertRow(0)
               for row,form in enumerate(Tasks):
                  for col,item in enumerate(form):
                     self.tableWidget_9.setItem(row,col,QTableWidgetItem(str(item)))
                     col=col+1
                  rowPosition=self.tableWidget_9.rowCount()
                  self.tableWidget_9.insertRow(rowPosition)                      
#####################################################################################################

   def Save_newRoom(Self):
      hotel=Self.lineEdit_6.text()
      Type=Self.lineEdit_3.text()
      occup=Self.lineEdit_52.text()
      PPN=Self.lineEdit_51.text()
      query=(""" INSERT OR IGNORE INTO RoomInfo (Hotel,Type,PricePerNight,occupancy) VALUES (?,?,?,?) """)
      Entryvalue=(hotel,Type,PPN,occup)
      Self.c.execute(query,Entryvalue)
      Self.conn.commit()
      Self.lineEdit_6.setText("")
      Self.lineEdit_3.setText("")
      Self.lineEdit_4.setText("")
      Self.lineEdit_52.setText("")
      Self.lineEdit_51.setText("")
###########################################################      
   def Logout(self):
      self.mainobj=project2.Intro_Main(0,"")
      self.mainobj.show()
      self.close()
######################################################
   def open_TasksTap(self):
      self.tabWidget.setCurrentIndex(4)
#############################################################
   def open_roomsTap(self):
      Self.tabWidget.setCurrentIndex(2)
######################################################      
   def Display_All_Rooms(Self):   
      Self.c.execute("SELECT * FROM RoomInfo")
      Self.conn.commit()
      RoomData=Self.c.fetchall()
      counter=0
      for atuple in RoomData:
         counter=counter+1
      if Self.tableWidget.rowCount()<=counter:
         Self.tableWidget.insertRow(0)
         for row,form in enumerate(RoomData):
            for col,item in enumerate(form):
               Self.tableWidget.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=Self.tableWidget.rowCount()
            Self.tableWidget.insertRow(rowPosition) 
#######################################################      
   def Display_newRoomForm(self):
      self.tabWidget.setCurrentIndex(3)    
#####################################################

   def open_AddEmployee(Self):
      Self.tabWidget.setCurrentIndex(7)
   def open_DiscountPage(Self):
      Self.tabWidget.setCurrentIndex(10)   

   def open_BookingTap(Self):
      Self.tabWidget.setCurrentIndex(0) 

   def open_EmployeeTab(Self):
      Self.tabWidget.setCurrentIndex(6)  

   def open_ServicesTap(Self):
      Self.tabWidget.setCurrentIndex(8)
   def open_newServicePage(self):
      self.tabWidget.setCurrentIndex(9)       

################### this section for adding new employees #########################################
   def Add_Employee(Self):
      EmpID=Self.lineEdit_10.text()
      EmpName=Self.lineEdit_9.text()
      EmpMail=Self.lineEdit_12.text()
      EmpPass=Self.lineEdit_34.text()
      EmpMob=Self.lineEdit_13.text()
      EmpHotel=Self.lineEdit_8.text()
      EmpPos=Self.lineEdit_35.text()
      Entry=(EmpID,EmpName,EmpMail,EmpPass,EmpMob,EmpHotel,EmpPos)
      queryA=(""" INSERT OR IGNORE INTO EmployeeInfo
                      (ID,Name,Email,Password,Mobile,Branch,Position) VALUES (?,?,?,?,?,?,?)""")
      Self.c.execute(queryA,Entry)                
      Self.conn.commit()
      
      Self.lineEdit_10.setText("")
      Self.lineEdit_9.setText("")
      Self.lineEdit_12.setText("")
      Self.lineEdit_34.setText("")
      Self.lineEdit_13.setText("")
      Self.lineEdit_8.setText("")
      Self.lineEdit_35.setText("")
#################################################################################################        
   def open_roomsTap(self):
      self.tabWidget.setCurrentIndex(2)     

############################## Handle Tasks #####################################
   def Add_Tasks(Self):
      HotelTasked=Self.comboBox_3.currentText()
      NewEmpName=Self.lineEdit_32.text()
      NewTaskDate=Self.lineEdit_31.text()
      TaskDesc=Self.textEdit.toPlainText()
      getallemps=("SELECT Name FROM EmployeeInfo")
      Self.c.execute(getallemps)
      Self.conn.commit()
      lista=Self.c.fetchall()
      flag=0
      for atuple in lista:
         for item in atuple:
            if NewEmpName ==str(item):
               flag=1
               EntryTask=(NewTaskDate,TaskDesc,NewEmpName,HotelTasked)
               query=(""" INSERT OR IGNORE INTO Tasks (Date,Task,EmployeeName,Hotel) VALUES (?,?,?,?) """)
               Self.c.execute(query,EntryTask)
               Self.conn.commit()
      if flag==0:
         QMessageBox.about(self,"Wrong action","we have not an employee with this name, Check agin!")
      
      Self.lineEdit_32.setText("")
      Self.lineEdit_31.setText("")
      Self.textEdit.clear()

   def Remove_Tasks(Self):
      RemovedID=Self.lineEdit_33.text()
      removQuery=("DELETE FROM Tasks WHERE ID=?")
      Self.c.execute(removQuery,(RemovedID,))
      Self.conn.commit()
      Self.Display_All_Tasks()   




####################################################################################

################################ TO confirm or refuse the Booking Request ###################################################
   # def Edit_Booking(self):
   #    GuestIDNO=self.lineEdit_43.text()
   #    GuestUsername=self.lineEdit_44.text() 
   #    GuestBookingSTatus=self.comboBox_29.currentIndex()
   #    if GuestBookingSTatus==0:## REFUSED ##
   #       somequery=(""" UPDATE GuestInfo SET Booked =? WHERE ID=? AND Username=? """)
   #       self.c.execute(somequery,(0,GuestIDNO,GuestUsername))
   #       self.conn.commit()
   #       QMessageBox.about(self,"Booking Request status","Booking Request Updated Successfuly !")
   #       self.tableWidget_2.setItem(int(GuestIDNO)-1,2, QTableWidgetItem('0'))         # self.tableWidget_2.clearContents()
   #       # self.get_Guests()
   #    else:
   #       somequery=(""" UPDATE GuestInfo SET Booked =? WHERE ID=? AND Username=? """)
   #       self.c.execute(somequery,(1,GuestIDNO,GuestUsername))
   #       self.conn.commit()
   #       QMessageBox.about(self,"Booking Request status","Booking Request Updated Successfuly !")
   #       self.tableWidget_2.setItem(int(GuestIDNO)-1,2, QTableWidgetItem('1'))         # self.tableWidget_2.clearContents()
   #       # self.tableWidget_2.clearContents()
   #       # self.get_Guests()                     

   def Refresh(self):
      pass




########################################### FOR HANDLING BOOKING PAGE ###########################################################
   def get_Guests(self):
      Entry1 = self.conn.execute("SELECT ID, Username,Booked,BasicCost,CheckInDay,CheckOutDay FROM GuestInfo")
      guestsData=Entry1.fetchall()
      counter=0
      for t in guestsData:
         counter+=1
      if self.tableWidget_2.rowCount()<=counter:
         self.tableWidget_2.insertRow(0)
         for row,form in enumerate(guestsData):
            for col,item in enumerate(form):
               self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)   
              

   def Search_By(self):
      FilterIndex=self.comboBox.currentIndex()
      FilterFactor=self.FilterFactorInput.text()
      if FilterIndex==0:
         query0=(""" SELECT ID, Username,Booked,BasicCost,CheckInDay,CheckOutDay FROM GuestInfo WHERE Username=? """)
         self.c.execute(query0,(FilterFactor,))
         self.conn.commit()
         searchedData=self.c.fetchall()
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.insertRow(0)
         for row,form in enumerate(searchedData):
            for col,item in enumerate(form):
               self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)
      elif FilterIndex==1:
         query0=(""" SELECT ID, Username,Booking_Request_STatus,BasicCost,CheckInDay,CheckOutDay FROM GuestInfo WHERE ID=? """)
         self.c.execute(query0,(FilterFactor,))
         self.conn.commit()
         searchedData=self.c.fetchall()
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.insertRow(0)
         for row,form in enumerate(searchedData):
            for col,item in enumerate(form):
               self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)
      elif FilterIndex==3:
         query0=(""" SELECT ID, Username,Booking_Request_STatus,BasicCost,CheckInDay,CheckOutDay FROM GuestInfo WHERE CheckInDay=? """)
         self.c.execute(query0,(FilterFactor,))
         self.conn.commit()
         searchedData=self.c.fetchall()
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.insertRow(0)
         for row,form in enumerate(searchedData):
            for col,item in enumerate(form):
               self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)
      elif FilterIndex==4:
         query0=(""" SELECT ID, Username,Booking_Request_STatus,BasicCost,CheckInDay,CheckOutDay FROM GuestInfo WHERE Booked=? """)
         self.c.execute(query0,(FilterFactor,))
         self.conn.commit()
         searchedData=self.c.fetchall()
         self.tableWidget_2.clearContents()
         self.tableWidget_2.setRowCount(0)
         self.tableWidget_2.insertRow(0)
         for row,form in enumerate(searchedData):
            for col,item in enumerate(form):
               self.tableWidget_2.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPosition)                                   

#########################################################################################################################

#################################### Handle BlackList #################################
   def open_BlacklistTab(self):
      self.tabWidget.setCurrentIndex(1)
                         ######## SELECT GUEST AND SHOW IT ##################
   def Handle_BlackList(Self):
      FilterIndex=Self.comboBox_30.currentIndex()
      FilterFactor=Self.BlackListFilter.text()
      if FilterIndex==1:
         query1=(""" SELECT ID, Username,BlackListed FROM GuestInfo WHERE Username=? """)
         Self.c.execute(query1,(FilterFactor,))
         Self.conn.commit()
         searchedData=Self.c.fetchall()
      if FilterIndex==0:
         query0=("""SELECT ID, Username,BlackListed FROM GuestInfo WHERE ID=? """)
         Self.c.execute(query0,(FilterFactor,))
         Self.conn.commit()
         searchedData=Self.c.fetchall()

      Self.tableWidget_10.clearContents()
      Self.tableWidget_10.setRowCount(0)
      Self.tableWidget_10.insertRow(0)
      for row,form in enumerate(searchedData):
         for col,item in enumerate(form):
            Self.tableWidget_10.setItem(row,col,QTableWidgetItem(str(item)))
            col=col+1
         rowPosition=Self.tableWidget_10.rowCount()
         Self.tableWidget_10.insertRow(rowPosition)
                         ##################### ADD TO BLackList #####################
   def Add_To_BlackList(self):
      FilterIndex=self.comboBox_30.currentIndex()
      FilterFactor=self.BlackListFilter.text()
      if FilterIndex==1:
         query1=(""" UPDATE GuestInfo SET BlackListed=?,Booked=? WHERE Username=? """)
         self.c.execute(query1,(1,0,FilterFactor))
         self.conn.commit()
         searchedData=self.c.fetchall()
      if FilterIndex==0:
         query0=("""UPDATE GuestInfo SET BlackListed=?,Booked=? WHERE ID=? """)
         self.c.execute(query0,(1,0,FilterFactor))
         self.conn.commit()
         searchedData=self.c.fetchall()
      self.tableWidget_10.clearContents()
      self.tableWidget_10.setRowCount(0)
            ################# Remove From BLackList ####################3
   def Remove_From_BlackList(self):
      FilterIndex=self.comboBox_30.currentIndex()
      FilterFactor=self.BlackListFilter.text()
      if FilterIndex==1:
         query1=(""" UPDATE GuestInfo SET BlackListed=?,Booked=? WHERE Username=? """)
         self.c.execute(query1,(0,1,FilterFactor))
         self.conn.commit()
         searchedData=self.c.fetchall()
      if FilterIndex==0:
         query0=("""UPDATE GuestInfo SET BlackListed=?,Booked=? WHERE ID=? """)
         self.c.execute(query0,(1,0,FilterFactor))
         self.conn.commit()
         searchedData=self.c.fetchall()
      self.tableWidget_10.clearContents()
      self.tableWidget_10.setRowCount(0)      
############################################################################################

   def Add_Room(self):
      pass

############################### TO show all Employee ##################################
   def get_Employees(self):
      self.c.execute(""" SELECT ID,Name,Email,Password,Mobile,Branch,Position FROM EmployeeInfo """)
      data =self.c.fetchall()
      counter=0
      for atuple in data:
         counter=counter+1
      if self.tableWidget_5.rowCount()<=counter:
         self.tableWidget_5.insertRow(0)
         for row,form in enumerate(data):
            for col,item in enumerate(form):
               self.tableWidget_5.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=self.tableWidget_5.rowCount() 
            self.tableWidget_5.insertRow(rowPosition)  
############################ Display ALl Servic #######################################
   def Display_Services(Self):
      Self.c.execute(""" SELECT ID,Name,Price,Hotel FROM Extra_Services """)
      Serdata =Self.c.fetchall()
      counter=0
      for atuple in Serdata:
         counter=counter+1
      if Self.tableWidget_8.rowCount()<=counter:
         Self.tableWidget_8.insertRow(0)      
         for row,form in enumerate(Serdata):
            for col,item in enumerate(form):
               Self.tableWidget_8.setItem(row,col,QTableWidgetItem(str(item)))
               col=col+1
            rowPosition=Self.tableWidget_8.rowCount() 
            Self.tableWidget_8.insertRow(rowPosition)
########################## ADD new service ############################
   def Add_newService(self):
      servicehotel=self.lineEdit_21.text()
      servicename=self.lineEdit_20.text()
      serviceprice=self.lineEdit_22.text()
      query=(""" INSERT OR IGNORE INTO Extra_Services (Name,Price,Hotel)
                VALUES (?,?,?) """)
      serviceEntry=(servicename,serviceprice,servicehotel)
      self.c.execute(query,serviceEntry)
      self.conn.commit()
      self.lineEdit_21.setText("")
      self.lineEdit_20.setText("")
      self.lineEdit_22.setText("")
###################### insert Discount #################################
   def insert_Discount(Self):
      DiscountCode=Self.lineEdit_23.text()
      DiscountTo=Self.lineEdit_25.text()
      DiscountValue=Self.lineEdit_24.text()
      FilterIndex=Self.comboBox_4.currentIndex()
      FilterFactor=DiscountTo
      querytogetbasiccost=(""" SELECT BasicCost FROM GuestInfo WHERE Username=? """)
      Self.c.execute(querytogetbasiccost,(FilterFactor,))
      Self.conn.commit()
      basiccostbefore=float(Self.c.fetchall()[0][0])
      finalafterdiscount=basiccostbefore-float(DiscountValue)
      if FilterIndex==1:
         query1=("""   UPDATE GuestInfo SET Discount =?,Cost_After_Discount=? WHERE Username=?""")
         Self.c.execute(query1,(DiscountValue,finalafterdiscount,FilterFactor))
         Self.conn.commit()
        
      if FilterIndex==0:
         query0=("""  UPDATE GuestInfo SET Discount =?,Cost_After_Discount=? WHERE ID=?  """)
         Self.c.execute(query0,(DiscountValue,finalafterdiscount,FilterFactor))
         Self.conn.commit()

        

         

      

      





def main():
   app=QApplication(sys.argv)
   window=MainApp()
   window.show()
   app.exec_()

if __name__ == '__main__':
     main()