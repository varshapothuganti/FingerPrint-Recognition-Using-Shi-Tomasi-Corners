#pip3 install scikit-image....Do not use skimage
import os
import cv2
import sys
import numpy
from match import *
from PyQt5 import QtWidgets, QtGui, QtCore
import matplotlib.pyplot as plt
#from enhance import image_enhance
#from PIL import ImageEnhance
from skimage.morphology import skeletonize, thin



class MyForm(QtWidgets.QMainWindow):
	def __init__(self,parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.main)
	def get_descriptors(self,img):
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		img = clahe.apply(img)
		corners = cv2.goodFeaturesToTrack(img,1000,0.01,10)
		corners = numpy.int0(corners)
		keypoints = []
		for i in corners:
			x,y = i.ravel()
			keypoints.append(cv2.KeyPoint(float(x) , float(y) , 1))
		# Define descriptor
		orb = cv2.ORB_create()
		# Compute descriptors
		_, des = orb.compute(img, keypoints)
		return (keypoints, des);
	def main(self):
		fname = str(self.ui.lineEdit_3.text())
		img1 = cv2.imread("C:\project code\imgbase/" + fname, cv2.IMREAD_GRAYSCALE)
		# find the keypoints and descriptors with ORB
		kp1, des1 =self.get_descriptors(img1)

		fname1 = str(self.ui.lineEdit_4.text())
		img2 = cv2.imread("C:\project code\imgbase/" + fname1, cv2.IMREAD_GRAYSCALE)
		# find the keypoints and descriptors with ORB
		kp2, des2 =self.get_descriptors(img2)
	
		
		# create BFMatcher object
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
		# Matching between the descriptors and Sort them in the order of their distance.
		matches = sorted(bf.match(des1, des2), key= lambda match:match.distance)

		# Plot the keypoints for imges syntax drawKeypoints(input_image, key_points, output_image, colour, flag)
		img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
		img5 = cv2.drawKeypoints(img2, kp2, outImage=None)
		#Horizontally stacked subplots
		f, axarr = plt.subplots(1,2)
		#displaying the image with keypoints as the output on the screen
		axarr[0].imshow(img4)
		axarr[1].imshow(img5)
		plt.show()

		# Draw matches
		img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
		plt.imshow(img3)
		plt.show()
	
		# Calculate score
		#print(matches)

		score = 0;
		for match in matches:
			score += match.distance
		#print(score)
		#print(len(matches),"matches")

		score_threshold = 50
		if score/len(matches) < score_threshold:
			print("Fingerprint matches.")
		else:
			print("Fingerprint does not match.")
  
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

