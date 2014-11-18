#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QSizePolicy as qs

import wmi
import os

def getTemp(coreNum):  
    ns = "root\\openhardwaremonitor"
    temp = u"/intelcpu/0/temperature/" + str(coreNum)
    try:
        return int(wmi.WMI(namespace=ns).Sensor(Identifier=temp)[0].value)
    except IndexError:
        print("Value not found. Please make sure Open Hardware Monitor is running.")
        return "error!"


class Example(QtGui.QWidget):

    @QtCore.pyqtSlot() # This is how you set up a custom slot!!!
    def updateTick(self):
        self.temp_CPU.setText("<html><head/><body><p align=\"center\">" + str(getTemp(4)) + "</p></body></html>")
        self.temp_core1.setText("<html><head/><body><p align=\"center\">" + str(getTemp(0)) + "</p></body></html>")
        self.temp_core2.setText("<html><head/><body><p align=\"center\">" + str(getTemp(1)) + "</p></body></html>")
        self.temp_core3.setText("<html><head/><body><p align=\"center\">" + str(getTemp(2)) + "</p></body></html>")
        self.temp_core4.setText("<html><head/><body><p align=\"center\">" + str(getTemp(3)) + "</p></body></html>")
        print "Updating..."
        

###################################################################################



#   The block below moves the window from anywhere without the title bar   #

    dragPosition = 0
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.dragPosition = e.globalPos() - self.frameGeometry().topLeft()
            e.accept()
    def mouseMoveEvent(self, e):
        if e.buttons() and QtCore.Qt.LeftButton:
            self.move(e.globalPos() - self.dragPosition)
            e.accept()

#   The block below closes the window on an escape press             #
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

 
##################################################################################
    def __init__(self):
        super(Example, self).__init__()    #need this to init the parent classd

        self.resize(400, 200)
        self.setStyleSheet("background-color: rgb(0,0,0)\n")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(.75)
        self.closeButton = QtGui.QPushButton()
        self.closeButton.setText("x")
        self.closeButton.setGeometry(QtCore.QRect(180, 20, 20, 20))
        self.closeButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.closeButton.setObjectName("closeButton")

        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setMargin(30)

        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setGeometry(QtCore.QRect(0, 10, 101, 151))  ######
##        self.gridLayout.setColumnMinimumWidth (0, 40)
##        self.gridLayout.setColumnMinimumWidth (1, 100)

        self.lab_core3 = QtGui.QLabel()
        self.lab_core3.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 255);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core3.setObjectName("lab_core3")
        #self.lab_core3.setFixedWidth(100)
        self.gridLayout.addWidget(self.lab_core3, 3, 1, 1, 1)
        
        self.lab_core4 = QtGui.QLabel()
        #self.lab_core4.setFixedWidth(100)
        self.lab_core4.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);"
"font: 87 9pt \"Arial Black\";")
        self.lab_core4.setObjectName("lab_core4")
        self.lab_core4.setSizePolicy(qs.Ignored, qs.Ignored)
        self.gridLayout.addWidget(self.lab_core4, 4, 1, 1, 1)
        self.lab_core1 = QtGui.QLabel()
        #self.lab_core1.setFixedWidth(100)
        self.lab_core1.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core1.setObjectName("lab_core1")
        self.gridLayout.addWidget(self.lab_core1, 1, 1, 1, 1)
        self.lab_core2 = QtGui.QLabel()
        #self.lab_core2.setFixedWidth(100)
        self.lab_core2.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core2.setObjectName("lab_core2")
        self.gridLayout.addWidget(self.lab_core2, 2, 1, 1, 1)
        self.lab_CPU = QtGui.QLabel()
        #self.lab_CPU.setFixedWidth(100)
        self.lab_CPU.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"        
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_CPU.setObjectName("lab_CPU")
        self.gridLayout.addWidget(self.lab_CPU, 0, 1, 1, 1)

        self.temp_CPU = QtGui.QLabel()
        #self.temp_CPU.setFixedWidth(40)
        self.temp_CPU.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_CPU.setObjectName("temp_CPU")
        self.gridLayout.addWidget(self.temp_CPU, 0, 0, 1, 1)
        self.temp_core1 = QtGui.QLabel()
        self.temp_core1.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core1.setObjectName("temp_core1")
        #self.temp_core1.setFixedWidth(40)
        
        self.gridLayout.addWidget(self.temp_core1, 1, 0, 1, 1)
        self.temp_core2 = QtGui.QLabel()
        self.temp_core2.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core2.setObjectName("temp_core2")
        self.gridLayout.addWidget(self.temp_core2, 2, 0, 1, 1)
        self.temp_core3 = QtGui.QLabel()
        #self.temp_core1.setFixedWidth(40)
        self.temp_core3.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core3.setObjectName("temp_core3")
        self.gridLayout.addWidget(self.temp_core3, 3, 0, 1, 1)
        self.temp_core4 = QtGui.QLabel()
        #self.temp_core1.setFixedWidth(40)
        self.temp_core4.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core4.setObjectName("temp_core4")
        self.gridLayout.addWidget(self.temp_core4, 4, 0, 1, 1)
        self.setWindowTitle("Temp Gauge")
				
        self.closeButton.setText("x")
        self.lab_core3.setText("Core 3 Temp")
        self.lab_core4.setText("Core 4 Temp")
        self.lab_core1.setText("Core 1 Temp")
        self.lab_core2.setText("Core 2 Temp")
        self.lab_CPU.setText("CPU Temp")
        self.temp_CPU.setText("<html><head/><body><p align=\"center\">" + str(getTemp(4)) + "</p></body></html>")
        self.temp_core1.setText("<html><head/><body><p align=\"center\">" + str(getTemp(0)) + "</p></body></html>")
        self.temp_core2.setText("<html><head/><body><p align=\"center\">" + str(getTemp(1)) + "</p></body></html>")
        self.temp_core3.setText("<html><head/><body><p align=\"center\">" + str(getTemp(2)) + "</p></body></html>")
        self.temp_core4.setText("<html><head/><body><p align=\"center\">" + str(getTemp(3)) + "</p></body></html>")
		

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()







def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    #setting up a timer
    timer = QtCore.QTimer()

    #connecting the signal (timer's timeout) to the slot (updateTick())
    ex.connect(timer, QtCore.SIGNAL("timeout()"), QtCore.SLOT("updateTick()"))
    ex.connect(ex.closeButton, QtCore.SIGNAL("clicked()"), ex.close)

    timer.start(1000)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  





############### Old Code ##################
#self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #this hides the frame
#QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), )
#QtCore.QMetaObject.connectSlotsByName(self)
##        self.setGeometry(2000, 100, 250, 150)
##        self.setWindowTitle('Event handler')
##        self.closeButton = QtGui.QPushButton(self)
##        self.closeButton.setText("X")
##        self.closeButton.setGeometry(QtCore.QRect(190, 90, 25, 19))
##        self.label = QtGui.QLabel(self)
##        self.label.setText(str(getTemp(4)))
##        self.label.setGeometry(30,30,30,30)


        #self.widget1 = QtGui.QWidget()
        #self.widget1.setObjectName("widget1")
        #self.gridLayout = QtGui.QGridLayout(self)
        #self.gridLayout.setGeometry(QtCore.QRect(10, 10, 48, 151))
        #self.gridLayout.setMargin(0)
       # self.gridLayout.setObjectName("gridLayout")
