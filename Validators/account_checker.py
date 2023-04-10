import sys
sys.path.insert(0, "../DBManagers")

from DBManagers import AccountDatabaseManager

sys.path.insert(0, "../CustomExceptions")

from CustomExceptions import InvalidLoginError,NullInputError

import os
#os.chdir("../DBManagers")

class AccountValidator():

    @staticmethod
    def check_login(func):
        def getInfos(email,password):
            
            acc_manager=AccountDatabaseManager()
            
            if email=="" or password=="":
                raise NullInputError("Email or password you entered is null")
            elif not(acc_manager.check_login(email,password)):
                raise InvalidLoginError("Email or password is invalid")
            else:
                func(email,password)


        

        return getInfos

    
    @staticmethod
    def check_register(func):
        def getInfos(name,surname,email,password,passwordAgain):
            acc_manager=AccountDatabaseManager()

            if name=="":
                raise NullInputError("Name is null")
            elif surname=="":
                raise NullInputError("Surname is null")
            elif not(AccountValidator.check_email(email)):
                raise NullInputError("Email is not correct format")
            elif len(password)<4:
                raise NullInputError("Password must be at least 4 char")
            elif password!=passwordAgain:
                raise NullInputError("Passwords are not same")
            elif acc_manager.isAlreadyRegistered(email):
                raise NullInputError("The email is already registered")

            func(name,surname,email,password,passwordAgain)

        return getInfos

    @staticmethod
    def check_email(email):
        return email.count("@")==1

