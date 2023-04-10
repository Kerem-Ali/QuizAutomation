import sys

import pip


try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    pip.main(['install', 'PyQt5'])



from UI.login.login import Login_Window
from UI.register.register import Register_Window
from UI.base.mainUI import MainUI

sys.path.insert(0, "../DBManagers")
sys.path.insert(0, "../CustomDataTypes")

from DBManagers import AccountDatabaseManager,QuestionDatabaseManager,TestDatabaseManager,ResultsDatabaseManager




from Validators.account_checker import AccountValidator,  InvalidLoginError,NullInputError
#from CustomExceptions.customExceptions import InvalidLoginError,NullInputError



import os
#os.chdir("DBManagers")

accountManager=AccountDatabaseManager()
questionManager=QuestionDatabaseManager()
testManager=TestDatabaseManager(questionManager)
resultsManager=ResultsDatabaseManager(testManager)


class App(QtWidgets.QApplication):
    def __init__(self,*args):
        super().__init__(*args)
        self.window=Login_Window()
        
        self.setupLogin()

    def setupLogin(self,message=""):
        if not isinstance(message,str):
            message=""

        self.window=Login_Window()
       
        self.window.loginButton.clicked.connect(self.tryLogin)
        self.window.registerButton.clicked.connect(self.setupRegister)
        self.window.statusbar.showMessage(message)
        self.window.show()
        
    def setupRegister(self):
        self.window=Register_Window()
        self.window.registerButton.clicked.connect(self.tryRegister)
        self.window.loginButton.clicked.connect(self.setupLogin)
        self.window.show()
        


    def tryLogin(self):
        try:
            self.window.statusbar.showMessage("Logging in")
            self.setupBase(self.window.inputEmail.text().strip(),self.window.inputPassword.text())
        except InvalidLoginError as ex:
            print("this")
            self.window.statusbar.showMessage(ex.message)
        except NullInputError as ex:
            self.window.statusbar.showMessage(ex.message)
        
        
    def tryRegister(self):
        @AccountValidator.check_register
        def register(name,surname,email,password,passwordAgain):
            accountManager.addUser(email,password,name,surname)
        register=staticmethod(register)
        try:
            register(self.window.inputName.text(),self.window.inputSurname.text(),self.window.inputEmail.text(),
                          self.window.inputPassword.text(),self.window.inputPasswordAgain.text())

            self.window.statusbar.showMessage("Successfully registered")
            
            self.setupLogin("Successfully registered")
        except NullInputError as ex:
            self.window.statusbar.showMessage(str(ex))

        except Exception as ex:
            print(ex)

    

    def setupBase(self,email,password):
        def get_user(email,password):
            if accountManager.check_login(email,password):
                return accountManager.getUserByEmail(email)
            else:
                raise InvalidLoginError()
        get_user=staticmethod(get_user)

        user=get_user(email,password)
        print(user)
        self.window=MainUI(accountManager,questionManager,testManager,resultsManager,user,self)

        self.window.headWidget.navbar.exit.clicked.connect(self.setupLogin)
        self.window.statusbar.showMessage("Welcome "+user.name)

        self.window.headWidget.navbar.exit.clicked.connect(self.setupLogin)
        self.window.show()
        
            


    
        

    


app = App(sys.argv)
sys.exit(app.exec_())

    




