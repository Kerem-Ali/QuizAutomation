import sqlite3
import sys
sys.path.insert(0, "..")

from CustomDataTypes import DatabaseUser,DatabaseTest,DatabaseFourChoiceQuestion


from .TestDatabaseManager import TestDatabaseManager



class ResultsDatabaseManager():
    filename="database.sqlite3"
    
    def __init__(self,tdm):
        self.tdm=tdm
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""
        CREATE TABLE if not exists Results (
                userID      INTEGER REFERENCES ACCOUNTS (userID) ON DELETE SET NULL
                                                                 ON UPDATE CASCADE
                                                                 MATCH SIMPLE
                                    NOT NULL,
                quizID      INTEGER REFERENCES Quiz (quizID) 
                                    NOT NULL,
                userAnswers TEXT    NOT NULL,
                date        DATE    NOT NULL
            );


            """)
        connection.commit()
        connection.close()
    
    def resetTable(self):
       connection=sqlite3.connect(self.filename)
       ex=connection.cursor()
       ex.execute("""
        CREATE TABLE Results (
            userID      INTEGER REFERENCES ACCOUNTS (userID) ON DELETE SET NULL
                                                             ON UPDATE CASCADE
                                                             MATCH SIMPLE
                                NOT NULL,
            quizID      INTEGER REFERENCES Quiz (quizID) 
                                NOT NULL,
            userAnswers TEXT    NOT NULL,
            date        DATE    NOT NULL
        );


            """)
       connection.commit()
       connection.close()

    def commitUserResults(self,databaseUser,databaseQuiz):
        from datetime import datetime
        now=str(datetime.today())[:10]
        print(now)
        
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        add="insert into Results (userID,quizID,userAnswers,date) values (?,?,?,?)"
        
        
        ex.execute(add,(databaseUser.ID,databaseQuiz.quizID,str([answer.selected for answer in databaseQuiz.questions]),now))
        connection.commit()

        self.tdm.solvedPlus(databaseQuiz.quizID)

        
        connection.close()

    def getSolvedQuizIDs(self,userID):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT quizID from Results where userID={} """.format(userID))
        ids=cur.fetchall()
        print(ids)

        connection.close()
 
        return [x[0] for x in ids]

    def getDate(self,userID):
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        print("userID",userID)
        cur.execute(""" SELECT date from Results where userID={} """.format(userID))
        dates=cur.fetchall()


        connection.close()
        return [x[0] for x in dates]

    def getUserAnswers(self,quizID,userID):
        from ast import literal_eval
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT userAnswers from Results where userID={} and quizID={} """.format(userID,quizID))
        datas=[literal_eval(x[0]) for x in cur.fetchall()]


        connection.close()
        return datas

        

    def getCategoryAndRates(self,userID):
        def getRate(userID,quizID,answers):
            correctAnswers=self.tdm.getCorrectAnswers(quizID)
            rate={"correct":0,"incorrect":0,"notAnswered":0}
            for i,x in enumerate(answers):

                if x==0:
                    rate["notAnswered"]+=1
                else:
                    if correctAnswers[i]==x:
                        rate["correct"]+=1
                    else:
                        rate["incorrect"]+=1

            return rate
            
                        
            
        
        mylist=[]
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT quizID,userAnswers from Results where userID={} """.format(userID))
        datas=cur.fetchall()

        from ast import literal_eval

        connection.close()
        for x in datas:
            print(x)
            mylist.append([self.tdm.getCategory(x[0]),getRate(userID,x[0],literal_eval(x[1]))])
            
        #print("mylist",mylist)
            
        return mylist

    def getQuizAndRate(self,userID):
        def getRate(userID,quizID,answers):
            correctAnswers=self.tdm.getCorrectAnswers(quizID)
            rate={"correct":0,"incorrect":0,"notAnswered":0}
            for i,x in enumerate(answers):

                if x==0:
                    rate["notAnswered"]+=1
                else:
                    if correctAnswers[i]==x:
                        rate["correct"]+=1
                    else:
                        rate["incorrect"]+=1

            return rate
            
                        
            
        
        mylist=[]
        connection=sqlite3.connect(self.filename)
        cur=connection.cursor()
        cur.execute(""" SELECT quizID,userAnswers from Results where userID={} """.format(userID))
        datas=cur.fetchall()

        from ast import literal_eval

        connection.close()
        for x in datas:
            quizID=x[0]
            userAnswers=literal_eval(x[1])
            quiz=self.tdm.getTest(x[0])
            for i,answer in enumerate(userAnswers):
                quiz.questions[i].selected=answer
            
            rate=getRate(userID,quizID,userAnswers)
            print(x)
            mylist.append([quiz,rate])
            
        #print("mylist",mylist)
            
        return mylist

        
#rdm= ResultsDatabaseManager()
#print(rdm.getCategoryAndRates(1))
        


