from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pytestqt.qt_compat import qt_api
import sys
from os import path
import pytest

import project2
import tharwatsignup
import tharwatlogin
import project
import tharwathotel

@pytest.fixture 
def app1(qtbot):
    Intro_window = project2.Intro_Main(0,"")
    qtbot.addWidget(Intro_window)
    
    return Intro_window

@pytest.fixture
def app2(qtbot):
    sign_up_window = tharwatsignup.App_WindowSU()
    qtbot.addWidget(sign_up_window)
    
    return sign_up_window

@pytest.fixture
def app3(qtbot):
    Log_in_window = tharwatlogin.App_Window("")
    qtbot.addWidget(Log_in_window)
    
    return Log_in_window

@pytest.fixture
def app4(qtbot):
    Dahab_hotel_window = project.MainDahab(1,"Pure Life Hurghada","")
    qtbot.addWidget(Dahab_hotel_window)
    
    return Dahab_hotel_window

@pytest.fixture
def app5(qtbot):
    Hurghada_hotel_window = tharwathotel.App_WindowHurghada(1,"Pure Life Hurghada","")
    qtbot.addWidget(Hurghada_hotel_window)
    
    return Hurghada_hotel_window

#################################################################
def test_open_signup(app1, app2, qtbot):
    qtbot.mouseClick(app1.pushButton, QtCore.Qt.LeftButton)
    assert app2.isVisible() == 0
   

def test_open_login(app1, app3, qtbot):
    qtbot.mouseClick(app1.pushButton_2, QtCore.Qt.LeftButton)
    assert app3.isVisible() == 0

def test_open_Dahab(app1, app4, qtbot):
    qtbot.mouseClick(app1.pushButton_3, QtCore.Qt.LeftButton)
    assert app4.isVisible() == 0

def test_open_Hurghada(app1, app5, qtbot):
    qtbot.mouseClick(app1.pushButton_4, QtCore.Qt.LeftButton)
    assert app5.isVisible() == 0