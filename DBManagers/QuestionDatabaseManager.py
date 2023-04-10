import sqlite3

import sys
sys.path.insert(0, "..")

from CustomDataTypes import FourChoiceQuestion,DatabaseFourChoiceQuestion


class QuestionDatabaseManager:
    filename="database.sqlite3"
    def __init__(self):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""
        CREATE TABLE if not exists Question (
            questionID  INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
            quizID      INTEGER REFERENCES Quiz ON DELETE SET NULL,
            question    TEXT    NOT NULL,
            choice1     TEXT    NOT NULL,
            choice2     TEXT    NOT NULL,
            choice3     TEXT    NOT NULL,
            choice4     TEXT    NOT NULL,
            correct     INT     NOT NULL,
            imageSource TEXT
        );




""")
        connection.commit()
        connection.close()

    def resetTable(self):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""

       CREATE TABLE Question (
            questionID  INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
            quizID      INTEGER REFERENCES Quiz ON DELETE SET NULL,
            question    TEXT    NOT NULL,
            choice1     TEXT    NOT NULL,
            choice2     TEXT    NOT NULL,
            choice3     TEXT    NOT NULL,
            choice4     TEXT    NOT NULL,
            correct     INT     NOT NULL,
            imageSource TEXT
        );


""")
        connection.commit()
        connection.close()
        
        


    def getQuestionsByQuizID(self,quizID):
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        questions=[DatabaseFourChoiceQuestion(*question[2:8],question[0],question[1],question[8]) for question in ex.execute("select * from Question where quizID={}".format(quizID))] 
        connection.close()
        return questions



    def addQuestion(self,quizID:int,question:FourChoiceQuestion):#finished
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        add="insert into Question ( quizID ,question, choice1, choice2,choice3,choice4,correct,imageSource) values (?,?,?,?,?,?,?,?)"
        print(quizID, question.question, question.choice1,question.choice2,question.choice3,question.choice4,question.selected,question.imageSource,sep="-*-")
        ex.execute(add,(quizID, question.question, question.choice1,question.choice2,question.choice3,question.choice4,question.selected,question.imageSource))
        connection.commit()
        connection.close()

    def deleteQuestionByQuestionID(self,questionID):#finished
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("delete from Question where questionID={}".format(questionID))
        connection.commit()
        connection.close()

    def deleteQuestionByQuizID(self,QuizID):#finished
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("delete from Question where QuizID={}".format(QuizID))
        connection.commit()
        connection.close()

    def updateQuestion(self,question:DatabaseFourChoiceQuestion):#finished
        connection=sqlite3.connect(self.filename)
        ex=connection.cursor()
        ex.execute("""UPDATE Question set question="{}",choice1="{}",choice2="{}",choice3="{}",choice4="{}",correct={},imageSource="{}" where questionID={}""".format(question.question,question.choice1,question.choice2,question.choice3,question.choice4,question.correct,question.imageSource,question.questionID))

        connection.commit()
        connection.close()



#questionDatabaseManager=QuestionDatabaseManager()
"""questions=questionDatabaseManager.getQuestionsByQuizID(33)
for question in questions:
    print(question.question)"""

