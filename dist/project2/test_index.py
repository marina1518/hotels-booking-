from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import project2
import index
import sqlite3
import SQLiteDB_Design
import pytest
from time import sleep

@pytest.fixture 
def data(qtbot):
    window = index.MainApp()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait_for_window_shown(window)
    qtbot.stopForInteraction()
    return data
    
                        #  -->  example to check data base of new employees ,
                        #       you must fill the appliction by this information to check
def test_add_employee(data):
    conn = sqlite3.connect('projectDB.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM EmployeeInfo ORDER BY rowid DESC""")
    employee_data = cur.fetchone()
    assert employee_data[0] == 27
    assert employee_data[1] == 'ayman'
    assert employee_data[2] == 'ayman456@gmail.com'
    assert employee_data[3] == '123456'
    assert employee_data[4] == 123789
    assert employee_data[5] == 'dahab'
    assert employee_data[6] == 'manager'
    conn.close()

                        #  -->  example to check data base of new rooms ,
                        #       you must fill the appliction by this information to check
def test_save_newroom(data):
    conn = sqlite3.connect('projectDB.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM RoomInfo ORDER BY rowid DESC""")
    Room_data = cur.fetchone()
    assert Room_data[1] == 'dahab'
    assert Room_data[2] == 'single'
    assert Room_data[3] == 4
    assert Room_data[4] == 415.50
    conn.close() 

                        #  -->  example to check data base of new services ,
                        #       you must fill the appliction by this information to check
def test_Add_newService(data):
    conn = sqlite3.connect('projectDB.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Extra_Services ORDER BY rowid DESC""")
    newService_data = cur.fetchone()
    assert newService_data[3] == 'dahab'
    assert newService_data[1] == 'massage-time'
    assert newService_data[2] == 600.55
    conn.close() 
