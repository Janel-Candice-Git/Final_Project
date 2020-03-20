from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Project import LogIn
from Project import Register 
from Project import ViewEvent
from Project import SetEvent
from Project import AboutUs
from Project import Home
from Project import ProgrammingLesson
from Project import LessonFrame
from Project import Programming2
from Project import MathLesson
from Project import BasicAlgebra
from Project import CalculusFrame
from Project import ScienceLesson
from Project import BiologyFrame
from Project import PhysicsFrame

from Project import DBQuery as SQL


#Instantiating Class Window Closing Functions (FRAME TRANSITIONING 1ST WAY)
class LoginWindow(QtWidgets.QMainWindow, LogIn.Ui_MainWindow1):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.registerButton.clicked.connect(self.hide)


class RegisterWindow(QtWidgets.QWidget, Register.Ui_registerForm):
    def __init__(self, parent = None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.backButton.clicked.connect(self.hide)
        
   
class HomeWindow(QtWidgets.QWidget, Home.Ui_homeForm):
    def __init__(self, parent = None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        self.aboutUsButton.clicked.connect(self.hide)
        self.viewEventButton.clicked.connect(self.hide)
        self.setEventButton.clicked.connect(self.hide)
        self.checkLesson.clicked.connect(self.hide)


class SetWindow(QtWidgets.QWidget, SetEvent.Ui_setEventForm):
    def __init__(self, parent = None):
        super(SetWindow, self).__init__(parent)
        self.setupUi(self)
        self.setBackButton.clicked.connect(self.hide)

       
class ViewWindow(QtWidgets.QWidget, ViewEvent.Ui_viewEventForm):
    def __init__(self, parent = None):
        super(ViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.viewBackButton.clicked.connect(self.hide)
        self.addButton.clicked.connect(self.hide)
        

class AboutWindow(QtWidgets.QWidget, AboutUs.Ui_aboutUsForm):
    def __init__(self, parent = None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.aboutBackButton.clicked.connect(self.hide)

class CheckLesson(QtWidgets.QWidget, LessonFrame.Ui_lessonForm):
    def __init__(self, parent = None):
        super(CheckLesson, self).__init__(parent)
        self.setupUi(self)
        self.lessonBackButton.clicked.connect(self.hide)
        self.lessonCompButton.clicked.connect(self.hide)
        self.lessonMathButton.clicked.connect(self.hide)
        self.lessongScienceButton.clicked.connect(self.hide)

class ProgLesson(QtWidgets.QWidget, ProgrammingLesson.Ui_progLessonForm):
    def __init__(self, parent = None):
        super(ProgLesson, self).__init__(parent)
        self.setupUi(self)
        self.progBackButton.clicked.connect(self.hide)
        self.progButton1.clicked.connect(self.hide)

class Programming2(QtWidgets.QWidget, Programming2.Ui_prog2Form):
    def __init__(self, parent = None):
        super (Programming2, self).__init__(parent)
        self.setupUi(self)
        self.prog2BackButton.clicked.connect(self.hide)

class MathLessons(QtWidgets.QWidget, MathLesson.Ui_mathLessonForm):
    def __init__(self, parent = None):
        super (MathLessons, self).__init__(parent)
        self.setupUi(self)
        self.mathBackButton.clicked.connect(self.hide)
        self.linearAlgebraButton.clicked.connect(self.hide)
        self.calculusButton.clicked.connect(self.hide)

class BasicAlgeb(QtWidgets.QWidget, BasicAlgebra.Ui_math1Form):
    def __init__(self, parent = None):
        super (BasicAlgeb, self).__init__(parent)
        self.setupUi(self)
        self.basicBackButton.clicked.connect(self.hide)

class Calculus1(QtWidgets.QWidget, CalculusFrame.Ui_math2Form ):
    def __init__(self, parent = None):
        super (Calculus1, self).__init__(parent)
        self.setupUi(self)
        self.calculusBackButton.clicked.connect(self.hide)

class ScienceLesson1(QtWidgets.QWidget, ScienceLesson.Ui_scienceLessonForm):
    def __init__(self, parent = None):
        super (ScienceLesson1, self).__init__(parent)
        self.setupUi(self)
        self.scienceBackButton.clicked.connect(self.hide)
        self.biologyButton.clicked.connect(self.hide)
        self.physicsButton.clicked.connect(self.hide)

class Biology(QtWidgets.QWidget, BiologyFrame.Ui_biologyForm):
    def __init__(self, parent = None):
        super (Biology, self).__init__(parent)
        self.setupUi(self)
        self.biologyBackButton.clicked.connect(self.hide)

class Physics(QtWidgets.QWidget, PhysicsFrame.Ui_physicsForm):
    def __init__(self, parent = None):
        super (Physics, self).__init__(parent)
        self.setupUi(self)
        self.physicsBackButton.clicked.connect(self.hide)
        


#Submit/Register/SetButtons
class frameManager:
    def __init__(self):
        
        #Instantiate the frames/window classes/global variables or objects
        self.loginframe = LoginWindow()
        self.registerframe = RegisterWindow()
        self.homeframe = HomeWindow()
        self.setframe = SetWindow()
        self.viewframe = ViewWindow()
        self.aboutframe = AboutWindow()
        self.lessonframe = CheckLesson()
        self.progframe = ProgLesson()
        self.proglessonframe = Programming2()
        self.mathlessonframe = MathLessons()
        self.basicalgebframe = BasicAlgeb()
        self.calculusframe = Calculus1()
        self.sciencelessonframe = ScienceLesson1()
        self.biologyframe = Biology()
        self.physicsframe = Physics()
        self.username = ''
        self.password = ''
        self.email = ''
        self.name = ''
        self.timestart = ''
        self.timeend = ''
        self.datestart = ''
        self.dateend = ''
        self.place = ''
        self.description = ''
        
        
        
        
        
        #Action Listener for Buttons (FRAME TRANSITIONING 2ND WAY) 
        
        #LOGIN window 
        #login->registration
        self.loginframe.registerButton.clicked.connect(self.registerframe.show)
        
        #login->homescreen with database verification
        self.loginframe.loginButton.clicked.connect(self.login)
        
        # REGISTRATION window
        #registration->login
        self.registerframe.backButton.clicked.connect(self.loginframe.show)
        
        #registration->database save
        self.registerframe.registerButton.clicked.connect(self.register)
        
        # HOME window 
        #homescreen->login with logout
        self.homeframe.logoutButton.clicked.connect(self.logout)   
        
        #homescreen->setframe
        self.homeframe.setEventButton.clicked.connect(self.setframe.show)
        
        #homescreen->viewframe with show all events user has
        self.homeframe.viewEventButton.clicked.connect(self.viewevent)
        
        #homescreen->Aboutus
        self.homeframe.aboutUsButton.clicked.connect(self.aboutframe.show)
        
        #SET window 
        #setframe->homescreen
        self.setframe.setBackButton.clicked.connect(self.homeframe.show)
        
        #setframe->database save
        self.setframe.setSubmitButton.clicked.connect(self.setevent)
        
        #Check Lesson Button -> Lesson Frame Window
        self.homeframe.checkLesson.clicked.connect(self.lessonframe.show)
        
        #View window 
        #viewframe->homescreen
        self.viewframe.viewBackButton.clicked.connect(self.homeframe.show)
        
        #Lesson Frame Window -> Home Frame
        self.lessonframe.lessonBackButton.clicked.connect(self.homeframe.show)
        
    
        self.lessonframe.lessonCompButton.clicked.connect(self.progframe.show)
        
        
        self.lessonframe.lessonMathButton.clicked.connect(self.mathlessonframe.show)
        
        
        self.progframe.progBackButton.clicked.connect(self.lessonframe.show)
        
        
        self.proglessonframe.prog2BackButton.clicked.connect(self.progframe.show)
        
        
        self.progframe.progButton1.clicked.connect (self.proglessonframe.show)
        
        
        self.mathlessonframe.linearAlgebraButton.clicked.connect(self.basicalgebframe.show)
        
        
        self.mathlessonframe.mathBackButton.clicked.connect(self.lessonframe.show)
        
        
        self.basicalgebframe.basicBackButton.clicked.connect(self.mathlessonframe.show)
        
        
        self.mathlessonframe.calculusButton.clicked.connect(self.calculusframe.show)
        
        
        self.calculusframe.calculusBackButton.clicked.connect(self.mathlessonframe.show)
        
        
        self.lessonframe.lessongScienceButton.clicked.connect(self.sciencelessonframe.show)
        
        
        self.sciencelessonframe.scienceBackButton.clicked.connect(self.lessonframe.show)
        
        
        self.sciencelessonframe.biologyButton.clicked.connect(self.biologyframe.show)
        
        
        self.sciencelessonframe.physicsButton.clicked.connect(self.physicsframe.show)
        
        
        self.biologyframe.biologyBackButton.clicked.connect(self.sciencelessonframe.show)
        
        
        self.physicsframe.physicsBackButton.clicked.connect(self.sciencelessonframe.show)
        
        
        #viewframe -> setevent
        self.viewframe.addButton.clicked.connect(self.setframe.show)
        
        
        
        self.viewframe.updateButton.clicked.connect(self.update)
        
        
        
        self.viewframe.deleteButton.clicked.connect(self.delete)
        
        
        #aboutus->homescreen
        self.aboutframe.aboutBackButton.clicked.connect(self.homeframe.show)
        
        #Show Login Window to start the program.
        self.loginframe.show()
        
        
        
    # Database Function and Back-end function
    def login(self):
        self.username = self.loginframe.lineEditUsername.text()
        self.password = self.loginframe.lineEditPassword.text()
        
        #Verification for login frame ( if text field was empty or wrong account)
        verification = SQL.verification_check(self.username, self.password)
        
        #Condition if username or password was empty or incorrect values
        if (self.username == '' or self.password == ''):
            print("Either one field is empty!")
        elif not (verification == None):
            
            print("Hello!", self.username)
            self.loginframe.hide()
            self.homeframe.show()
        else:
            print("Credentials is incorrect.")
            
            
    
    #Function for Logout Button
    def logout(self):
        self.username = ''
        self.password = ''
        self.loginframe.lineEditUsername.setText(self.username)
        self.loginframe.lineEditPassword.setText(self.password)
        self.homeframe.hide()
        self.loginframe.show()
        
        print("Logging Out!")
        
        
    #Function for Registration and Insertion to Database
    def register(self):
        
        #Instantiation of Variables for the Object name, username, password and email
        self.name = self.registerframe.lineEditName.text()
        self.username = self.registerframe.lineEditUsername2.text()
        self.password = self.registerframe.lineEditPassword2.text()
        self.email = self.registerframe.lineEditEmail.text()
        
        #Condition Statement if one or more values were empty
        #Elese if the requirements have been met the values will insert to the database
        if (self.name == '' or self.username == '' or self.password == '' or self.email == ''):
            print("One of the field boxes is empty.")
        else: 
            SQL.insert_user_data(self.username, self.name, self.password, self.email)
            #Clearing out the field boxes before transitioning
            self.name = ''
            self.username = ''
            self.password = ''
            self.email = ''
            self.registerframe.lineEditName.setText(self.name)
            self.registerframe.lineEditUsername2.setText(self.username)
            self.registerframe.lineEditPassword2.setText(self.password)
            self.registerframe.lineEditEmail.setText(self.email)
            self.registerframe.hide()
            self.loginframe.show()
        print("Operation Completed.")
     

    #Function for Viewing the Set Event         
    def viewevent(self):
        self.homeframe.hide()
        self.viewframe.show()
        self.viewframe.tableWidgetEvent.setRowCount(0)
        
        #Getting the Resultset or Fetching the Data that is being inserted in the Database
        #Placing it to the View Table 
        for row, form in enumerate(SQL.get_all_data(self.username)):
            self.viewframe.tableWidgetEvent.insertRow(row)
            for column, item in enumerate(form):
                self.viewframe.tableWidgetEvent.setItem(row, column, QTableWidgetItem(str(item)))
    
    #Function for Set Event        
    def setevent(self):
        
        #Instantiation for the objects start time, end time, start date, end date, place and description
        self.timestart = self.setframe.setStartTime.time().toString("hh:mm:ss")
        self.timeend = self.setframe.setEndTime.time().toString("hh:mm:ss")
        self.datestart = self.setframe.setStartDate.date().toString("yyyy-MM-dd")
        self.dateend = self.setframe.setEndDate.date().toString("yyyy-MM-dd")
        self.place = self.setframe.placeTextEdit.toPlainText()
        self.description = self.setframe.descriptionTextEdit.toPlainText()
        
        #If the values for Set Event were submitted.
        #SQL Command will insert all the values to the Database
        SQL.insert_set_event(self.username, self.timestart, self.timeend, self.datestart, self.dateend, self.place, self.description)
    
    
    #Function for Update Event Button in the View Events
    def update(self):
        self.toupdate = self.viewframe.searchEdit.toPlainText()
        self.updatesearch = SQL.get_search_data(self.username, self.toupdate)
        SQL.update_set_event(self.updatesearch[0], self.updatesearch[1], self.updatesearch[2], self.updatesearch[3], self.updatesearch[4], self.updatesearch[5])
    
    
    #Function for Delete Event Button in the View Events
    def delete(self):
        
        self.content = self.viewframe.searchEdit.toPlainText()
        self.deleterows = SQL.get_search_data(self.username, self.content)
        print(self.deleterows)
        
        
        self.delete1 = self.deleterows[0]
        self.delete2 = self.deleterows[1]
        self.delete3 = self.deleterows[2]
        self.delete4 = self.deleterows[3]
        self.delete5 = self.deleterows[4]
        self.delete6 = self.deleterows[5]
        self.delete7 = self.deleterows[6]
        SQL.delete_set_event(self.delete1, self.delete2, self.delete3, self.delete4, self.delete5, self.delete6, self.delete7)
        
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = frameManager()
    sys.exit(app.exec_())