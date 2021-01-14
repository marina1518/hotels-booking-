from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import project2
import index
import tharwatsignup
import sqlite3
import SQLiteDB_Design
import pytest
from time import sleep

@pytest.fixture 
def Guest_db(qtbot):
    window = tharwatsignup.App_WindowSU()
    qtbot.addWidget(window)
    window.show()
    qtbot.wait_for_window_shown(window)
    qtbot.stopForInteraction()
    conn = sqlite3.connect('projectDB.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM GuestInfo ORDER BY rowid DESC""")
    guest_data = cur.fetchone()
    yield guest_data
    conn.close()
                        #  -->  example to check the validale of the guest data ,
                        #       you must fill the appliction by this information to check
def test_signup_validate(Guest_db):
    assert Guest_db[1] == 'fadyza444@gmail.com'
    assert Guest_db[2] == 'fady'
    assert Guest_db[3] == '123456'
    
   