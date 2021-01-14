from PyQt5 import QtCore, QtGui, QtWidgets
import pytest
import sys
from os import path

import botros

@pytest.fixture
def staff_app(qtbot):
    window = botros.Botros("")
    qtbot.addWidget(window)

    return window

def test_staff_Buttons(staff_app, qtbot):
    ############### open booking tab #######################
    qtbot.mouseClick(staff_app.pushButton, QtCore.Qt.LeftButton)
    assert staff_app.tabWidget.currentIndex() == 0

    ############### open tasks tab #######################
    qtbot.mouseClick(staff_app.pushButton_2, QtCore.Qt.LeftButton)
    assert staff_app.tabWidget.currentIndex() == 1

    ############### open editing tasks tab #######################
    qtbot.mouseClick(staff_app.pushButton_3, QtCore.Qt.LeftButton)
    assert staff_app.tabWidget.currentIndex() == 2
