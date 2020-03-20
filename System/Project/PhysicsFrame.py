from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib



class Ui_physicsForm(object):
    
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, physicsForm):
        
        
        physicsForm.setObjectName("physicsForm")
        physicsForm.resize(568, 598)
        
        
        self.calculusBG = QtWidgets.QLabel(physicsForm)
        self.calculusBG.setGeometry(QtCore.QRect(0, -40, 831, 741))
        self.calculusBG.setText("")
        self.calculusBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.calculusBG.setObjectName("calculusBG")
        
        
        
        self.calculusModal = QtWidgets.QLabel(physicsForm)
        self.calculusModal.setGeometry(QtCore.QRect(20, 20, 521, 551))
        self.calculusModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.calculusModal.setText("")
        self.calculusModal.setObjectName("calculusModal")
        
        
        
        self.labelPhysicsTutorial = QtWidgets.QLabel(physicsForm)
        self.labelPhysicsTutorial.setGeometry(QtCore.QRect(160, 40, 271, 61))
        self.labelPhysicsTutorial.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelPhysicsTutorial.setObjectName("labelPhysicsTutorial")
        
        
        
        self.physicsText = QtWidgets.QTextBrowser(physicsForm)
        self.physicsText.setGeometry(QtCore.QRect(70, 110, 441, 311))
        self.physicsText.setStyleSheet("")
        self.physicsText.setObjectName("physicsText")
        
        
        
        self.physicsBackButton = QtWidgets.QPushButton(physicsForm)
        self.physicsBackButton.setGeometry(QtCore.QRect(60, 500, 131, 51))
        self.physicsBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.physicsBackButton.setObjectName("physicsBackButton")
        
        

        self.retranslateUi(physicsForm)
        QtCore.QMetaObject.connectSlotsByName(physicsForm)

    def retranslateUi(self, physicsForm):
        
        
        _translate = QtCore.QCoreApplication.translate
        
        
        
        physicsForm.setWindowTitle(_translate("physicsForm", "Physics Tutorial"))
        self.labelPhysicsTutorial.setText(_translate("physicsForm", "PHYSICS TUTORIAL"))
        self.physicsText.setHtml(_translate("physicsForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">INTRODUCTION TO PHYSICS</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; font-weight:600; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">Physics</span><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\"> is the natural science that studies the matter and its motion and behaviour through space and time and that studies the related entities of energy and force. Let’s find out more about basic physics.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; font-weight:600; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">Physics</span><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\"> is one of the broader subjects that fall under the category of Science. The main object of all the three division, Biology, Physics, and Chemistry are to understand the law of the universe and understand everything in it. Physics is concerned with every aspect of Universe. It is a scientific study that governs the physical world and natural phenomenon around us. It deals with matter and its relation to energy.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216);\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">Everything from the rainbow formation of eclipse occurrence to the falling of things from up to down ( gravity ), the cause of sunset or sunrise is all bound to have answers and Basic Physics states it all. Behind every question lies the four important aspect or terms to understand: Hypothesis, Model, Theory, and Law.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216);\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">Gravity and Electric Current</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Open Sans,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; font-weight:600; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">Gravity</span><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\"> is one of the universal forces if nature that is a force acting upon all matters. The gravitational force between two objects is dependent on their masses. The first scientist to define the law of gravitation was Issac Newton. The law of gravitation states the gravity is strongest when between two huge objects and as and when those objects get apart, it gets much weaker.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216);\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">The interactions of the Universe are governed by the four forces including – Strong, Weak, Electromagnetic and Gravitational. Electric Current is another aspect of Physics which play a very important role. The continuous flow of electrons through a conducting material is known as </span><a href=\"https://www.toppr.com/guides/physics/electricity/electric-current-and-circuit-diagrams/\"><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">electric current</span></a><span style=\" font-family:\'Minion Pro,serif\'; font-size:12pt; color:rgba(0,0,0,0.839216); background-color:#ffffff;\">.</span></p></body></html>"))
        self.physicsBackButton.setText(_translate("physicsForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    physicsForm = QtWidgets.QWidget()
    ui = Ui_physicsForm()
    ui.setupUi(physicsForm)
    physicsForm.show()
    sys.exit(app.exec_())

