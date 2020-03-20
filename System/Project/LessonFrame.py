from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_lessonForm(object):
    
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, lessonForm):
        
        
        lessonForm.setObjectName("lessonForm")
        lessonForm.resize(781, 584)
        self.lessonBG = QtWidgets.QLabel(lessonForm)
        self.lessonBG.setGeometry(QtCore.QRect(-10, -30, 831, 741))
        self.lessonBG.setText("")
        self.lessonBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.lessonBG.setObjectName("lessonBG")
        
        
        
        self.lessonModal = QtWidgets.QLabel(lessonForm)
        self.lessonModal.setGeometry(QtCore.QRect(60, 30, 671, 521))
        self.lessonModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.lessonModal.setText("")
        self.lessonModal.setObjectName("lessonModal")
        
        
        
        self.lessonCompButton = QtWidgets.QPushButton(lessonForm)
        self.lessonCompButton.setGeometry(QtCore.QRect(280, 130, 251, 61))
        self.lessonCompButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.lessonCompButton.setObjectName("lessonCompButton")
        
        
        
        self.labelLessons = QtWidgets.QLabel(lessonForm)
        self.labelLessons.setGeometry(QtCore.QRect(340, 40, 141, 81))
        self.labelLessons.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelLessons.setObjectName("labelLessons")
        
        
        
        self.lessongScienceButton = QtWidgets.QPushButton(lessonForm)
        self.lessongScienceButton.setGeometry(QtCore.QRect(280, 340, 251, 61))
        self.lessongScienceButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.lessongScienceButton.setObjectName("lessongScienceButton")
        
        
        
        self.lessonMathButton = QtWidgets.QPushButton(lessonForm)
        self.lessonMathButton.setGeometry(QtCore.QRect(280, 230, 251, 61))
        self.lessonMathButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.lessonMathButton.setObjectName("lessonMathButton")
        
        
        
        self.lessonBackButton = QtWidgets.QPushButton(lessonForm)
        self.lessonBackButton.setGeometry(QtCore.QRect(90, 470, 161, 61))
        self.lessonBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.lessonBackButton.setObjectName("lessonBackButton")

        self.retranslateUi(lessonForm)
        QtCore.QMetaObject.connectSlotsByName(lessonForm)
        
        

    def retranslateUi(self, lessonForm):
        _translate = QtCore.QCoreApplication.translate
        lessonForm.setWindowTitle(_translate("lessonForm", "Lessons"))
        self.lessonCompButton.setText(_translate("lessonForm", "COMPUTER STUDIES"))
        self.labelLessons.setText(_translate("lessonForm", "LESSONS"))
        self.lessongScienceButton.setText(_translate("lessonForm", "SCIENCE "))
        self.lessonMathButton.setText(_translate("lessonForm", "MATH"))
        self.lessonBackButton.setText(_translate("lessonForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lessonForm = QtWidgets.QWidget()
    ui = Ui_lessonForm()
    ui.setupUi(lessonForm)
    lessonForm.show()
    sys.exit(app.exec_())

