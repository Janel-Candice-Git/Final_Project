from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib 


#Class Instantiation for LogIn Form
class Ui_MainWindow1(object):
    
    
    #Path directory for the Assets/Design Images 
    assets = pathlib.Path("Assets")
    
    
    #Function for Creating User Interfaces (LOGIN)
    def setupUi(self, MainWindow1):
        
        #Main Frame Login
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.setEnabled(True)
        MainWindow1.resize(621, 618)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(self.assets/"calendar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow1.setWindowIcon(icon)
        MainWindow1.setStyleSheet("")
        
        #Background for Login (Light Blue Background)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogInBG = QtWidgets.QLabel(self.centralwidget)
        self.labelLogInBG.setGeometry(QtCore.QRect(0, 0, 741, 651))
        self.labelLogInBG.setText("")
        self.labelLogInBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelLogInBG.setObjectName("labelLogInBG")
        
        #Modal (Black Container)
        self.labelModal = QtWidgets.QLabel(self.centralwidget)
        self.labelModal.setGeometry(QtCore.QRect(40, 90, 541, 481))
        self.labelModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal.setText("")
        self.labelModal.setObjectName("labelModal")
        
        #Login Button and Cascading Stylesheet (Design and Geometry)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(60, 500, 161, 51))
        self.loginButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.loginButton.setObjectName("loginButton")
        
        
        #Connection Action
        #Register Button and Cascading Stylesheet (Design and Geometry)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(390, 500, 171, 51))
        self.registerButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.registerButton.setObjectName("registerButton")
        
        #Line Edit / Text Field (Username)
        self.lineEditUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUsername.setGeometry(QtCore.QRect(110, 250, 381, 41))
        self.lineEditUsername.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditUsername.setObjectName("lineEditUsername")
      
        
        #Line Edit / Text Field (Password)
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(110, 380, 381, 41))
        self.lineEditPassword.setStyleSheet("QLineEdit { background: transparent; border:none; color:#717072;border-bottom:2px solid #717072; font-family: century gothic; font-size: 24px;}")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        
        
        #Label
        self.labelLoginHere = QtWidgets.QLabel(self.centralwidget)
        self.labelLoginHere.setGeometry(QtCore.QRect(220, 100, 321, 91))
        self.labelLoginHere.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelLoginHere.setObjectName("labelLoginHere")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

        #Compilation of the Objects in the MainWindow1 (LogIn Frame)
    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Welcome"))
        self.loginButton.setText(_translate("MainWindow1", "LOGIN"))
        self.registerButton.setText(_translate("MainWindow1", "REGISTER"))
        self.lineEditUsername.setPlaceholderText(_translate("MainWindow1", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow1", "Password"))
        self.labelLoginHere.setText(_translate("MainWindow1", "LOGIN HERE"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
