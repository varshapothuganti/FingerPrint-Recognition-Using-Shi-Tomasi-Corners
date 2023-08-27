import sys
import os 
from images import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.checkfile1)
     self.ui.pushButton_2.clicked.connect(self.checkfile2)
     self.ui.pushButton_3.clicked.connect(self.checkfile3)
     self.ui.pushButton_4.clicked.connect(self.checkfile4)
     self.ui.pushButton_5.clicked.connect(self.checkfile5)
     self.ui.pushButton_6.clicked.connect(self.checkfile6)
     self.ui.pushButton_7.clicked.connect(self.checkfile7)
     self.ui.pushButton_8.clicked.connect(self.checkfile8)
     self.ui.pushButton_9.clicked.connect(self.checkfile9)
     self.ui.pushButton_10.clicked.connect(self.checkfile10)	 

  def checkfile1(self):                
        fname = str(self.ui.lineEdit.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists') 
		  
  def checkfile2(self):                 
        fname = str(self.ui.lineEdit_2.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile3(self):                 
        fname = str(self.ui.lineEdit_3.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile4(self):                
        fname = str(self.ui.lineEdit_4.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile5(self):                 
        fname = str(self.ui.lineEdit_5.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile6(self):                 
        fname = str(self.ui.lineEdit_6.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile7(self):                 
        fname = str(self.ui.lineEdit_7.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile8(self):                 
        fname = str(self.ui.lineEdit_8.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile9(self):                 
        fname = str(self.ui.lineEdit_9.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
  def checkfile10(self):                 
        fname = str(self.ui.lineEdit_10.text())
        if (os.path.isfile(fname)):
          print(' file exists')
        else:
          print(' file does not exists')
		  
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

