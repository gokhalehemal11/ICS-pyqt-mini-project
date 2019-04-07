# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ics.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pycipher import ADFGVX


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):


	def __init__(self):
		self.secret_key= "secretkey"
		self.msg1=""
		self.msg2=""

	def send_msg1(self):

		self.msg1= self.textEdit.toPlainText()
		adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword=str(self.secret_key))
		cur= adfgvx.encipher(str(self.msg1))
		print("A says: ", cur)
		self.textEdit_3.append('A says: '+ adfgvx.decipher(cur))
		self.textEdit.clear()


	def send_msg2(self):

		self.msg2= self.textEdit_2.toPlainText()
		adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword=str(self.secret_key))
		cur= adfgvx.encipher(str(self.msg2))
		print("B says: ", cur)
		self.textEdit_3.append('B says: '+ adfgvx.decipher(cur))
		self.textEdit_2.clear()


	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.setFixedSize(659, 473)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.textEdit = QtGui.QTextEdit(self.centralwidget)
		self.textEdit.setGeometry(QtCore.QRect(60, 180, 231, 30))
		self.textEdit.setObjectName(_fromUtf8("textEdit"))
		self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
		self.textEdit_2.setGeometry(QtCore.QRect(390, 180, 231, 30))
		self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
		self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
		self.textEdit_3.setGeometry(QtCore.QRect(230, 50, 231, 100))
		self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(120, 210, 97, 27))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(450, 210, 97, 27))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.lineEdit = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(260, 280, 121, 27))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(290, 310, 61, 27))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(220, 350, 220, 27))
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(280, 20, 250, 10))
		self.label_2.setObjectName(_fromUtf8("label_2"))

		MainWindow.setCentralWidget(self.centralwidget)




		self.pushButton.clicked.connect(self.send_msg1)
		self.pushButton_2.clicked.connect(self.send_msg2)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.pushButton.setText(_translate("MainWindow", "Send Msg", None))
		self.pushButton_2.setText(_translate("MainWindow", "Send Msg", None))
		self.pushButton_3.setText(_translate("MainWindow", "Set Key", None))
		self.label.setText(_translate("MainWindow", "Default Secret Key is :"+ self.secret_key, None))
		self.label_2.setText(_translate("MainWindow", "Chat Shown Here ", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

