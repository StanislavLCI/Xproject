import sys
import os
from PyQt5 import QtWidgets
import LiginPanel
import time
import pickle
import socket

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
        self.pushButton_3.clicked.connect(self.con)
        self.pushButton.clicked.connect(self.lite)
        if self.label != self.label.show():
            self.con()


    def con(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 1000))
            sock.close()
            if sock:
                self.label_2.show()
                self.label_3.show()
                self.lineEdit.show()
                self.lineEdit_2.show()
                self.pushButton.show()
                self.label.hide()
                self.pushButton_3.hide()
        except:
          pass


    def lite(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            lig = self.lineEdit.text()
            pas = self.lineEdit_2.text()
            ff = [lig, pas]
            dy = pickle.dumps(ff)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex(('localhost', 1000))
            sock.sendall(dy)
            data = sock.recv(10000)
            decode = data.decode('utf-8')
            sock.close()
            print(decode)
            if decode == '1':
                self.label_6.setText('логин и пароль верны')
            else:
                self.label_6.setText('неправельные данные')




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


