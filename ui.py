# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 601)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #3a3a3a;\n"
"    color: #fff;\n"
"    selection-background-color: #b78620;\n"
"    selection-color: #000;\n"
"\n"
"}\n"
"\n"
"QPushButton#stopButton\n"
"{\n"
"    color:rgb(237, 52, 53);\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-size : 11px;\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: rgb(183, 134, 32);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: rgb(183, 134, 32);\n"
"    height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));\n"
"    border-top: none;\n"
"    border-bottom: 1px solid #4f4f4f;\n"
"    border-left: 1px solid #4f4f4f;\n"
"    border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"    background-color: #2e2e2e;\n"
"    width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    padding: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"    \n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #666;\n"
"    border-bottom: none;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: red;\n"
"    border: 1px solid #666;\n"
"    top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    background-color: #0c0c0d;\n"
"    margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    border-radius : 2px;\n"
"    font-size : 20px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"    border-top-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(images/up2.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"    border-bottom-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(images/down.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"    padding: 4px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"    show-decoration-selected: 1;\n"
"    alternate-background-color: #3a3a3a;\n"
"    selection-color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid gray;\n"
"    padding-top : 5px;\n"
"    color: #fff;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #b78620;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"    border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"    background-color: #656565;\n"
"    color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: lightgray;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"    color: lightgray;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: lightgray;\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"    background-color: rgba(183,134,32,20%);  \n"
"    width: 9px; \n"
"    height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #131313;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"    width: 14px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"    background-color: #d89e25;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"    border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cycle_info = QtWidgets.QFrame(self.centralwidget)
        self.cycle_info.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.cycle_info.setObjectName("cycle_info")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.cycle_info)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.cycle_info2_label = QtWidgets.QLabel(self.cycle_info)
        self.cycle_info2_label.setStyleSheet("border-style : none;")
        self.cycle_info2_label.setObjectName("cycle_info2_label")
        self.gridLayout_9.addWidget(self.cycle_info2_label, 1, 0, 1, 1)
        self.cycle_info1_label = QtWidgets.QLabel(self.cycle_info)
        self.cycle_info1_label.setStyleSheet("border-style : none;")
        self.cycle_info1_label.setObjectName("cycle_info1_label")
        self.gridLayout_9.addWidget(self.cycle_info1_label, 0, 0, 1, 1)
        self.cycle_info3_label = QtWidgets.QLabel(self.cycle_info)
        self.cycle_info3_label.setStyleSheet("border-style : none;")
        self.cycle_info3_label.setObjectName("cycle_info3_label")
        self.gridLayout_9.addWidget(self.cycle_info3_label, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.cycle_info, 1, 1, 1, 1)
        self.mesh_parameters = QtWidgets.QFrame(self.centralwidget)
        self.mesh_parameters.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.mesh_parameters.setObjectName("mesh_parameters")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mesh_parameters)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.mesh_parameters)
        self.label.setIndent(-3)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.mesh_parameters)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_14.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.resistance_input = QtWidgets.QLineEdit(self.mesh_parameters)
        self.resistance_input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.resistance_input.setObjectName("resistance_input")
        self.gridLayout_4.addWidget(self.resistance_input, 1, 1, 1, 1)
        self.mesh_length_input = QtWidgets.QLineEdit(self.mesh_parameters)
        self.mesh_length_input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.mesh_length_input.setObjectName("mesh_length_input")
        self.gridLayout_4.addWidget(self.mesh_length_input, 3, 1, 1, 1)
        self.mesh_width_input = QtWidgets.QLineEdit(self.mesh_parameters)
        self.mesh_width_input.setMaximumSize(QtCore.QSize(75, 16777215))
        self.mesh_width_input.setObjectName("mesh_width_input")
        self.gridLayout_4.addWidget(self.mesh_width_input, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.mesh_parameters)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.mesh_parameters)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.mesh_parameters)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.mesh_parameters)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.mesh_parameters)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 2)
        self.gridLayout_2.addWidget(self.mesh_parameters, 0, 0, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.svg"))
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 2, 1, 1)
        self.set_parameters = QtWidgets.QFrame(self.centralwidget)
        self.set_parameters.setMaximumSize(QtCore.QSize(16777215, 300))
        self.set_parameters.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.set_parameters.setObjectName("set_parameters")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.set_parameters)
        self.gridLayout_5.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_24 = QtWidgets.QLabel(self.set_parameters)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_24.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.set_voltage1_label = QtWidgets.QLabel(self.set_parameters)
        self.set_voltage1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_voltage1_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_voltage1_label.setObjectName("set_voltage1_label")
        self.gridLayout_5.addWidget(self.set_voltage1_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_time3_label = QtWidgets.QLabel(self.set_parameters)
        self.set_time3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_time3_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_time3_label.setObjectName("set_time3_label")
        self.gridLayout_5.addWidget(self.set_time3_label, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_voltage3_label = QtWidgets.QLabel(self.set_parameters)
        self.set_voltage3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_voltage3_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_voltage3_label.setObjectName("set_voltage3_label")
        self.gridLayout_5.addWidget(self.set_voltage3_label, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_current1_label = QtWidgets.QLabel(self.set_parameters)
        self.set_current1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_current1_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_current1_label.setObjectName("set_current1_label")
        self.gridLayout_5.addWidget(self.set_current1_label, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_time2_label = QtWidgets.QLabel(self.set_parameters)
        self.set_time2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_time2_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_time2_label.setObjectName("set_time2_label")
        self.gridLayout_5.addWidget(self.set_time2_label, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_time1_label = QtWidgets.QLabel(self.set_parameters)
        self.set_time1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_time1_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_time1_label.setObjectName("set_time1_label")
        self.gridLayout_5.addWidget(self.set_time1_label, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_current3_label = QtWidgets.QLabel(self.set_parameters)
        self.set_current3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_current3_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_current3_label.setObjectName("set_current3_label")
        self.gridLayout_5.addWidget(self.set_current3_label, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_voltage2_label = QtWidgets.QLabel(self.set_parameters)
        self.set_voltage2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_voltage2_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_voltage2_label.setObjectName("set_voltage2_label")
        self.gridLayout_5.addWidget(self.set_voltage2_label, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.set_current2_label = QtWidgets.QLabel(self.set_parameters)
        self.set_current2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.set_current2_label.setStyleSheet("border-style : none;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.set_current2_label.setObjectName("set_current2_label")
        self.gridLayout_5.addWidget(self.set_current2_label, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_44 = QtWidgets.QLabel(self.set_parameters)
        self.label_44.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_44.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_44.setObjectName("label_44")
        self.gridLayout_5.addWidget(self.label_44, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_45 = QtWidgets.QLabel(self.set_parameters)
        self.label_45.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_45.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_45.setObjectName("label_45")
        self.gridLayout_5.addWidget(self.label_45, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_39 = QtWidgets.QLabel(self.set_parameters)
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_39.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_39.setObjectName("label_39")
        self.gridLayout_5.addWidget(self.label_39, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.run_cycle_button = QtWidgets.QPushButton(self.set_parameters)
        self.run_cycle_button.setMinimumSize(QtCore.QSize(92, 70))
        self.run_cycle_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.run_cycle_button.setObjectName("run_cycle_button")
        self.gridLayout_5.addWidget(self.run_cycle_button, 2, 3, 3, 1)
        self.gridLayout_2.addWidget(self.set_parameters, 2, 0, 1, 1)
        self.emergency = QtWidgets.QFrame(self.centralwidget)
        self.emergency.setObjectName("emergency")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.emergency)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.emergency_button = QtWidgets.QPushButton(self.emergency)
        self.emergency_button.setMinimumSize(QtCore.QSize(92, 75))
        self.emergency_button.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.emergency_button.setObjectName("emergency_button")
        self.gridLayout_6.addWidget(self.emergency_button, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.emergency)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_6.addWidget(self.progressBar, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.emergency, 0, 1, 1, 1)
        self.connections = QtWidgets.QFrame(self.centralwidget)
        self.connections.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.connections.setObjectName("connections")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.connections)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.plc_connection_button = QtWidgets.QPushButton(self.connections)
        self.plc_connection_button.setMinimumSize(QtCore.QSize(92, 40))
        self.plc_connection_button.setObjectName("plc_connection_button")
        self.gridLayout_10.addWidget(self.plc_connection_button, 2, 0, 1, 1)
        self.power_supply_connection_button = QtWidgets.QPushButton(self.connections)
        self.power_supply_connection_button.setMinimumSize(QtCore.QSize(92, 40))
        self.power_supply_connection_button.setObjectName("power_supply_connection_button")
        self.gridLayout_10.addWidget(self.power_supply_connection_button, 1, 0, 1, 1)
        self.simulation_mode_button = QtWidgets.QPushButton(self.connections)
        self.simulation_mode_button.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.simulation_mode_button.setObjectName("simulation_mode_button")
        self.gridLayout_10.addWidget(self.simulation_mode_button, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.connections, 1, 2, 1, 1)
        self.temp_measurements = QtWidgets.QFrame(self.centralwidget)
        self.temp_measurements.setMaximumSize(QtCore.QSize(16777215, 300))
        self.temp_measurements.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.temp_measurements.setObjectName("temp_measurements")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.temp_measurements)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_38 = QtWidgets.QLabel(self.temp_measurements)
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_38.setStyleSheet("border-style : none; color : rgb(30, 146, 202)")
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.tc7_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc7_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc7_label.setStyleSheet("border-style : none;")
        self.tc7_label.setObjectName("tc7_label")
        self.gridLayout_8.addWidget(self.tc7_label, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc2_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc2_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc2_label.setStyleSheet("border-style : none;")
        self.tc2_label.setObjectName("tc2_label")
        self.gridLayout_8.addWidget(self.tc2_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc6_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc6_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc6_label.setStyleSheet("border-style : none;")
        self.tc6_label.setObjectName("tc6_label")
        self.gridLayout_8.addWidget(self.tc6_label, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc4_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc4_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc4_label.setStyleSheet("border-style : none;")
        self.tc4_label.setObjectName("tc4_label")
        self.gridLayout_8.addWidget(self.tc4_label, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc3_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc3_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc3_label.setStyleSheet("border-style : none;")
        self.tc3_label.setObjectName("tc3_label")
        self.gridLayout_8.addWidget(self.tc3_label, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc9_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc9_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc9_label.setStyleSheet("border-style : none;")
        self.tc9_label.setObjectName("tc9_label")
        self.gridLayout_8.addWidget(self.tc9_label, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc10_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc10_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc10_label.setStyleSheet("border-style : none;")
        self.tc10_label.setObjectName("tc10_label")
        self.gridLayout_8.addWidget(self.tc10_label, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc8_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc8_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc8_label.setStyleSheet("border-style : none;")
        self.tc8_label.setObjectName("tc8_label")
        self.gridLayout_8.addWidget(self.tc8_label, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.stop_temperatures_button = QtWidgets.QPushButton(self.temp_measurements)
        self.stop_temperatures_button.setMinimumSize(QtCore.QSize(92, 30))
        self.stop_temperatures_button.setObjectName("stop_temperatures_button")
        self.gridLayout_8.addWidget(self.stop_temperatures_button, 6, 1, 1, 1)
        self.tc1_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc1_label.setStyleSheet("border-style : none;")
        self.tc1_label.setObjectName("tc1_label")
        self.gridLayout_8.addWidget(self.tc1_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tc5_label = QtWidgets.QLabel(self.temp_measurements)
        self.tc5_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tc5_label.setStyleSheet("border-style : none;")
        self.tc5_label.setObjectName("tc5_label")
        self.gridLayout_8.addWidget(self.tc5_label, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.measure_temperatures_button = QtWidgets.QPushButton(self.temp_measurements)
        self.measure_temperatures_button.setMinimumSize(QtCore.QSize(92, 30))
        self.measure_temperatures_button.setObjectName("measure_temperatures_button")
        self.gridLayout_8.addWidget(self.measure_temperatures_button, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.temp_measurements, 2, 1, 1, 1)
        self.part_parameters = QtWidgets.QFrame(self.centralwidget)
        self.part_parameters.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.part_parameters.setObjectName("part_parameters")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.part_parameters)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.part_parameters)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.part_parameters)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_13.setStyleSheet("border-style : none; color : rgb(30, 146, 202);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 7, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.part_parameters)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.part_parameters)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 2, 1, 1)
        self.current2_input = QtWidgets.QLineEdit(self.part_parameters)
        self.current2_input.setObjectName("current2_input")
        self.gridLayout_3.addWidget(self.current2_input, 2, 3, 1, 1)
        self.current1_input = QtWidgets.QLineEdit(self.part_parameters)
        self.current1_input.setObjectName("current1_input")
        self.gridLayout_3.addWidget(self.current1_input, 2, 1, 1, 1)
        self.current3_input = QtWidgets.QLineEdit(self.part_parameters)
        self.current3_input.setObjectName("current3_input")
        self.gridLayout_3.addWidget(self.current3_input, 2, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.part_parameters)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.part_parameters)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.time2_input = QtWidgets.QLineEdit(self.part_parameters)
        self.time2_input.setObjectName("time2_input")
        self.gridLayout_3.addWidget(self.time2_input, 3, 3, 1, 1)
        self.voltage1_input = QtWidgets.QLineEdit(self.part_parameters)
        self.voltage1_input.setObjectName("voltage1_input")
        self.gridLayout_3.addWidget(self.voltage1_input, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.part_parameters)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.part_parameters)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 4, 1, 1)
        self.voltage2_input = QtWidgets.QLineEdit(self.part_parameters)
        self.voltage2_input.setObjectName("voltage2_input")
        self.gridLayout_3.addWidget(self.voltage2_input, 1, 3, 1, 1)
        self.set_parameters_button = QtWidgets.QPushButton(self.part_parameters)
        self.set_parameters_button.setMinimumSize(QtCore.QSize(92, 30))
        self.set_parameters_button.setObjectName("set_parameters_button")
        self.gridLayout_3.addWidget(self.set_parameters_button, 4, 2, 1, 2)
        self.time1_input = QtWidgets.QLineEdit(self.part_parameters)
        self.time1_input.setObjectName("time1_input")
        self.gridLayout_3.addWidget(self.time1_input, 3, 1, 1, 1)
        self.time3_input = QtWidgets.QLineEdit(self.part_parameters)
        self.time3_input.setObjectName("time3_input")
        self.gridLayout_3.addWidget(self.time3_input, 3, 5, 1, 1)
        self.voltage3_input = QtWidgets.QLineEdit(self.part_parameters)
        self.voltage3_input.setObjectName("voltage3_input")
        self.gridLayout_3.addWidget(self.voltage3_input, 1, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.part_parameters)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.part_parameters)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.part_parameters, 1, 0, 1, 1)
        self.old_cycles = QtWidgets.QWidget(self.centralwidget)
        self.old_cycles.setMaximumSize(QtCore.QSize(16777215, 300))
        self.old_cycles.setStyleSheet("border-width: 1; border-radius: 1;border-style: solid;border-color: rgb(100,100,100)")
        self.old_cycles.setObjectName("old_cycles")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.old_cycles)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_15 = QtWidgets.QLabel(self.old_cycles)
        self.label_15.setMinimumSize(QtCore.QSize(0, 20))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_15.setStyleSheet("border-style : none; color : rgb(30, 146, 202)")
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.old_cycles)
        self.pushButton_4.setMinimumSize(QtCore.QSize(92, 10))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_7.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.old_cycles)
        self.pushButton_6.setMinimumSize(QtCore.QSize(92, 10))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_7.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.old_cycles)
        self.pushButton_3.setMinimumSize(QtCore.QSize(92, 10))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.old_cycles)
        self.pushButton_7.setMinimumSize(QtCore.QSize(92, 10))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_7.addWidget(self.pushButton_7, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.old_cycles)
        self.pushButton_2.setMinimumSize(QtCore.QSize(92, 10))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.old_cycles, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resistance Welding"))
        self.cycle_info2_label.setText(_translate("MainWindow", "Cycle Information"))
        self.cycle_info1_label.setText(_translate("MainWindow", "Cycle Information"))
        self.cycle_info3_label.setText(_translate("MainWindow", "Cycle Information"))
        self.label.setText(_translate("MainWindow", "Resistance :"))
        self.label_14.setText(_translate("MainWindow", "MESH PARAMETERS"))
        self.label_3.setText(_translate("MainWindow", "Mesh length :"))
        self.label_2.setText(_translate("MainWindow", "Mesh width :"))
        self.label_18.setText(_translate("MainWindow", "SOIR NUMBER :"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE RESISTANCE"))
        self.label_24.setText(_translate("MainWindow", "SET PARAMETERS"))
        self.set_voltage1_label.setText(_translate("MainWindow", "0 Volt"))
        self.set_time3_label.setText(_translate("MainWindow", "0 second"))
        self.set_voltage3_label.setText(_translate("MainWindow", "0 Volt"))
        self.set_current1_label.setText(_translate("MainWindow", "0 amper"))
        self.set_time2_label.setText(_translate("MainWindow", "0 second"))
        self.set_time1_label.setText(_translate("MainWindow", "0 second"))
        self.set_current3_label.setText(_translate("MainWindow", "0 amper"))
        self.set_voltage2_label.setText(_translate("MainWindow", "0 Volt"))
        self.set_current2_label.setText(_translate("MainWindow", "0 amper"))
        self.label_44.setText(_translate("MainWindow", "MELTSTEP"))
        self.label_45.setText(_translate("MainWindow", "DWELL STEP"))
        self.label_39.setText(_translate("MainWindow", "RAISE STEP"))
        self.run_cycle_button.setText(_translate("MainWindow", "RUN CYCLE"))
        self.emergency_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">EMERGENCY \\n STOP</span></p></body></html>"))
        self.emergency_button.setText(_translate("MainWindow", "EMERGENCY \n"
" STOP"))
        self.plc_connection_button.setText(_translate("MainWindow", "CONNECT TO PLC"))
        self.power_supply_connection_button.setText(_translate("MainWindow", "CONNECT TO POWER SUPPLY"))
        self.simulation_mode_button.setText(_translate("MainWindow", "SIMULATION MODE"))
        self.label_38.setText(_translate("MainWindow", "TEMPERATURE MEASUREMENTS"))
        self.tc7_label.setText(_translate("MainWindow", "TC7"))
        self.tc2_label.setText(_translate("MainWindow", "TC2"))
        self.tc6_label.setText(_translate("MainWindow", "TC6"))
        self.tc4_label.setText(_translate("MainWindow", "TC4"))
        self.tc3_label.setText(_translate("MainWindow", "TC3"))
        self.tc9_label.setText(_translate("MainWindow", "TC9"))
        self.tc10_label.setText(_translate("MainWindow", "TC10"))
        self.tc8_label.setText(_translate("MainWindow", "TC8"))
        self.stop_temperatures_button.setText(_translate("MainWindow", "STOP \n"
" MEASURING"))
        self.tc1_label.setText(_translate("MainWindow", "TC1"))
        self.tc5_label.setText(_translate("MainWindow", "TC5"))
        self.measure_temperatures_button.setText(_translate("MainWindow", "MEASURE \n"
" TEMPERATURES"))
        self.label_10.setText(_translate("MainWindow", "Voltage(dwell) volts :"))
        self.label_13.setText(_translate("MainWindow", "PART PARAMETERS"))
        self.label_4.setText(_translate("MainWindow", "Voltage(raise) volts :"))
        self.label_9.setText(_translate("MainWindow", "Time(melt) seconds :"))
        self.label_11.setText(_translate("MainWindow", "Current(dwell) ampers :"))
        self.label_5.setText(_translate("MainWindow", "Current(raise) ampers :"))
        self.label_6.setText(_translate("MainWindow", "Time(raise) seconds :"))
        self.label_12.setText(_translate("MainWindow", "Time(dwell) seconds :"))
        self.set_parameters_button.setText(_translate("MainWindow", "SET PARAMETERS"))
        self.label_8.setText(_translate("MainWindow", "Current(melt) ampers :"))
        self.label_7.setText(_translate("MainWindow", "Voltage(melt) volts :"))
        self.label_15.setText(_translate("MainWindow", "OLD CYCLES"))
        self.pushButton_4.setText(_translate("MainWindow", "old_cycle3"))
        self.pushButton_6.setText(_translate("MainWindow", "old_cycle4"))
        self.pushButton_3.setText(_translate("MainWindow", "old_cycle2"))
        self.pushButton_7.setText(_translate("MainWindow", "old_cycle5"))
        self.pushButton_2.setText(_translate("MainWindow", "old_cycle1"))

