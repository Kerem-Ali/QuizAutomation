from PyQt5 import QtCore, QtGui, QtWidgets
from .QuestionUI import QuestionUI
from .schemes import QUESTION_STYLE

class QuestionUIReview(QuestionUI):
    def __init__(self):
        super().__init__()
        self.correctColor="rgb(0,255,0)"
        self.wrongColor="rgb(255,0,0)"
        self.noAnswerColor="rgb(75,75,75)"

    def setup(self,question):
        self.question=question
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Question", "Question"))
        text=QUESTION_STYLE.format(self.question.question)
        self.question_text.setHtml(_translate("Question",text))
        if question.imageSource!="":
            self.image.setStyleSheet("border-image:url(../questionImages/{}/{});".format(question.quizID,question.imageSource))
        else:
            self.image.setStyleSheet("")

        for i,btn in enumerate(self.btns):
            btn.setStyleSheet("")
            btn.setText(_translate("Question", question.choices[i]))
        
        print(self.question.selected)
        print(self.question.correct)
        if self.question.selected==self.question.correct:
            self.btns[self.question.correct-1].setStyleSheet("background-color:{};".format(self.correctColor))
        else:
            if self.question.selected==0:
                self.btns[self.question.correct-1].setStyleSheet("background-color:{};".format(self.noAnswerColor))
            else:
                print("here")
                self.btns[self.question.correct-1].setStyleSheet("background-color:{};".format(self.correctColor))
                self.btns[self.question.selected-1].setStyleSheet("background-color:{};".format(self.wrongColor))
                
            
