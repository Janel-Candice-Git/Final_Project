# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeForm(object):
    def setupUi(self, homeForm):
        homeForm.setObjectName("homeForm")
        homeForm.setEnabled(True)
        homeForm.resize(787, 584)
        self.labelHomeBG = QtWidgets.QLabel(homeForm)
        self.labelHomeBG.setGeometry(QtCore.QRect(0, -20, 831, 741))
        self.labelHomeBG.setText("")
        self.labelHomeBG.setPixmap(QtGui.QPixmap("../Assets/label_bg.jpg"))
        self.labelHomeBG.setObjectName("labelHomeBG")
        self.labelModal3 = QtWidgets.QLabel(homeForm)
        self.labelModal3.setGeometry(QtCore.QRect(20, 40, 741, 531))
        self.labelModal3.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal3.setText("")
        self.labelModal3.setObjectName("labelModal3")
        self.labelEventSetter = QtWidgets.QLabel(homeForm)
        self.labelEventSetter.setGeometry(QtCore.QRect(300, 70, 321, 91))
        self.labelEventSetter.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelEventSetter.setObjectName("labelEventSetter")
        self.setEventButton = QtWidgets.QPushButton(homeForm)
        self.setEventButton.setGeometry(QtCore.QRect(80, 240, 251, 61))
        self.setEventButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.setEventButton.setObjectName("setEventButton")
        self.logoutButton = QtWidgets.QPushButton(homeForm)
        self.logoutButton.setGeometry(QtCore.QRect(80, 410, 251, 61))
        self.logoutButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.logoutButton.setObjectName("logoutButton")
        self.viewEventButton = QtWidgets.QPushButton(homeForm)
        self.viewEventButton.setGeometry(QtCore.QRect(440, 240, 251, 61))
        self.viewEventButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.viewEventButton.setObjectName("viewEventButton")
        self.aboutUsButton = QtWidgets.QPushButton(homeForm)
        self.aboutUsButton.setGeometry(QtCore.QRect(450, 410, 251, 61))
        self.aboutUsButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.aboutUsButton.setObjectName("aboutUsButton")
        self.checkLesson = QtWidgets.QPushButton(homeForm)
        self.checkLesson.setGeometry(QtCore.QRect(260, 320, 251, 61))
        self.checkLesson.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.checkLesson.setObjectName("checkLesson")

        self.retranslateUi(homeForm)
        QtCore.QMetaObject.connectSlotsByName(homeForm)

    def retranslateUi(self, homeForm):
        _translate = QtCore.QCoreApplication.translate
        homeForm.setWindowTitle(_translate("homeForm", "Home Page"))
        self.labelEventSetter.setText(_translate("homeForm", "EVENT SETTER"))
        self.setEventButton.setText(_translate("homeForm", "SET EVENTS"))
        self.logoutButton.setText(_translate("homeForm", "LOGOUT"))
        self.viewEventButton.setText(_translate("homeForm", "VIEW EVENTS"))
        self.aboutUsButton.setText(_translate("homeForm", "ABOUT US"))
        self.checkLesson.setText(_translate("homeForm", "CHECK LESSONS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeForm = QtWidgets.QWidget()
    ui = Ui_homeForm()
    ui.setupUi(homeForm)
    homeForm.show()
    sys.exit(app.exec_())

