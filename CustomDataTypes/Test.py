from .Question import FourChoiceQuestion,DatabaseFourChoiceQuestion


    
        
class Test():
    def __init__(self,testName:str,category:str,questions:list,authorID:int):
        self.__testName=testName
        self.__questions=questions
        self.__category=category
        self.__authorID=authorID

    @property
    def testName(self):
        return self.__testName

    @property
    def questions(self):
        return self.__questions

    @property
    def category(self):
        return self.__category

    @property
    def authorID(self):
        return self.__authorID

class DatabaseTest(Test):
    def __init__(self,quizID:int,testName:str,category:str,date_created:str,authorID:int,plays:int,questions:list):
        super().__init__(testName,category,questions,authorID)
        self.__quizID=quizID
        self.__testName=testName
        self.__date_created=date_created
        self.__plays=plays

    @property
    def quizID(self):
        return self.__quizID
    @property
    def date_created(self):
        return self.__date_created
    @property
    def plays(self):
        return self.__plays
    

    


    
