#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
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

        self.resize(179, 171)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.closeButton = QtGui.QPushButton()
        self.closeButton.setGeometry(QtCore.QRect(160, 10, 21, 20))
        self.closeButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);\n"
"color: rgb(244, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.closeButton.setObjectName("closeButton")
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(QtCore.QRect(60, 10, 101, 151))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lab_core3 = QtGui.QLabel(self.widget)
        self.lab_core3.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core3.setObjectName("lab_core3")
        self.gridLayout_2.addWidget(self.lab_core3, 5, 0, 1, 1)
        self.lab_core4 = QtGui.QLabel(self.widget)
        self.lab_core4.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core4.setObjectName("lab_core4")
        self.gridLayout_2.addWidget(self.lab_core4, 6, 0, 1, 1)
        self.lab_core1 = QtGui.QLabel(self.widget)
        self.lab_core1.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core1.setObjectName("lab_core1")
        self.gridLayout_2.addWidget(self.lab_core1, 2, 0, 1, 1)
        self.lab_core2 = QtGui.QLabel(self.widget)
        self.lab_core2.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_core2.setObjectName("lab_core2")
        self.gridLayout_2.addWidget(self.lab_core2, 4, 0, 1, 1)
        self.lab_CPU = QtGui.QLabel(self.widget)
        self.lab_CPU.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(0, 255, 0, 150);\n"
"font: 87 9pt \"Arial Black\";")
        self.lab_CPU.setObjectName("lab_CPU")
        self.gridLayout_2.addWidget(self.lab_CPU, 1, 0, 1, 1)
        self.widget1 = QtGui.QWidget()
        self.widget1.setGeometry(QtCore.QRect(10, 10, 48, 151))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.temp_CPU = QtGui.QLabel(self.widget1)
        self.temp_CPU.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_CPU.setObjectName("temp_CPU")
        self.gridLayout.addWidget(self.temp_CPU, 0, 0, 1, 1)
        self.temp_core1 = QtGui.QLabel(self.widget1)
        self.temp_core1.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core1.setObjectName("temp_core1")
        self.gridLayout.addWidget(self.temp_core1, 1, 0, 1, 1)
        self.temp_core2 = QtGui.QLabel(self.widget1)
        self.temp_core2.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core2.setObjectName("temp_core2")
        self.gridLayout.addWidget(self.temp_core2, 2, 0, 1, 1)
        self.temp_core3 = QtGui.QLabel(self.widget1)
        self.temp_core3.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
"border-color: rgba(0, 0, 127, 200);\n"
"color: rgba(255, 0, 0, 150);\n"
"font: 75 14pt \"Arial\";\n"
"")
        self.temp_core3.setObjectName("temp_core3")
        self.gridLayout.addWidget(self.temp_core3, 3, 0, 1, 1)
        self.temp_core4 = QtGui.QLabel(self.widget1)
        self.temp_core4.setStyleSheet("background-color: rgba(0, 0, 0,200);\n"
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
        self.temp_CPU.setText("<html><head/><body><p align=\"center\">4</p></body></html>")
        self.temp_core1.setText("<html><head/><body><p align=\"center\">0</p></body></html>")
        self.temp_core2.setText("<html><head/><body><p align=\"center\">1</p></body></html>")
        self.temp_core3.setText("<html><head/><body><p align=\"center\">2</p></body></html>")
        self.temp_core4.setText("<html><head/><body><p align=\"center\">3</p></body></html>")
		











##        self.setGeometry(2000, 100, 250, 150)
##        self.setWindowTitle('Event handler')
##        self.closeButton = QtGui.QPushButton(self)
##        self.closeButton.setText("X")
##        self.closeButton.setGeometry(QtCore.QRect(190, 90, 25, 19))
##        self.label = QtGui.QLabel(self)
##        self.label.setText(str(getTemp(4)))
##        self.label.setGeometry(30,30,30,30)







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
