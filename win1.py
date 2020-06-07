# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LiginPanel2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 300)
        MainWindow.setMinimumSize(QtCore.QSize(750, 300))
        MainWindow.setMaximumSize(QtCore.QSize(750, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(294, 18, 431, 261))
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listView.setMouseTracking(False)
        self.listView.setTabletTracking(False)
        self.listView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("QListView{\n"
"background:rgba(30,30,30,0.9);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"}")
        self.listView.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(333, 230, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background:rgba(240,240,240,0.2);\n"
"color:white;\n"
"border-radius: 9px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background:rgba(180,80,0,0.4);\n"
"color:white;\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(334, 88, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:transparent;\n"
"border:none;\n"
"color:rgba(240,240,240,1);\n"
"border-bottom: 1px solid #717072;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(334, 168, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background:transparent;\n"
"border:none;\n"
"color:rgba(240,240,240,1);\n"
"border-bottom: 1px solid #717072;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(336, 68, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(334, 148, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(695, 29, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"color:white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#f75e25;\n"
"background:transparent;;\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(127, 120, 61, 50))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:transparent;\n"
"color:white;\n"
"border-bottom: 1px solid white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(129, 172, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 118, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 168, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"color:white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#f75e25;\n"
"background:transparent;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 230, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(13, 18, 281, 261))
        self.listView_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listView_2.setMouseTracking(False)
        self.listView_2.setTabletTracking(False)
        self.listView_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listView_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listView_2.setAutoFillBackground(False)
        self.listView_2.setStyleSheet("QListView{\n"
"background:rgb(180, 70, 0)    ;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}")
        self.listView_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listView_2.setObjectName("listView_2")
        self.listView.raise_()
        self.listView_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Launcher"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.label_2.setText(_translate("MainWindow", "LOGIN."))
        self.label_3.setText(_translate("MainWindow", "PASSWORD."))
        self.pushButton_2.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "YS"))
        self.label_5.setText(_translate("MainWindow", "GROUP"))
        self.label.setText(_translate("MainWindow", "Connecting Server..."))
        self.pushButton_3.setText(_translate("MainWindow", "UPDATE"))
