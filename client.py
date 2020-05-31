import sys
import os
from PyQt5 import QtWidgets
import LiginPanel
import time
import pickle
import socket
import core
from multiprocessing import Process

class ExampleApp(QtWidgets.QMainWindow, LiginPanel.Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.label_2.hide()
        self.label_3.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.pushButton.hide()
        self.pushButton_2.clicked.connect(exit)
        self.pushButton_3.clicked.connect(self.test_connect)
        self.pushButton.clicked.connect(self.lite)
        self.test_connect()





    def test_connect(self):
        a = core.sock.sock_conn_test(self)
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
                f = core.sock.verefy_profile(self, self.lineEdit.text(), self.lineEdit_2.text())
                self.label_6.setText(f[0])
                if f[1] == '1':
                    print('Клиент запущен')
                else:
                    print('Запусе клиента откланен')
            except:
                self.label_6.setText('сервер не отвечает...')
        else:
            self.label_6.setText('В ведите данные...')




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
