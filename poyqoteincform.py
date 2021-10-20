# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'poyqoteincform.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 545)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(39, 17, 481, 421))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.emp_name = QLabel(self.layoutWidget)
        self.emp_name.setObjectName(u"emp_name")

        self.gridLayout.addWidget(self.emp_name, 0, 0, 1, 1)

        self.emp_name_entry = QLineEdit(self.layoutWidget)
        self.emp_name_entry.setObjectName(u"emp_name_entry")

        self.gridLayout.addWidget(self.emp_name_entry, 0, 1, 2, 1)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 3, 1, 2, 1)

        self.position_list = QComboBox(self.layoutWidget)
        self.position_list.setObjectName(u"position_list")

        self.gridLayout.addWidget(self.position_list, 5, 1, 2, 1)

        self.salary = QDoubleSpinBox(self.layoutWidget)
        self.salary.setObjectName(u"salary")

        self.gridLayout.addWidget(self.salary, 7, 1, 1, 1)

        self.text_description = QTextBrowser(self.layoutWidget)
        self.text_description.setObjectName(u"text_description")

        self.gridLayout.addWidget(self.text_description, 8, 1, 1, 1)

        self.description = QLabel(self.layoutWidget)
        self.description.setObjectName(u"description")

        self.gridLayout.addWidget(self.description, 8, 0, 1, 1)

        self.ann_salary = QLabel(self.layoutWidget)
        self.ann_salary.setObjectName(u"ann_salary")

        self.gridLayout.addWidget(self.ann_salary, 7, 0, 1, 1)

        self.position = QLabel(self.layoutWidget)
        self.position.setObjectName(u"position")

        self.gridLayout.addWidget(self.position, 6, 0, 1, 1)

        self.depart = QLabel(self.layoutWidget)
        self.depart.setObjectName(u"depart")

        self.gridLayout.addWidget(self.depart, 4, 0, 1, 1)

        self.emp_daate = QLabel(self.layoutWidget)
        self.emp_daate.setObjectName(u"emp_daate")

        self.gridLayout.addWidget(self.emp_daate, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(380, 450, 176, 28))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 604, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.emp_name_entry, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.position_list)
        QWidget.setTabOrder(self.position_list, self.salary)
        QWidget.setTabOrder(self.salary, self.text_description)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Employment Record", None))
        self.emp_name.setText(QCoreApplication.translate("MainWindow", u"Employee name", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"Job description", None))
        self.ann_salary.setText(QCoreApplication.translate("MainWindow", u"Annual salary", None))
        self.position.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.depart.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.emp_daate.setText(QCoreApplication.translate("MainWindow", u"Employment date", None))
    # retranslateUi

