import sys
import os
from stfprints import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_4.clicked.connect(self.iver)
     self.ui.pushButton_5.clicked.connect(self.hcdet)
     self.ui.pushButton_6.clicked.connect(self.match)
     self.ui.pushButton_7.clicked.connect(self.separate)     


  def iver(self):
    os.system("python3 imagesv1.py")#images verification

  def hcdet(self):
    os.system("python3 samp3.py")#good look features

  def match(self):
    os.system("python3 match1.py")#image matching
	
  def separate(self):
    os.system("python3 sampdf1.py")#image separation from pdf
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
