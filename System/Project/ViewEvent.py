from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib



#Class Instantiation for View Event Form
class Ui_viewEventForm(object):
    
    
    #File Directory for Design/Background Images etc/
    assets = pathlib.Path("Assets")
    
    def setupUi(self, viewEventForm):
        
        viewEventForm.setObjectName("viewEventForm")
        viewEventForm.resize(893, 611)
        
        self.labelViewEvent = QtWidgets.QLabel(viewEventForm)
        self.labelViewEvent.setGeometry(QtCore.QRect(0, -50, 901, 771))
        self.labelViewEvent.setText("")
        self.labelViewEvent.setPixmap(QtGui.QPixmap(str(self.assets/"label_bg.jpg")))
        self.labelViewEvent.setObjectName("labelViewEvent")
        
        
        
        self.labelModal6 = QtWidgets.QLabel(viewEventForm)
        self.labelModal6.setGeometry(QtCore.QRect(30, 10, 841, 581))
        self.labelModal6.setStyleSheet("QLabel{ background: #333; border-radius: 10px;}")
        self.labelModal6.setText("")
        self.labelModal6.setObjectName("labelModal6")
        
        
        #Create Table Widget
        self.tableWidgetEvent = QtWidgets.QTableWidget(viewEventForm)
        self.tableWidgetEvent.setGeometry(QtCore.QRect(70, 40, 761, 311))
        self.tableWidgetEvent.setRowCount(5)
        self.tableWidgetEvent.setColumnCount(7)
        self.tableWidgetEvent.setObjectName("tableWidgetEvent")
        
        #Row and Column Values
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetEvent.setHorizontalHeaderItem(6, item)        
        
        
        self.addButton = QtWidgets.QPushButton(viewEventForm)
        self.addButton.setGeometry(QtCore.QRect(470, 370, 171, 51))
        self.addButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.addButton.setObjectName("addButton")
        
        
        self.updateButton = QtWidgets.QPushButton(viewEventForm)
        self.updateButton.setGeometry(QtCore.QRect(280, 370, 171, 51))
        self.updateButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.updateButton.setObjectName("updateButton")
        
        
        self.deleteButton = QtWidgets.QPushButton(viewEventForm)
        self.deleteButton.setGeometry(QtCore.QRect(670, 370, 171, 51))
        self.deleteButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.deleteButton.setObjectName("deleteButton")
        
        
        
        self.viewBackButton = QtWidgets.QPushButton(viewEventForm)
        self.viewBackButton.setGeometry(QtCore.QRect(60, 510, 171, 51))
        self.viewBackButton.setStyleSheet("QPushButton{font-family: century gothic; font-size: 24px;  background: white; color: black; border-radius: 10px;}\n"
"QPushButton:hover{  color: black; background: lightblue;}")
        self.viewBackButton.setObjectName("viewBackButton")
        
        
        #Search Bar
        self.searchEdit = QtWidgets.QTextEdit(viewEventForm)
        self.searchEdit.setGeometry(QtCore.QRect(60, 380, 191, 41))
        self.searchEdit.setObjectName("searchEdit")
        self.searchEdit.setStyleSheet("QTextEdit {font-style:century gothic; font-size:24px;}")


        self.retranslateUi(viewEventForm)
        QtCore.QMetaObject.connectSlotsByName(viewEventForm)
        
        

    def retranslateUi(self, viewEventForm):
        
        _translate = QtCore.QCoreApplication.translate
        
        
        
        viewEventForm.setWindowTitle(_translate("viewEventForm", "View Event"))
        item = self.tableWidgetEvent.horizontalHeaderItem(0)
        item.setText(_translate("viewEventForm", "Number"))
        item = self.tableWidgetEvent.horizontalHeaderItem(1)
        item.setText(_translate("viewEventForm", "Start Time"))
        item = self.tableWidgetEvent.horizontalHeaderItem(2)
        item.setText(_translate("viewEventForm", "End Time"))
        item = self.tableWidgetEvent.horizontalHeaderItem(3)
        item.setText(_translate("viewEventForm", "Start Date"))
        item = self.tableWidgetEvent.horizontalHeaderItem(4)
        item.setText(_translate("viewEventForm", "End Date"))
        item = self.tableWidgetEvent.horizontalHeaderItem(5)
        item.setText(_translate("viewEventForm", "Place"))
        item = self.tableWidgetEvent.horizontalHeaderItem(6)
        item.setText(_translate("viewEventForm", "Description"))       
        
        self.addButton.setText(_translate("viewEventForm", "ADD"))
        self.updateButton.setText(_translate("viewEventForm", "EDIT"))
        self.deleteButton.setText(_translate("viewEventForm", "ERASE"))
        self.viewBackButton.setText(_translate("viewEventForm", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewEventForm = QtWidgets.QWidget()
    ui = Ui_viewEventForm()
    ui.setupUi(viewEventForm)
    viewEventForm.show()
    sys.exit(app.exec_())

