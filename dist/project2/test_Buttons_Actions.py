from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import project2
import index
import sqlite3
import SQLiteDB_Design
import pytest
from time import sleep

@pytest.fixture
def app(qtbot):
    window = index.MainApp()
    qtbot.addWidget(window)

    return window

def test_Buttons(app, qtbot):
                       # --> open_BookingTap     
    qtbot.mouseClick(app.pushButton, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 0

                       # --> open_EmployeeTab
    qtbot.mouseClick(app.pushButton_13, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 6

                       # --> open_AddEmployee
    qtbot.mouseClick(app.pushButton_49, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 7

                       # --> open_BlacklistTab
    qtbot.mouseClick(app.pushButton_32, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 1
    
                       # --> open_ServicesTap
    qtbot.mouseClick(app.pushButton_6, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 8

                       # --> open_newServicePage
    qtbot.mouseClick(app.pushButton_3, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 9

                       # --> open_roomsTap
    qtbot.mouseClick(app.pushButton_4, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 2

                       # --> open_TasksTap
    qtbot.mouseClick(app.pushButton_25, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 4

                       # --> Display_newRoomForm
    qtbot.mouseClick(app.pushButton_9, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 3

                       # --> open_Edit_TaskPage
    qtbot.mouseClick(app.pushButton_27, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 5

                        # --> open_DiscountPage
    qtbot.mouseClick(app.pushButton_8, QtCore.Qt.LeftButton)
    assert app.tabWidget.currentIndex() == 10


    