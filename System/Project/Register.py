from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


#Class instantiation for Registration Form
class Ui_registerForm(object):
    
    
     #Path directory for the Assets/Design Images 
    assets = pathlib.Path("Assets")
    
    
    #Function for creating User Interfaces (REGISTRATION)
    def setupUi(self, registerForm):
        
        
        #Registration Widgqt/Geometry or Dimension 
        registerForm.setObjectName("registerForm")
        registerForm.resize(631, 657)
        
        
        #Background for Registration (Light Blue Color)
        self.labelRegistrationBG = QtWidgets.QLabel(registerForm)
        self.labelRegistrationBG.setGeometry(QtCore.QRect(0, -20, 641, 741))
        self.labelRegistrationBG.setText("")
        self.labelRegistrationBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelRegistrationBG.setObjectName("labelRegistrationBG")
        
        #Modal (Black Container)
        self.labelModal2 = QtWidgets.QLabel(registerForm)
        self.labelModal2.setGeometry(QtCore.QRect(40, 20, 541, 611))
        self.labelModal2.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal2.setText("")
        self.labelModal2.setObjectName("labelModal2")
        
        
        #Label (Register Here)
        self.labelRegisterHere = QtWidgets.QLabel(registerForm)
        self.labelRegisterHere.setGeometry(QtCore.QRect(200, 20, 321, 91))
        self.labelRegisterHere.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelRegisterHere.setObjectName("labelRegisterHere")
        
        
        #Line Edit / Text Field for the Name
        self.lineEditName = QtWidgets.QLineEdit(registerForm)
        self.lineEditName.setGeometry(QtCore.QRect(120, 140, 381, 41))
        self.lineEditName.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditName.setObjectName("lineEditName")


        #Line Edit / Text Field for the Username
        self.lineEditUsername2 = QtWidgets.QLineEdit(registerForm)
        self.lineEditUsername2.setGeometry(QtCore.QRect(120, 230, 381, 41))
        self.lineEditUsername2.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditUsername2.setObjectName("lineEditUsername2")


        #Line Edit / Text Field for the Password
        self.lineEditPassword2 = QtWidgets.QLineEdit(registerForm)
        self.lineEditPassword2.setGeometry(QtCore.QRect(120, 330, 381, 41))
        self.lineEditPassword2.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword2.setObjectName("lineEditPassword2")


        #Line Edit / Text Field for the Email
        self.lineEditEmail = QtWidgets.QLineEdit(registerForm)
        self.lineEditEmail.setGeometry(QtCore.QRect(120, 440, 381, 41))
        self.lineEditEmail.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditEmail.setObjectName("lineEditEmail")


        #Back Button for Registration Frame
        self.backButton = QtWidgets.QPushButton(registerForm)
        self.backButton.setGeometry(QtCore.QRect(60, 560, 161, 51))
        self.backButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.backButton.setObjectName("backButton")


        #Register / Submit Button
        self.registerButton = QtWidgets.QPushButton(registerForm)
        self.registerButton.setGeometry(QtCore.QRect(390, 560, 171, 51))
        self.registerButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.registerButton.setObjectName("registerButton")



        self.retranslateUi(registerForm)
        QtCore.QMetaObject.connectSlotsByName(registerForm)
        
        
        
            
    def retranslateUi(self, registerForm):
        _translate = QtCore.QCoreApplication.translate
        registerForm.setWindowTitle(_translate("registerForm", "Register"))
        self.labelRegisterHere.setText(_translate("registerForm", "REGISTER HERE"))
        self.lineEditName.setPlaceholderText(_translate("registerForm", "Name"))
        self.lineEditUsername2.setPlaceholderText(_translate("registerForm", "Username"))
        self.lineEditPassword2.setPlaceholderText(_translate("registerForm", "Password"))
        self.lineEditEmail.setPlaceholderText(_translate("registerForm", "Email"))
        self.backButton.setText(_translate("registerForm", "BACK"))
        self.registerButton.setText(_translate("registerForm", "REGISTER"))
        

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerForm = QtWidgets.QWidget()
    ui = Ui_registerForm()
    ui.setupUi(registerForm)
    registerForm.show()
    sys.exit(app.exec_())

