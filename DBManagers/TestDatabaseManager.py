import sqlite3

import sys
sys.path.insert(0, "..")
from CustomDataTypes import Test,DatabaseTest


from .QuestionDatabaseManager import QuestionDatabaseManager




class TestDatabaseManager:
    filename="database.sqlite3"
    def __init__(self,questionDatabaseManager):

        self.questionDatabaseManager=questionDatabaseManager
        
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""
        CREATE TABLE if not exists Quiz (
            quizID      INTEGER NOT NULL
                                PRIMARY KEY AUTOINCREMENT
                                DEFAULT (1) 
                                UNIQUE,
            quizName    TEXT    NOT NULL,
            category    TEXT    NOT NULL,
            dateCreated DATE    NOT NULL
                                DEFAULT (23 - 12 - 2007),
            authorID    INTEGER NOT NULL
                                REFERENCES ACCOUNTS (userID),
            plays       INTEGER DEFAULT (0) 
                                NOT NULL
        );



""")
        connection.commit()
        connection.close()

    def resetTable(self):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""

        CREATE TABLE Quiz (
            quizID      INTEGER NOT NULL
                                PRIMARY KEY AUTOINCREMENT
                                DEFAULT (1) 
                                UNIQUE,
            quizName    TEXT    NOT NULL,
            category    TEXT    NOT NULL,
            dateCreated DATE    NOT NULL
                                DEFAULT (23 - 12 - 2007),
            authorID    INTEGER NOT NULL
                                REFERENCES ACCOUNTS (userID),
            plays       INTEGER DEFAULT (0) 
                                NOT NULL
        );


""")
        connection.commit()
        connection.close()
        
        





    def getTestsInfos(self) ->list :
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        tests=[test for test in ex.execute("select * from Quiz")]
        connection.close()
        return tests

    def getTests(self) ->list :
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ids=[ID[0] for ID in ex.execute("select QuizID from Quiz").fetchall()]
        print(ids)
        connection.close()

        return [self.getTest(ID) for ID in ids]
        

    def getTest(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("select * from Quiz where quizID={}".format(quizID))
        test=ex.fetchone()
        questions=self.questionDatabaseManager.getQuestionsByQuizID(quizID)
        connection.close()
        return DatabaseTest(*test,questions)
        
        


    def addTestByTest(self,test:Test):
        from datetime import datetime
        now=str(datetime.today())[:10]
        
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        add="insert into Quiz (quizName,category,dateCreated,authorID) values (?,?,?,?)"
        

        ex.execute(add,(test.testName,test.category,now,test.authorID))
        connection.commit()
        connection.close()

        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()

        quizID=[x for x in ex.execute("SELECT MAX(quizID) from Quiz")][0][0]
        for question in test.questions:
            self.questionDatabaseManager.addQuestion(quizID,question)

        connection.commit()
        connection.close()


    def getNextQuizID(self):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        output=0
        try:
            output= [x for x in ex.execute("SELECT MAX(quizID) from Quiz")][0][0]+1
        except:
            output=1
        finally:
            return output

    def updateTest(self,databaseTest):
        
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        add=""" UPDATE Quiz set quizName="{}",category="{}",authorID={} where quizID={} """.format(
            databaseTest.testName,databaseTest.category,databaseTest.authorID,databaseTest.quizID)
        
        
        ex.execute(add)
        connection.commit()
        connection.close()

        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        

        for question in databaseTest.questions:
            self.questionDatabaseManager.updateQuestion(question)

        connection.commit()
        connection.close()
        
        



    def deleteTest(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("delete from Quiz where quizID={}".format(quizID))
        connection.commit()
        connection.close()

        from QuestionDatabaseManager import QuestionDatabaseManager
        
        self.questionDatabaseManager.deleteQuestionByQuizID(quizID)

    def getCategory(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("select category from Quiz where quizID={}".format(quizID))
        category=ex.fetchone()[0]
        connection.close()
        return category


    def getCorrectAnswers(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("select correct from Question where quizID={}".format(quizID))
        datas=[x[0] for x in ex.fetchall()]
        connection.close()
        return datas

    def howManyCreated(self,userID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        tests=[ID for ID in ex.execute("select QuizID from Quiz where authorID={}".format(userID))]
        connection.close()
        print(len(tests))
        return len(tests)

    def solvedPlus(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("select plays from Quiz where quizID={}".format(quizID))
        datas=[x for x in ex.fetchone()][0]
        print("datas",datas)

        ex.execute("update Quiz set plays={} where quizID={}".format(str(datas+1),quizID))

        connection.commit()
        connection.close()
        return datas
        
        
        





"""testDatabaseManager=TestDatabaseManager()

tests=testDatabaseManager.getTestsInfos()

tests=testDatabaseManager.getTests()
print(tests)"""

"""quests=[
FourChoiceQuestion("Benim adım?","Kerem Ali","Ali Kerem","Kemal","Kerem",1),
FourChoiceQuestion("Benim soyadım?","Kerem Ali","Avcioglu","Kemal","Kerem",2),
FourChoiceQuestion("Benim okulum?","ITU","MTAL","ITU MTAL","TEKNO",3)]
                         

testDatabaseManager.addTestByTest(Test(testName="Benim kimim?",category="Personal",authorID=1,questions=quests))"""



