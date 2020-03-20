from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


#Class Instantiation for Home Page Form
class Ui_homeForm(object):
    
    
    #File Directory for Design/Background Images etc/
    assets = pathlib.Path("Assets")
    
    
    #Function for Creating User Interface (HOME PAGE)
    def setupUi(self, homeForm):
        
        #Home Page Window/Frame
        homeForm.setObjectName("homeForm")
        homeForm.resize(793, 606)
        
        
        #Background  
        self.labelHomeBG = QtWidgets.QLabel(homeForm)
        self.labelHomeBG.setGeometry(QtCore.QRect(0, -20, 831, 741))
        self.labelHomeBG.setText("")
        self.labelHomeBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelHomeBG.setObjectName("labelHomeBG")
        
        
        
        #Black Container
        self.labelModal3 = QtWidgets.QLabel(homeForm)
        self.labelModal3.setGeometry(QtCore.QRect(20, 40, 741, 531))
        self.labelModal3.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal3.setText("")
        self.labelModal3.setObjectName("labelModal3")
        
        
        
        #Label for Home Page (Event Setter)
        self.labelEventSetter = QtWidgets.QLabel(homeForm)
        self.labelEventSetter.setGeometry(QtCore.QRect(300, 70, 321, 91))
        self.labelEventSetter.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelEventSetter.setObjectName("labelEventSetter")
        
        
        
        #Set Event Button. It includes the Dimension/Size/Design or Stylesheet
        self.setEventButton = QtWidgets.QPushButton(homeForm)
        self.setEventButton.setGeometry(QtCore.QRect(80, 240, 251, 61))
        self.setEventButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.setEventButton.setObjectName("setEventButton")
        
        
        #Logout Button. It includes the Dimension/Size/Design or Stylesheet
        self.logoutButton = QtWidgets.QPushButton(homeForm)
        self.logoutButton.setGeometry(QtCore.QRect(80, 410, 251, 61))
        self.logoutButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.logoutButton.setObjectName("logoutButton")
        
        
        #View Event Button. It includes the Dimension/Size/Design or Stylesheet
        self.viewEventButton = QtWidgets.QPushButton(homeForm)
        self.viewEventButton.setGeometry(QtCore.QRect(440, 240, 251, 61))
        self.viewEventButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.viewEventButton.setObjectName("viewEventButton")
        
        
        
        #About Us Button. It includes the Dimension/Size/Design or Stylesheet
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



    #Compilation of all objects in the Home.py or Home Page Window/Frame
    def retranslateUi(self, homeForm):
        
        _translate = QtCore.QCoreApplication.translate
        homeForm.setWindowTitle(_translate("homeForm", "Home Page"))
        self.labelEventSetter.setText(_translate("homeForm", "EVENT SETTER"))
        self.setEventButton.setText(_translate("homeForm", "PLAN EVENTS"))
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

