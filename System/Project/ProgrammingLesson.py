from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_progLessonForm(object):
    
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, progLessonForm):
        
        progLessonForm.setObjectName("progLessonForm")
        progLessonForm.resize(684, 514)
        
        
        self.programmingBG = QtWidgets.QLabel(progLessonForm)
        self.programmingBG.setGeometry(QtCore.QRect(-40, -60, 831, 741))
        self.programmingBG.setText("")
        self.programmingBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.programmingBG.setObjectName("programmingBG")
        
        
        
        self.programmingModal = QtWidgets.QLabel(progLessonForm)
        self.programmingModal.setGeometry(QtCore.QRect(20, 10, 641, 481))
        self.programmingModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.programmingModal.setText("")
        self.programmingModal.setObjectName("programmingModal")
        
        
        
        self.progButton1 = QtWidgets.QPushButton(progLessonForm)
        self.progButton1.setGeometry(QtCore.QRect(220, 220, 251, 61))
        self.progButton1.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.progButton1.setObjectName("progButton1")
        
        
        
        self.progBackButton = QtWidgets.QPushButton(progLessonForm)
        self.progBackButton.setGeometry(QtCore.QRect(50, 410, 131, 51))
        self.progBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.progBackButton.setObjectName("progBackButton")
        
        


        self.retranslateUi(progLessonForm)
        QtCore.QMetaObject.connectSlotsByName(progLessonForm)

    def retranslateUi(self, progLessonForm):
        _translate = QtCore.QCoreApplication.translate
        progLessonForm.setWindowTitle(_translate("progLessonForm", "Programming Lesson"))
        self.progButton1.setText(_translate("progLessonForm", "PROGRAMMING 1"))
        self.progBackButton.setText(_translate("progLessonForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progLessonForm = QtWidgets.QWidget()
    ui = Ui_progLessonForm()
    ui.setupUi(progLessonForm)
    progLessonForm.show()
    sys.exit(app.exec_())

