from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib



class Ui_biologyForm(object):
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, biologyForm):
        
        
        
        biologyForm.setObjectName("biologyForm")
        biologyForm.resize(568, 598)
        
        
        self.biologyBG = QtWidgets.QLabel(biologyForm)
        self.biologyBG.setGeometry(QtCore.QRect(0, -40, 831, 741))
        self.biologyBG.setText("")
        self.biologyBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.biologyBG.setObjectName("biologyBG")
        
        
        
        self.biologyModal = QtWidgets.QLabel(biologyForm)
        self.biologyModal.setGeometry(QtCore.QRect(20, 20, 521, 551))
        self.biologyModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.biologyModal.setText("")
        self.biologyModal.setObjectName("biologyModal")
        
        
        
        self.labelBiologyTutorial = QtWidgets.QLabel(biologyForm)
        self.labelBiologyTutorial.setGeometry(QtCore.QRect(160, 40, 271, 61))
        self.labelBiologyTutorial.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelBiologyTutorial.setObjectName("labelBiologyTutorial")
        
        
        
        self.biologyText = QtWidgets.QTextBrowser(biologyForm)
        self.biologyText.setGeometry(QtCore.QRect(70, 110, 441, 311))
        self.biologyText.setStyleSheet("")
        self.biologyText.setObjectName("biologyText")
        
        
        
        self.biologyBackButton = QtWidgets.QPushButton(biologyForm)
        self.biologyBackButton.setGeometry(QtCore.QRect(60, 500, 131, 51))
        self.biologyBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.biologyBackButton.setObjectName("biologyBackButton")
        
        
        

        self.retranslateUi(biologyForm)
        QtCore.QMetaObject.connectSlotsByName(biologyForm)

    def retranslateUi(self, biologyForm):
        
        
        
        _translate = QtCore.QCoreApplication.translate
        biologyForm.setWindowTitle(_translate("biologyForm", "Biology Tutorial"))
        self.labelBiologyTutorial.setText(_translate("biologyForm", "BIOLOGY TUTORIAL"))
        
        
        
        self.biologyText.setHtml(_translate("biologyForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">INTRODUCTION TO BIOLOGY</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">Biology </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\">is the study of living things. It encompasses the cellular basis of living things, the energy metabolism that underlies the activities of life, and the genetic basis for inheritance in organisms. Biology also includes the study of evolutionary relationships among organisms and the diversity of life on Earth. It considers the biology of microorganisms, plants, and animals, for example, and it brings together the structural and functional relationships that underlie their day-to-day activities. Biology draws on the sciences of chemistry and physics for its foundations and applies the laws of these disciplines to living things.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\">Many subdisciplines and special areas of biology exist, which can be conveniently divided into practical and theoretical categories. Types of </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">practical biology</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> include plant breeding, wildlife management, medical science, and crop production. </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">Theoretical biology</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> encompasses such disciplines as </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">physiology</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> (the study of the function of living things), </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">biochemistry</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> (the study of the chemistry of organisms), </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">taxonomy</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> (classification), </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">ecology</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> (the study of populations and their interactions with each other and their environments), and </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">microbiology</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> (the study of microscopic organisms).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latobold,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222; background-color:#ffffff;\">Characteristics of Living Things</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latobold,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\">Defining a living thing is a difficult proposition, as is defining “life”—that property possessed by living things. However, a living thing possesses certain properties that help define what life is.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\">Complex organization</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">Living things</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> have a level of complexity and organization not found in lifeless objects. At its most fundamental level, a living thing is composed of one or more </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">cells</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:696; color:#000000; background-color:#ffffff;\">.</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> These units, generally too small to be seen with the naked eye, are organized into tissues. A </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">tissue</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> is a series of cells that accomplish a shared function. Tissues, in turn, form </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">organs,</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> such as the stomach and kidney. A number of organs working together compose an </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">organ system.</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> An </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-style:italic; color:#000000; background-color:#ffffff;\">organism</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> is a complex series of various organ systems.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\">Metabolism</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">Living things</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> exhibit a rapid turnover of chemical materials, which is referred to as </span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000; background-color:#ffffff;\">metabolism</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:696; color:#000000; background-color:#ffffff;\">.</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"> Metabolism involves exchanges of chemical matter with the external environment and extensive transformations of organic matter within the cells of a living organism. Metabolism generally involves the release or use of chemical energy. Nonliving things do not display metabolism.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\">Responsiveness</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\">All living things are able to respond to stimuli in the external environment. For example, living things respond to changes in light, heat, sound, and chemical and mechanical contact. To detect stimuli, organisms have means for receiving information, such as eyes, ears, and taste buds.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\">To respond effectively to changes in the environment, an organism must coordinate its responses. A system of nerves and a number of chemical regulators called</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\"> hormones</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"> coordinate activities within an organism. The organism responds to the stimuli by means of a number of effectors, such as muscles and glands. Energy is generally used in the process.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\">Growth</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222; background-color:#ffffff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#000000;\">Growth</span><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\"> requires an organism to take in material from the environment and organize the material into its own structures. To accomplish growth, an organism expends some of the energy it acquires during metabolism. An organism has a pattern for accomplishing the building of growth structures.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; color:#000000;\">During growth, a living organism transforms material that is unlike itself into materials that are like it. A person, for example, digests a meal of meat and vegetables and transforms the chemical material into more of himself or herself. A nonliving organism does not display this characteristic.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'latoregular,Helvetica,Arial,sans-serif\'; font-size:12pt; font-weight:600; color:#222222;\"><br /></p></body></html>"))
        
        
        self.biologyBackButton.setText(_translate("biologyForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    biologyForm = QtWidgets.QWidget()
    ui = Ui_biologyForm()
    ui.setupUi(biologyForm)
    biologyForm.show()
    sys.exit(app.exec_())

