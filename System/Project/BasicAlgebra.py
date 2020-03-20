from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


class Ui_math1Form(object):
    
    
    assets = pathlib.Path("Assets")
    
    def setupUi(self, math1Form):
        
        
        math1Form.setObjectName("math1Form")
        math1Form.resize(568, 598)
        
        
        
        self.programming2BG = QtWidgets.QLabel(math1Form)
        self.programming2BG.setGeometry(QtCore.QRect(0, -40, 831, 741))
        self.programming2BG.setText("")
        self.programming2BG.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.programming2BG.setObjectName("programming2BG")
        
        
        
        self.programming2Modal = QtWidgets.QLabel(math1Form)
        self.programming2Modal.setGeometry(QtCore.QRect(20, 20, 521, 551))
        self.programming2Modal.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.programming2Modal.setText("")
        self.programming2Modal.setObjectName("programming2Modal")
        
        
        
        self.labelAlgebraTutorial = QtWidgets.QLabel(math1Form)
        self.labelAlgebraTutorial.setGeometry(QtCore.QRect(90, 40, 381, 61))
        self.labelAlgebraTutorial.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelAlgebraTutorial.setObjectName("labelAlgebraTutorial")
        
        
        
        self.basicAlgebraText = QtWidgets.QTextBrowser(math1Form)
        self.basicAlgebraText.setGeometry(QtCore.QRect(70, 110, 441, 311))
        self.basicAlgebraText.setStyleSheet("")
        self.basicAlgebraText.setObjectName("basicAlgebraText")
        
        
        
        self.basicBackButton = QtWidgets.QPushButton(math1Form)
        self.basicBackButton.setGeometry(QtCore.QRect(60, 500, 131, 51))
        self.basicBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.basicBackButton.setObjectName("basicBackButton")
        
        
        

        self.retranslateUi(math1Form)
        QtCore.QMetaObject.connectSlotsByName(math1Form)





    def retranslateUi(self, math1Form):
        _translate = QtCore.QCoreApplication.translate
        math1Form.setWindowTitle(_translate("math1Form", "Basic Algebra"))
        self.labelAlgebraTutorial.setText(_translate("math1Form", "BASIC ALGEBRA TUTORIAL"))
        self.basicAlgebraText.setHtml(_translate("math1Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">INTRODUCTION TO INTEGERS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">Basically, integers are used to represent situations that whole numbers are not able to represent mathematically.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">For examples, adding money to a saving account or withdrawing money from a saving account, gains and losses when playing a football game are situations that require both positive and negative numbers.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; font-weight:600; color:#666666;\">COMPARING INTEGERS</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; font-weight:600; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">When comparing integers, you can use a number line and this is what we will use to show you how to compare integers.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">Any number to the right of 0 gets bigger and bigger as you move to the right.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">Therefore, if the numbers are positive, the smaller number is the one closer to 0.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">Any number to the left of 0 gets smaller and smaller as you move to the left. So, if the numbers are negative, the bigger number is the one closer to zero.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; font-weight:600; color:#666666;\">ADDING INTEGERS</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; font-weight:600; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; font-weight:600; color:#666666;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">When adding integers, use a number line to help you think through problems.It will be really helpful.</span><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></span></p>\n"
"<p style=\" margin-top:21px; margin-bottom:32px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666; background-color:#ffffff;\">For example: 2 + 6</span><span style=\" font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /><br />Start at 2 and move 6 units to the right.<br /><br />Since you stopped at 8, the answer is 8<br /><br />Notice that you would get the same answer if you start at 6 and move 2 units to the right.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:12pt; color:#666666;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#666666;\"><br /></p></body></html>"))
        self.basicBackButton.setText(_translate("math1Form", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    math1Form = QtWidgets.QWidget()
    ui = Ui_math1Form()
    ui.setupUi(math1Form)
    math1Form.show()
    sys.exit(app.exec_())

