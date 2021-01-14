from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import project2
import index
import sqlite3
import SQLiteDB_Design
import pytest
import tharwathotel
import project
import booking_before_edit
from time import sleep

@pytest.fixture
def app1(qtbot):
    window = tharwathotel.App_WindowHurghada(0,"","")
    qtbot.addWidget(window)
    return window

@pytest.fixture
def app2(qtbot):
    dahab_window = project.MainDahab(0,"","")
    qtbot.addWidget(dahab_window)
    return dahab_window

def test_button_open_booking_Hurghada(app1, qtbot):
                       # --> open_Booking    
    qtbot.mouseClick(app1.BookBtn, QtCore.Qt.LeftButton)
    booking_window = booking_before_edit.MainBookingPage(0,"","")
    assert booking_window.isHidden()

def test_Buttons_Back_to_main_Hurghada(app1, qtbot):
                      # --> Back_To_Main   
    qtbot.mouseClick(app1.pushButton_2, QtCore.Qt.LeftButton)
    backtomain_window = project2.Intro_Main(0,"")
    assert backtomain_window.isHidden()    
      
def test_Buttons_open_booking_Dahab(app2, qtbot):
                      # --> open_Booking    
    qtbot.mouseClick(app2.book_button1, QtCore.Qt.LeftButton)
    booking_window = booking_before_edit.MainBookingPage(1,"","")
    assert booking_window.isHidden()    
      
def test_Buttons_Back_to_main_Dahab(app2, qtbot):
                      # --> Back_To_Main   
    qtbot.mouseClick(app2.pushButton, QtCore.Qt.LeftButton)
    backtomain_window =project2.Intro_Main(0,"")
    assert backtomain_window.isHidden()   