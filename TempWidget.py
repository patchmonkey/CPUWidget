#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import QSizePolicy as qs

import wmi
import os

cellFormat = ("border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 0, 0,);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 14pt \"Arial\";\n"
"text-align: center;\n")



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
        self.temp_CPU.setText(str(getTemp(4)))
        self.temp_core1.setText(str(getTemp(0)))
        self.temp_core2.setText(str(getTemp(1)))
        self.temp_core3.setText(str(getTemp(2)))
        self.temp_core4.setText(str(getTemp(3)))
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

 
 
##    Main Window Flags **  
 
        self.resize(220, 220)
        self.setStyleSheet("background-color: rgb(0,0,0)\n")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(.75)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("Temp Gauge")

#Initializing the Columns
        self.col1 = QtGui.QWidget(self)
        self.col1.setObjectName("col1")
        self.col1.setGeometry(QtCore.QRect(5, 5, 50, 200)) 
        self.vbox1 = QtGui.QVBoxLayout(self.col1)
        self.vbox1.setMargin(0)
        self.vbox1.setGeometry(QtCore.QRect(10, 10, 30, 150))
 
        self.col2 = QtGui.QWidget(self)
        self.col2.setObjectName("col2")
        self.col2.setGeometry(QtCore.QRect(60, 5, 120, 200)) 
        self.vbox2 = QtGui.QVBoxLayout(self.col2)
        self.vbox2.setMargin(0)
        self.vbox2.setGeometry(QtCore.QRect(10, 10, 30, 150))
        
        self.col3 = QtGui.QWidget(self)
        self.col3.setObjectName("col3")
        self.col3.setGeometry(QtCore.QRect(185, 5, 30, 30))
        self.vbox3 = QtGui.QVBoxLayout(self.col3)
        self.vbox3.setMargin(0)
        self.vbox3.setGeometry(QtCore.QRect(185, 0, 30, 30))        
        
        
        self.closeButton = QtGui.QPushButton()
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setText("X")   
        self.closeButton.setFixedSize(QtCore.QSize(30,30))
        self.closeButton.setStyleSheet(cellFormat)
        
        
        
        
        self.lab_core3 = QtGui.QLabel(self.col2)
        self.lab_core3.setStyleSheet(cellFormat)
        self.lab_core3.setObjectName("lab_core3")
        self.lab_core3.setAlignment(QtCore.Qt.AlignCenter)
        
    
       
        self.lab_core4 = QtGui.QLabel(self.col2)
        self.lab_core4.setStyleSheet(cellFormat)
        self.lab_core4.setObjectName("lab_core4")
        self.lab_core4.setSizePolicy(qs.Ignored, qs.Ignored)
        self.lab_core4.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.lab_core1 = QtGui.QLabel(self.col2)
        self.lab_core1.setStyleSheet(cellFormat)
        self.lab_core1.setObjectName("lab_core1")
        self.lab_core1.setAlignment(QtCore.Qt.AlignCenter)
        
        self.lab_core2 = QtGui.QLabel(self.col2)
        self.lab_core2.setStyleSheet(cellFormat)
        self.lab_core2.setObjectName("lab_core2")
        self.lab_core2.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.lab_CPU = QtGui.QLabel(self.col2)
        self.lab_CPU.setStyleSheet(cellFormat)
        self.lab_CPU.setObjectName("lab_CPU")
        self.lab_CPU.setAlignment(QtCore.Qt.AlignCenter)




        self.temp_CPU = QtGui.QLabel(self.col1)
        self.temp_CPU.setStyleSheet(cellFormat)
        self.temp_CPU.setObjectName("temp_CPU")
        self.temp_CPU.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.temp_core1 = QtGui.QLabel(self.col1)
        self.temp_core1.setStyleSheet(cellFormat)
        self.temp_core1.setObjectName("temp_core1")
        self.temp_core1.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.temp_core2 = QtGui.QLabel(self.col1)
        self.temp_core2.setStyleSheet(cellFormat)
        self.temp_core2.setObjectName("temp_core2")
        self.temp_core2.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.temp_core3 = QtGui.QLabel(self.col1)
        self.temp_core3.setStyleSheet(cellFormat)
        self.temp_core3.setObjectName("temp_core3")
        self.temp_core3.setAlignment(QtCore.Qt.AlignCenter)
        
    
        self.temp_core4 = QtGui.QLabel(self.col1)
        self.temp_core4.setStyleSheet(cellFormat)
        self.temp_core4.setObjectName("temp_core4")
        self.temp_core4.setAlignment(QtCore.Qt.AlignCenter)
        
# Packing the widgets
        self.vbox1.addWidget(self.temp_CPU)
        self.vbox1.addWidget(self.temp_core1)
        self.vbox1.addWidget(self.temp_core2)
        self.vbox1.addWidget(self.temp_core3)
        self.vbox1.addWidget(self.temp_core4)
        
        
        self.vbox2.addWidget(self.lab_CPU)
        self.vbox2.addWidget(self.lab_core1)
        self.vbox2.addWidget(self.lab_core2)
        self.vbox2.addWidget(self.lab_core3)
        self.vbox2.addWidget(self.lab_core4)
        
        self.vbox3.addWidget(self.closeButton)
        
        
        
        
        self.lab_core3.setText("Core 3 Temp")
        self.lab_core4.setText("Core 4 Temp")
        self.lab_core1.setText("Core 1 Temp")
        self.lab_core2.setText("Core 2 Temp")
        self.lab_CPU.setText("CPU Temp")
        self.temp_CPU.setText(str(getTemp(4)))
        self.temp_core1.setText(str(getTemp(0)))
        self.temp_core2.setText(str(getTemp(1)))
        self.temp_core3.setText(str(getTemp(2)))
        self.temp_core4.setText(str(getTemp(3)))
        

        
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





