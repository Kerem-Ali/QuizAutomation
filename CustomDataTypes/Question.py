from abc import ABC,abstractmethod
class BaseQuestion(ABC):
    @property
    @abstractmethod
    def question(self):
        pass

    @property
    @abstractmethod
    def correctAnswer(self):
        pass





class FCQ(BaseQuestion):
    """A Question Type which has one valid answer and total 4 options"""
    
    def __init__(self,question:str,choice1:str,choice2:str,choice3:str,choice4:str,correct:int,imageSource=""):

        self.__question=question
        
        self.__choice1=choice1
        self.__choice2=choice2
        self.__choice3=choice3
        self.__choice4=choice4
        
        self.__correct=correct
        
        self.__imageSource=imageSource

        self.__selected=0

    @property
    def selected(self):
        return self.__selected

   

    @property
    def question(self):
        return self.__question
        

    @property
    def choice1(self) -> str:
        return self.__choice1

    @property
    def choice2(self) -> str:
        return self.__choice2

    @property
    def choice3(self) -> str:
        return self.__choice3

    @property
    def choice4(self) -> str:
        return self.__choice4

    @property
    def choices(self) -> list:
        return [self.__choice1,self.__choice2,self.__choice3,self.__choice4]

    @property
    def correct(self):
        return self.__correct

    @property
    def correctAnswer(self):
        return self.choices[self.__correct-1]

    @property
    def imageSource(self):
        return self.__imageSource


class FourChoiceQuestion(FCQ):
    """A Question Type which has one valid answer and total 4 options"""
    
    def __init__(self,question:str,choice1:str,choice2:str,choice3:str,choice4:str,correct:int,imageSource=""):

        self.__question=question
        
        self.__choice1=choice1
        self.__choice2=choice2
        self.__choice3=choice3
        self.__choice4=choice4
        
        self.__correct=correct
        
        self.__imageSource=imageSource

        self.__selected=0

    @property
    def selected(self):
        return self.__selected

   

    @property
    def question(self):
        return self.__question
        

    @property
    def choice1(self) -> str:
        return self.__choice1

    @property
    def choice2(self) -> str:
        return self.__choice2

    @property
    def choice3(self) -> str:
        return self.__choice3

    @property
    def choice4(self) -> str:
        return self.__choice4

    @property
    def choices(self) -> list:
        return [self.__choice1,self.__choice2,self.__choice3,self.__choice4]

    @property
    def correct(self):
        return self.__correct

    @property
    def correctAnswer(self):
        return self.choices[self.__correct-1]

    @property
    def imageSource(self):
        return self.__imageSource

    @question.setter
    def question(self,value):
        if isinstance(value,str):
            self.__question=value


    @choice1.setter
    def choice1(self,value):
        if isinstance(value,str):
            self.__choice1=value

    @choice2.setter
    def choice2(self,value):
        if isinstance(value,str):
            self.__choice2=value

    @choice3.setter
    def choice3(self,value):
        if isinstance(value,str):
            self.__choice3=value

    @choice4.setter
    def choice4(self,value):
        if isinstance(value,str):
            self.__choice4=value

    @correct.setter
    def correct(self,value):
        if isinstance(value,str):
            self.__correct=value

    @imageSource.setter
    def imageSource(self,value):
        if isinstance(value,str):
            self.__imageSource=value


    @selected.setter
    def selected(self,value):
        if 0<=value<=4:
            self.__selected=value
    






class DatabaseFourChoiceQuestion(FCQ):
    def __init__(self,question:str,choice1:str,choice2:str,choice3:str,choice4:str,correct:int,questionID,quizID,imageSource:str=""):
        super().__init__(question,choice1,choice2,choice3,choice4,correct,imageSource)
        self.__questionID=questionID
        self.__quizID=quizID

        self.__question=question
        
        self.__choice1=choice1
        self.__choice2=choice2
        self.__choice3=choice3
        self.__choice4=choice4
        
        self.__correct=correct
        
        self.__imageSource=imageSource

        self.__selected=0


    @property
    def question(self):
        return self.__question
    
    @property
    def questionID(self):
        return self.__questionID

    @property
    def quizID(self):
        return self.__quizID

    @property
    def selected(self):
        return self.__selected

   

    
        

    @property
    def choice1(self) -> str:
        return self.__choice1

    @property
    def choice2(self) -> str:
        return self.__choice2

    @property
    def choice3(self) -> str:
        return self.__choice3

    @property
    def choice4(self) -> str:
        return self.__choice4

    @property
    def choices(self) -> list:
        return [self.__choice1,self.__choice2,self.__choice3,self.__choice4]

    @property
    def correct(self):
        return self.__correct

    @property
    def correctAnswer(self):
        return self.choices[self.__correct-1]

    @property
    def imageSource(self):
        return self.__imageSource


    @selected.setter
    def selected(self,value):
        if 0<=value<=4:
            self.__selected=value
    





if __name__=="__main__":  
    try:
        myq=DatabaseFourChoiceQuestion("What is the logic","Kerem","Ali","Avci","Avcioglu",1,1,1)

        print(myq.question)
        print(myq.choices)

    except Exception as ex:
        print(ex)

