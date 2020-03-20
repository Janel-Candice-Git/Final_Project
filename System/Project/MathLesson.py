from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_mathLessonForm(object):
    
    
    assets = pathlib.Path("Assets")
    
    
    def setupUi(self, mathLessonForm):
        
        
        mathLessonForm.setObjectName("mathLessonForm")
        mathLessonForm.resize(684, 514)
        
        
        self.mathBG = QtWidgets.QLabel(mathLessonForm)
        self.mathBG.setGeometry(QtCore.QRect(-40, -60, 831, 741))
        self.mathBG.setText("")
        self.mathBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.mathBG.setObjectName("mathBG")
        
        
        
        self.mathModal = QtWidgets.QLabel(mathLessonForm)
        self.mathModal.setGeometry(QtCore.QRect(20, 10, 641, 481))
        self.mathModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.mathModal.setText("")
        self.mathModal.setObjectName("mathModal")
        
        
        
        self.linearAlgebraButton = QtWidgets.QPushButton(mathLessonForm)
        self.linearAlgebraButton.setGeometry(QtCore.QRect(220, 140, 251, 61))
        self.linearAlgebraButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.linearAlgebraButton.setObjectName("linearAlgebraButton")
        
        
        
        self.mathBackButton = QtWidgets.QPushButton(mathLessonForm)
        self.mathBackButton.setGeometry(QtCore.QRect(50, 410, 131, 51))
        self.mathBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.mathBackButton.setObjectName("mathBackButton")
        
        
        
        self.calculusButton = QtWidgets.QPushButton(mathLessonForm)
        self.calculusButton.setGeometry(QtCore.QRect(220, 270, 251, 61))
        self.calculusButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.calculusButton.setObjectName("calculusButton")
        
        
        

        self.retranslateUi(mathLessonForm)
        QtCore.QMetaObject.connectSlotsByName(mathLessonForm)
        
        
        

    def retranslateUi(self, mathLessonForm):
        
        
        _translate = QtCore.QCoreApplication.translate
        mathLessonForm.setWindowTitle(_translate("mathLessonForm", "Math Lessons"))
        self.linearAlgebraButton.setText(_translate("mathLessonForm", "BASIC ALGEBRA"))
        self.mathBackButton.setText(_translate("mathLessonForm", "BACK"))
        self.calculusButton.setText(_translate("mathLessonForm", "CALCULUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mathLessonForm = QtWidgets.QWidget()
    ui = Ui_mathLessonForm()
    ui.setupUi(mathLessonForm)
    mathLessonForm.show()
    sys.exit(app.exec_())

