from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_math2Form(object):
    
    assets = pathlib.Path("Assets")
    
    
    def setupUi(self, math2Form):
        
        
        math2Form.setObjectName("math2Form")
        math2Form.resize(568, 598)
        
        
        
        self.calculusBG = QtWidgets.QLabel(math2Form)
        self.calculusBG.setGeometry(QtCore.QRect(0, -40, 831, 741))
        self.calculusBG.setText("")
        self.calculusBG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.calculusBG.setObjectName("calculusBG")
        
        
        
        self.calculusModal = QtWidgets.QLabel(math2Form)
        self.calculusModal.setGeometry(QtCore.QRect(20, 20, 521, 551))
        self.calculusModal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.calculusModal.setText("")
        self.calculusModal.setObjectName("calculusModal")
        
        
        
        self.labelCalculusTutorial = QtWidgets.QLabel(math2Form)
        self.labelCalculusTutorial.setGeometry(QtCore.QRect(120, 40, 381, 61))
        self.labelCalculusTutorial.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelCalculusTutorial.setObjectName("labelCalculusTutorial")
        
        
        
        self.calculusText = QtWidgets.QTextBrowser(math2Form)
        self.calculusText.setGeometry(QtCore.QRect(70, 110, 441, 311))
        self.calculusText.setStyleSheet("")
        self.calculusText.setObjectName("calculusText")
        
        
        
        self.calculusBackButton = QtWidgets.QPushButton(math2Form)
        self.calculusBackButton.setGeometry(QtCore.QRect(60, 500, 131, 51))
        self.calculusBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.calculusBackButton.setObjectName("calculusBackButton")
        
        

        self.retranslateUi(math2Form)
        QtCore.QMetaObject.connectSlotsByName(math2Form)
        
        
        

    def retranslateUi(self, math2Form):
        
        
        _translate = QtCore.QCoreApplication.translate
        math2Form.setWindowTitle(_translate("math2Form", "Calculus Tutorial"))
        self.labelCalculusTutorial.setText(_translate("math2Form", "CALCULUS TUTORIAL"))
        
        
        self.calculusText.setHtml(_translate("math2Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">INTRODUCTION TO CALCULUS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; color:#333333;\">The word Calculus comes from Latin meaning &quot;small stone&quot;, because it is like understanding something by looking at small pieces.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; font-weight:600; color:#333333;\">Differential Calculus</span><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; color:#333333;\"> cuts something into small pieces to find how it changes.</span><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; font-weight:600; color:#333333;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; font-weight:600; color:#333333;\">Integral Calculus</span><span style=\" font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; color:#333333;\"> joins (integrates) the small pieces together to find how much there is.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; color:#333333;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana,Arial,Tahoma,sans-serif\'; font-size:12pt; color:#333333;\"><br /></p></body></html>"))
        self.calculusBackButton.setText(_translate("math2Form", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    math2Form = QtWidgets.QWidget()
    ui = Ui_math2Form()
    ui.setupUi(math2Form)
    math2Form.show()
    sys.exit(app.exec_())

