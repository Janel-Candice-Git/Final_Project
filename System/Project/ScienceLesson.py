from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib



class Ui_scienceLessonForm(object):
    
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, scienceLessonForm):
        
        
        scienceLessonForm.setObjectName("scienceLessonForm")
        scienceLessonForm.resize(684, 515)
        
        
        self.scienceBG = QtWidgets.QLabel(scienceLessonForm)
        self.scienceBG.setGeometry(QtCore.QRect(-40, -60, 831, 741))
        self.scienceBG.setText("")
        self.scienceBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.scienceBG.setObjectName("scienceBG")
        
        
        
        self.scienceModal = QtWidgets.QLabel(scienceLessonForm)
        self.scienceModal.setGeometry(QtCore.QRect(20, 10, 641, 481))
        self.scienceModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.scienceModal.setText("")
        self.scienceModal.setObjectName("scienceModal")
        
        
        
        self.physicsButton = QtWidgets.QPushButton(scienceLessonForm)
        self.physicsButton.setGeometry(QtCore.QRect(220, 140, 251, 61))
        self.physicsButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.physicsButton.setObjectName("physicsButton")
        
        
        
        self.scienceBackButton = QtWidgets.QPushButton(scienceLessonForm)
        self.scienceBackButton.setGeometry(QtCore.QRect(50, 410, 131, 51))
        self.scienceBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.scienceBackButton.setObjectName("scienceBackButton")
        
        
        
        
        self.biologyButton = QtWidgets.QPushButton(scienceLessonForm)
        self.biologyButton.setGeometry(QtCore.QRect(220, 270, 251, 61))
        self.biologyButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.biologyButton.setObjectName("biologyButton")
        
        
        

        self.retranslateUi(scienceLessonForm)
        QtCore.QMetaObject.connectSlotsByName(scienceLessonForm)
        
        

    def retranslateUi(self, scienceLessonForm):
        
        
        _translate = QtCore.QCoreApplication.translate
        scienceLessonForm.setWindowTitle(_translate("scienceLessonForm", "Science Lesson"))
        self.physicsButton.setText(_translate("scienceLessonForm", "PHYSICS"))
        self.scienceBackButton.setText(_translate("scienceLessonForm", "BACK"))
        self.biologyButton.setText(_translate("scienceLessonForm", "BIOLOGY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scienceLessonForm = QtWidgets.QWidget()
    ui = Ui_scienceLessonForm()
    ui.setupUi(scienceLessonForm)
    scienceLessonForm.show()
    sys.exit(app.exec_())

