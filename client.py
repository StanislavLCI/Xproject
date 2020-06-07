import sys
import os
from PyQt5 import QtWidgets, QtCore
import LiginPanel
import time
import pickle
import socket
import win1
import core
from multiprocessing import Process

class ExampleApp(QtWidgets.QMainWindow, win1.Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.label_2.hide()
        self.label_3.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.pushButton.hide()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # скрываем окно Виндовс
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Скрываем задний план окна
        self.pushButton_2.clicked.connect(exit)
        self.pushButton_3.clicked.connect(self.test_connect)
        self.pushButton.clicked.connect(self.lite)
        self.test_connect()





    def test_connect(self):
        a = core.Sock.sock_conn_test(self)
        if a:
            self.label_2.show()
            self.label_3.show()
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.pushButton.show()
            self.label.hide()
            self.pushButton_3.hide()


    def lite(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            try:
                f = core.Sock.verefy_profile(self, self.lineEdit.text(), self.lineEdit_2.text())
                self.lineEdit.setPlaceholderText(f[0])
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                if f[1] == '1':
                    print('Клиент запущен')
                else:
                    print('Запусе клиента откланен')
            except:
                self.lineEdit.setPlaceholderText('сервер не отвечает...')
                self.lineEdit.clear()
                self.lineEdit_2.clear()
        else:
            self.lineEdit.setPlaceholderText('Введите данные...')




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
