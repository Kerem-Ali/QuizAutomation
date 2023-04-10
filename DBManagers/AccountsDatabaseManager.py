import sqlite3


import sys
sys.path.insert(0, "..")
from CustomDataTypes import User,DatabaseUser


import os
print(os.getcwd())
os.chdir("DBManagers")

class AccountDatabaseManager():

    
    filename="database.sqlite3"
    
    def __init__(self):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""
        CREATE TABLE if  not exists ACCOUNTS (
            userID             INTEGER PRIMARY KEY AUTOINCREMENT,
            userEmail          TEXT    NOT NULL
                                       UNIQUE,
            userPassword       TEXT    NOT NULL,
            userName            TEXT    NOT NULL,
            userSurname        TEXT    NOT NULL,
            userDescription    TEXT,
            userProfilepicture TEXT
        );

            """)
        connection.commit()
        connection.close()
    
    def resetTable(self):
       connection=sqlite3.connect(self.filename)
       ex=connection.cursor()
       ex.execute("""
        CREATE TABLE ACCOUNTS (
            userID             INTEGER PRIMARY KEY AUTOINCREMENT,
            userEmail          TEXT    NOT NULL
                                       UNIQUE,
            userPassword       TEXT    NOT NULL,
            userName            TEXT    NOT NULL,
            userSurname        TEXT    NOT NULL,
            userDescription    TEXT,
            userProfilepicture TEXT
        );

            """)
       connection.commit()
       connection.close()


    def isAlreadyRegistered(self,email):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute("SELECT userEmail from ACCOUNTS")
        emails=[element[0] for element in cur.fetchall()]
        connection.close()
        
        return email in  emails

    def check_login(self,email,password):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT userEmail,userPassword from ACCOUNTS where userEmail="{}" and userPassword="{}"  """.format(email,password))
        emails=[element[0] for element in cur.fetchall()]
        connection.close()
        
        return email in  emails

    def IDtoName(self,userID):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT userName from ACCOUNTS where userID={}  """.format(userID))
        name=cur.fetchone()[0]
        connection.close()
        
        return name
        
        
        


    def getUserByEmail(self,email):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT userID,userEmail,userPassword,userName,userSurname,userDescription,userProfilepicture from ACCOUNTS where userEmail="{}" """.format(email))
        User=cur.fetchone()


        connection.close()
 
        return DatabaseUser(*User)

    def getUserByID(self,ID):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT userID,userEmail,userPassword,userName,userSurname,userDescription,userProfilepicture from ACCOUNTS where userID={} """.format(ID))
        user=cur.fetchone()
        ID=user[0]
        email=user[1]
        password=user[2]
        name=user[3]
        surname=user[4]
        description=user[5]
        profilepicture=user[6]

        connection.close()
 
        return DatabaseUser(ID,email,password,name,surname,description,profilepicture)

    def getUsers(self):
        Users=[]
        
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute("SELECT userID from ACCOUNTS")
        ids=[element[0] for element in cur.fetchall()]
        for ID in ids:
            Users.append(self.getUserByID(ID))
        return Users
        




    def addUser(self,email,password,name,surname):
        if self.isAlreadyRegistered(email):
            print("Bu email zaten kayıtlı")

        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        try:
            add = "insert into ACCOUNTS (userEmail,userPassword,userName,userSurname) values (?,?,?,?)"
            
            cur.execute(add,(email,password,name,surname))
            connection.commit()

        except Exception as error:
            print("Kayıt Eklenemedi Hata Çıktı === "+str(error))

        finally:
            connection.close()

    
    def updateEmail(self,ID,email):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute(""" update ACCOUNTS set userEmail="{}" where userID={}  """ .format(email,ID))
        connection.commit()
        connection.close()

    def updatePassword(self,ID,password):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute(""" update ACCOUNTS set userPassword="{}" where userID={} """.format(password,ID))
        connection.commit()
        connection.close()

    def updateName(self,ID,name):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""update ACCOUNTS set userName="{}" where userID={} """.format(name,ID))
        connection.commit()
        connection.close()

    def updateSurname(self,ID,surname):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute(""" update ACCOUNTS set userSurname="{}" where userID={} """.format(surname,ID))
        connection.commit()
        connection.close()

    def updateDescription(self,ID,description):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute(""" update ACCOUNTS set userDescription="{}" where userID={} """.format(description,ID))
        connection.commit()
        connection.close()


    def updateProfilePicture(self,ID,profilepicture):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute(""" update ACCOUNTS set userProfilepicture="{}" where userID={} """.format(profilepicture,ID))
        connection.commit()
        connection.close()
        


    


    def deleteUser(self,userID):
        #not finished
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        delete="""delete from users where userID="{}" """.format(userID)
        try:
            ex.execute(delete)
            connection.commit()
            connection.close()
        except Exception as error:
            print("Error:",error)

        finally:
            connection.close()

"""if __name__=="__main__":
    accountDatabaseManager=AccountDatabaseManager()
    #accountDatabaseManager.updateName(1,"kerem")
    #print(accountDatabaseManager.check_login("keremali@gmail.com","1234"))
    #print(accountDatabaseManager.isAlreadyRegistered("kali@gmail.com"))
    Users=accountDatabaseManager.getUsers()
    for User in Users:
        print("Name:",User.ID)"""
