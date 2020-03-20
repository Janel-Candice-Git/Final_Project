from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


#Class Instantiation for About Us Form
class Ui_aboutUsForm(object):
    
    
    
    #File Directory for Design/Background Images etc/
    assets = pathlib.Path("Assets")
    
    
    #Function for Creating User Interface 
    def setupUi(self, aboutUsForm):
        
        
        aboutUsForm.setObjectName("aboutUsForm")
        aboutUsForm.resize(793, 640)
        self.labelAboutBG = QtWidgets.QLabel(aboutUsForm)
        self.labelAboutBG.setGeometry(QtCore.QRect(-10, -10, 801, 651))
        self.labelAboutBG.setText("")
        self.labelAboutBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelAboutBG.setObjectName("labelAboutBG")
        self.labelModal4 = QtWidgets.QLabel(aboutUsForm)
        self.labelModal4.setGeometry(QtCore.QRect(70, 40, 651, 581))
        self.labelModal4.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal4.setText("")
        self.labelModal4.setObjectName("labelModal4")
        self.labelAuthor1 = QtWidgets.QLabel(aboutUsForm)
        self.labelAuthor1.setGeometry(QtCore.QRect(110, 150, 201, 181))
        self.labelAuthor1.setStyleSheet("QLabel{ border-radius: 20px;}")
        self.labelAuthor1.setText("")
        self.labelAuthor1.setPixmap(QtGui.QPixmap(str(self.assets/"image11.jpg")))
        self.labelAuthor1.setObjectName("labelAuthor1")
        self.authorTextInfo = QtWidgets.QPlainTextEdit(aboutUsForm)
        self.authorTextInfo.setEnabled(False)
        self.authorTextInfo.setGeometry(QtCore.QRect(320, 160, 361, 201))
        self.authorTextInfo.setStyleSheet("QPlainTextEdit{ background: #333; font-style:century gothic; font-size:24px;\n"
"color: white; border:none}")
        self.authorTextInfo.setObjectName("authorTextInfo")
        self.labelAuthor2 = QtWidgets.QLabel(aboutUsForm)
        self.labelAuthor2.setGeometry(QtCore.QRect(120, 350, 191, 181))
        self.labelAuthor2.setText("")
        self.labelAuthor2.setPixmap(QtGui.QPixmap(str(self.assets/"image22.jpg")))
        self.labelAuthor2.setObjectName("labelAuthor2")
        self.authorTextInfo2 = QtWidgets.QPlainTextEdit(aboutUsForm)
        self.authorTextInfo2.setEnabled(False)
        self.authorTextInfo2.setGeometry(QtCore.QRect(320, 350, 391, 201))
        self.authorTextInfo2.setStyleSheet("QPlainTextEdit{ background: #333; font-style:century gothic; font-size:24px;\n"
"color: white; border:none}")
        self.authorTextInfo2.setObjectName("authorTextInfo2")
        self.labelAboutUs = QtWidgets.QLabel(aboutUsForm)
        self.labelAboutUs.setGeometry(QtCore.QRect(330, 40, 321, 91))
        self.labelAboutUs.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelAboutUs.setObjectName("labelAboutUs")
        self.aboutBackButton = QtWidgets.QPushButton(aboutUsForm)
        self.aboutBackButton.setGeometry(QtCore.QRect(320, 560, 161, 51))
        self.aboutBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.aboutBackButton.setObjectName("aboutBackButton")

        self.retranslateUi(aboutUsForm)
        QtCore.QMetaObject.connectSlotsByName(aboutUsForm)

    def retranslateUi(self, aboutUsForm):
        _translate = QtCore.QCoreApplication.translate
        aboutUsForm.setWindowTitle(_translate("aboutUsForm", "About Us"))
        self.authorTextInfo.setPlainText(_translate("aboutUsForm", "DELEON, SHEINA MAE\n"
"\n"
"CPE12FC1\n"
"\n"
"sheinamaedeleon@gmail.com"))
        self.authorTextInfo2.setPlainText(_translate("aboutUsForm", "DEL ROSARIO, JANEL CANDICE S.\n"
"\n"
"CPE12FC1\n"
"\n"
"delrosario.janelcandice@gmail.com"))
        self.labelAboutUs.setText(_translate("aboutUsForm", "AUTHORS"))
        self.aboutBackButton.setText(_translate("aboutUsForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutUsForm = QtWidgets.QWidget()
    ui = Ui_aboutUsForm()
    ui.setupUi(aboutUsForm)
    aboutUsForm.show()
    sys.exit(app.exec_())

