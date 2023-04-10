
class BaseUser():
    def __init__(self,email,password):

        self.__email=email
        self.__password=password


    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password
        
class User(BaseUser):
    def __init__(self,email,password,name="",surname="",description="",profilepicture=""):
        super().__init__(email,password)
        self.__name=name
        self.__surname=surname
        self.__description=description
        self.__profilepicture=profilepicture
    
    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def description(self):
        return self.__description

    @property
    def profilepicture(self):
        return self.__profilepicture
    

class DatabaseUser(User):
    def __init__(self,ID,email,password,name="",surname="",description="",profilepicture=""):
        super().__init__(email,password,name,surname,description,profilepicture)
        self.__profilepicture=profilepicture
        self.__ID=ID
        

    @property
    def ID(self):
        return self.__ID


    @property
    def profilepicture(self):
        return self.__profilepicture

    @profilepicture.setter
    def profilepicture(self,value):
        self.__profilepicture=value
    
    



    


        
