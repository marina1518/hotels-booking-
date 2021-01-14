import sqlite3
#to get value of comboBox_29 : value =self.comboBox.currentIndex()

#connect to database

conn=sqlite3.connect('projectDB.db')
c=conn.cursor()

c.executescript("""CREATE TABLE IF NOT EXISTS Hotels(ID INTEGER PRIMARY KEY, Name TEXT, Location TEXT, RoomsNo INTEGER) """)
conn.commit()

Entrya=(1,'Pure Life','Dahab',30)
Entryb=(2,'Pure Life','Hurghada',25)
c.execute(""" INSERT OR IGNORE INTO Hotels (ID,Name,Location,RoomsNo) VALUES (?,?,?,?)""",Entrya)
conn.commit()
c.execute(""" INSERT OR IGNORE INTO Hotels (ID,Name,Location,RoomsNo) VALUES (?,?,?,?)""",Entryb)
conn.commit()




######################################### GUEST TABLE ####################################################
c.executescript(""" CREATE TABLE IF NOT EXISTS GuestInfo
                     ( ID INTEGER PRIMARY KEY,    Email TEXT NOT NULL, 
                      Username TEXT NOT NULL,     Password TEXT NOL NULL,
                      Mobile INTEGER,             Address TEXT,
                       NationalId INTEGER,        Gender TEXT,
                       BasicCost REAL,            CheckInDay INTEGER,
                       CheckOutDay INTEGER,       CarRental INTEGER,
                       AdultsNo INTEGER,          KidsNo INTEGER,
                       RoomType TEXT,             SignedStatus INTEGER,
                       Booked INTEGER ) """)## 3andna column Hotel hna
conn.commit()

  

# c.execute(""" ALTER TABLE GuestInfo ADD Hotel TEXT""")
# conn.commit()
# c.execute("""  ALTER TABLE GuestInfo ADD BlackListed INTEGER """)
# conn.commit()
# c.execute("""  ALTER TABLE GuestInfo ADD RoomID INTEGER AUTO INCREMENT """)
# conn.commit()
# c.execute("""  ALTER TABLE GuestInfo ADD Discount Real """)
# conn.commit()
# c.execute("""  ALTER TABLE GuestInfo ADD Cost_After_Discount Real """)
# conn.commit()
# c.execute("""  ALTER TABLE GuestInfo ADD Cost_After_additionalServices Real """)
# conn.commit()

# c.execute("SELECT * FROM GuestInfo")
# guests=[description[0] for description in c.description]
# conn.commit()
# for guest in guests:
#    print(guest)
########################################## EMPLOYEE TABLE #############################################
c.executescript(""" CREATE TABLE IF NOT EXISTS EmployeeInfo
                  (ID INTEGER PRIMARY KEY,     Name TEXT,
                   Email TEXT,                  Password TEXT,
                   Mobile INTEGER,               Branch TEXT,      Position TEXT) """)
conn.commit()       
# c.execute("SELECT * FROM GuestInfo")
# conn.commit()
# print(c.fetchall())  

# queryForStatus=(""" SELECT BlackListed, Booked From GuestInfo WHERE Username=? """)
# UserName="Fady Mokhtar"
# c.execute(queryForStatus,(UserName,))
# conn.commit()
# t=c.fetchall()[0]
# print(t[1])

# query=("SELECT ID FROM GuestInfo WHERE Username=?")
# c.execute(query,('Fady Zeka',))
# conn.commit()
# print(c.fetchall())
# c.execute("DELETE FROM GuestInfo ")
# conn.commit()
# c.execute("DELETE FROM EmployeeInfo ")
# conn.commit()  
# c.execute("DELETE FROM Tasks ")
# conn.commit()  
# c.execute("DELETE FROM Extra_Services ")
# conn.commit()    
# c.execute("DELETE FROM RoomInfo")
# conn.commit()
########################################## TASKS TABLE #################################################
c.executescript(""" CREATE TABLE IF NOT EXISTS Tasks
                     (ID INTEGER PRIMARY KEY,    Date TEXT,   Task TEXT,     Status INTEGER) """)
conn.commit()
# c.execute("ALTER TABLE Tasks ADD Hotel,EmlpyeeName TEXT")
# conn.commit()
########################################## Extra Services Table #############################################
c.executescript(""" CREATE TABLE IF NOT EXISTS Extra_Services 
                  (ID INTEGER PRIMARY KEY, Name TEXT , Price REAL, Hotel TEXT) """)
conn.commit()
#######################################################################################
c.executescript(""" CREATE TABLE IF NOT EXISTS RoomInfo
                     (ID INTEGER PRIMARY KEY,Hotel TEXT,
                     Type TEXT, occupancy INTEGER,
                     PricePerNight REAL
                     ) """)
conn.commit()                     
##############################################################################












# c.executescript(""" CREATE TABLE IF NOT EXISTS BookingInfo
#                      (Booking_ID INTEGER PRIMARY KEY, Guest_ID INTEGER PRIMARY KEY )  """)

# c.executescript("""DROP TABLE IF EXISTS CAR_RENTAL""")
# conn.commit()

# c.executescript(""" CREATE TABLE IF NOT EXISTS Room
#                   () """)


# c.executescript(""" SELECT * FROM SignUpData """)
# print(c.fetchall())
# conn.commit()

# Entry=(1,'fady',0,'25147')
# c.execute(""" INSERT OR IGNORE INTO Guest (id,name,blacklisted,booking_id) VALUES (?,?,?,?)""",Entry)
# conn.commit()

# c.execute(""" ALTER TABLE Employee ADD Email TEXT""")
# conn.commit()
# c.execute(""" ALTER TABLE Employee ADD password TEXT""")
# conn.commit()
# c.execute(""" ALTER TABLE Employee ADD Hotel TEXT""")
# conn.commit()

# c.execute("SELECT * FROM Guest")
# print(c.fetchall())
# conn.commit()

# c.execute("SELECT * FROM Employee")
# print(c.fetchall())
# conn.commit()

# c.execute("SELECT * FROM Hotel")
# print(c.fetchall())
# conn.commit()

# c.execute("SELECT * FROM Room")
# print(c.fetchall())
# conn.commit()





# c.executescript("""DROP TABLE IF EXISTS Employee""")
# conn.commit()

# c.executescript("""DROP TABLE IF EXISTS Hotel""")
# conn.commit()

# c.executescript("""DROP TABLE IF EXISTS Room""")
# conn.commit()



                                              ### this query for get a list of columns names ###
# c.execute("SELECT * FROM GuestInfo") 
# names = [description[0] for description in c.description]
# conn.commit()
# for name in names:
#   print(name)
# print()

# c.execute("SELECT * FROM GuestInfo")
# guests=[description[0] for description in c.description]
# conn.commit()
# for guest in guests:
#    print(guest)


# c.execute("SELECT * FROM GuestInfo")
# conn.commit()
# print(c.fetchall())
# print
# c.execute("SELECT * FROM EmployeeInfo")
# conn.commit()
# print(c.fetchall())
# c.execute("SELECT * FROM Extra_Services ")
# conn.commit()
# print(c.fetchall())
# c.execute("SELECT * FROM Tasks ")
# conn.commit()
# print(c.fetchall())
# c.execute("SELECT * FROM RoomInfo ")
# conn.commit()
# print(c.fetchall())


conn.close()