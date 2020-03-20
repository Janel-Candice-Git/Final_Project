from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


#Class Instantiation for Set Event Form
class Ui_setEventForm(object):
    
    #File Directory for Design/Background Images etc/
    assets = pathlib.Path("Assets")
    
    
    #Create Function for creating User Interfaces (SET EVENT)
    def setupUi(self, setEventForm):
        
        
        #Window Frame for SetEven (Dimension and Object Name)
        setEventForm.setObjectName("setEventForm")
        setEventForm.resize(946, 685)
        
        
        #Background for SetEvent Window/Frame
        self.labelSetEvent = QtWidgets.QLabel(setEventForm)
        self.labelSetEvent.setGeometry(QtCore.QRect(-20, -90, 971, 831))
        self.labelSetEvent.setText("")
        self.labelSetEvent.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelSetEvent.setObjectName("labelSetEvent")
        
        
        #Black Container
        self.labelModal5 = QtWidgets.QLabel(setEventForm)
        self.labelModal5.setGeometry(QtCore.QRect(60, 20, 841, 651))
        self.labelModal5.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal5.setText("")
        self.labelModal5.setObjectName("labelModal5")
        
        
        #Date Edit for set Start-Date
        self.setStartDate = QtWidgets.QDateEdit(setEventForm)
        self.setStartDate.setGeometry(QtCore.QRect(140, 140, 251, 51))
        self.setStartDate.setStyleSheet("QDateEdit{ background-color: #black; border-style: solid; border-width: 4px; border-color: rgb(100,100,100);  spacing: 10px; font-family: century gothic;\n"
"font-size: 24px;}\n"
"")
        self.setStartDate.setCalendarPopup(True)
        self.setStartDate.setObjectName("setStartDate")
        
        
        
        #Label for set Start-Date
        self.labelStartDate = QtWidgets.QLabel(setEventForm)
        self.labelStartDate.setGeometry(QtCore.QRect(150, 60, 171, 61))
        self.labelStartDate.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelStartDate.setObjectName("labelStartDate")
        
        
        
        #Label for set End-Date
        self.labelEndDate = QtWidgets.QLabel(setEventForm)
        self.labelEndDate.setGeometry(QtCore.QRect(580, 60, 171, 61))
        self.labelEndDate.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelEndDate.setObjectName("labelEndDate")
        
        
        
        #Date Edit for set End-Date
        self.setEndDate = QtWidgets.QDateEdit(setEventForm)
        self.setEndDate.setGeometry(QtCore.QRect(570, 140, 251, 51))
        self.setEndDate.setStyleSheet("QDateEdit{ background-color: #black; border-style: solid; border-width: 4px; border-color: rgb(100,100,100);  spacing: 10px; font-family: century gothic;\n"
"font-size: 24px;}\n"
"")
        self.setEndDate.setCalendarPopup(True)
        self.setEndDate.setObjectName("setEndDate")
        
        
        
        #Label for set Start-Time
        self.labelStartTime = QtWidgets.QLabel(setEventForm)
        self.labelStartTime.setGeometry(QtCore.QRect(140, 250, 171, 61))
        self.labelStartTime.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelStartTime.setObjectName("labelStartTime")
        
        
        
        #Time Edit for set Start-Time
        self.setStartTime = QtWidgets.QTimeEdit(setEventForm)
        self.setStartTime.setEnabled(True)
        self.setStartTime.setGeometry(QtCore.QRect(130, 320, 251, 51))
        self.setStartTime.setStyleSheet("QTimeEdit{ background-color: #black; border-style: solid; border-width: 4px; border-color: rgb(100,100,100);  spacing: 10px; font-family: century gothic;\n"
"font-size: 24px;}\n"
"")
        self.setStartTime.setKeyboardTracking(False)
        self.setStartTime.setCalendarPopup(False)
        self.setStartTime.setObjectName("setStartTime")
        
        
        
        #Label for set End-Time
        self.labelEndTime = QtWidgets.QLabel(setEventForm)
        self.labelEndTime.setGeometry(QtCore.QRect(580, 240, 171, 61))
        self.labelEndTime.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelEndTime.setObjectName("labelEndTime")
        
        
        
        #Time Edit for set End-Time
        self.setEndTime = QtWidgets.QTimeEdit(setEventForm)
        self.setEndTime.setEnabled(True)
        self.setEndTime.setGeometry(QtCore.QRect(570, 320, 261, 51))
        self.setEndTime.setStyleSheet("QTimeEdit{ background-color: #black; border-style: solid; border-width: 4px; border-color: rgb(100,100,100);  spacing: 10px; font-family: century gothic;\n"
"font-size: 24px;}\n"
"")
        self.setEndTime.setKeyboardTracking(False)
        self.setEndTime.setCalendarPopup(False)
        self.setEndTime.setObjectName("setEndTime")
        
        
        
        #Label for Place
        self.labelPlace = QtWidgets.QLabel(setEventForm)
        self.labelPlace.setGeometry(QtCore.QRect(240, 430, 111, 51))
        self.labelPlace.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelPlace.setObjectName("labelPlace")
        
        
        
        #Text Edit for Place
        self.placeTextEdit = QtWidgets.QTextEdit(setEventForm)
        self.placeTextEdit.setGeometry(QtCore.QRect(370, 430, 281, 51))
        self.placeTextEdit.setStyleSheet("QTextEdit {font-style:century gothic; font-size:24px;}")
        self.placeTextEdit.setObjectName("placeTextEdit")
        
        
        
        #Label for Description
        self.labelDescription = QtWidgets.QLabel(setEventForm)
        self.labelDescription.setGeometry(QtCore.QRect(140, 520, 211, 51))
        self.labelDescription.setStyleSheet("QLabel{font-size: 30px; font-family: century gothic; color: white;}")
        self.labelDescription.setObjectName("labelDescription")
        
        
        
        #Text Edit for Description
        self.descriptionTextEdit = QtWidgets.QTextEdit(setEventForm)
        self.descriptionTextEdit.setGeometry(QtCore.QRect(370, 520, 281, 51))
        self.descriptionTextEdit.setStyleSheet("QTextEdit {font-style:century gothic; font-size:24px;}")
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        
        
        
        #Back Button
        self.setBackButton = QtWidgets.QPushButton(setEventForm)
        self.setBackButton.setGeometry(QtCore.QRect(100, 600, 171, 51))
        self.setBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.setBackButton.setObjectName("setBackButton")
        
        
        
        #Submit Button for Set Event
        self.setSubmitButton = QtWidgets.QPushButton(setEventForm)
        self.setSubmitButton.setGeometry(QtCore.QRect(690, 600, 171, 51))
        self.setSubmitButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.setSubmitButton.setObjectName("setSubmitButton")

        self.retranslateUi(setEventForm)
        QtCore.QMetaObject.connectSlotsByName(setEventForm)

    #Compilation ng Object sa SetEvent.py frame
    def retranslateUi(self, setEventForm):
        
        
        #Compiling all objects in the SetEvent Frame 
        _translate = QtCore.QCoreApplication.translate
        setEventForm.setWindowTitle(_translate("setEventForm", "Set Event"))
        self.labelStartDate.setText(_translate("setEventForm", "START DATE:"))
        self.labelEndDate.setText(_translate("setEventForm", "END DATE:"))
        self.labelStartTime.setText(_translate("setEventForm", "START TIME:"))
        self.labelEndTime.setText(_translate("setEventForm", "END TIME:"))
        self.labelPlace.setText(_translate("setEventForm", "PLACE:"))
        self.labelDescription.setText(_translate("setEventForm", "DESCRIPTION:"))
        self.setBackButton.setText(_translate("setEventForm", "BACK"))
        self.setSubmitButton.setText(_translate("setEventForm", "SUBMIT"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setEventForm = QtWidgets.QWidget()
    ui = Ui_setEventForm()
    ui.setupUi(setEventForm)
    setEventForm.show()
    sys.exit(app.exec_())

