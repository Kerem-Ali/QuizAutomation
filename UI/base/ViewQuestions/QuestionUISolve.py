from PyQt5 import QtCore, QtGui, QtWidgets
from .QuestionUI import QuestionUI
from .schemes import QUESTION_STYLE

class QuestionUISolve(QuestionUI):
    def __init__(self):
        super().__init__()
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:gray;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-color:rgb(218, 241, 248);\n"
"border: 2px solid;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(201, 221, 227);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(150, 236, 244);\n"
"}")


    def setup(self,question):
        import os
        print("alarm",os.getcwd())
        self.question=question
        self.selected=None if self.question.selected==0 else self.btns[self.question.selected-1]
        #print("selected",self.selected)
        #print("selectedquestion",self.question.selected)
        
        _translate = QtCore.QCoreApplication.translate
        text=QUESTION_STYLE.format(self.question.question)
        self.question_text.setHtml(_translate("Question",text))
        if question.imageSource=="":
            self.image.clear()
            self.image.setPixmap(QtGui.QPixmap())
            self.image.update()
            self.image.setStyleSheet("")
        else:
            self.image.setStyleSheet("border-image:url(../questionImages/{}/{})".format(question.quizID,question.imageSource))
            print(question.quizID,question.imageSource)
            #pixmap=QtGui.QPixmap("C:/Users/Kerem_Ali/Desktop/QuizAutomation/questionImages/{}/{}".format(question.quizID,question.imageSource))
            #pixmap=pixmap.scaled(self.image.width(),self.image.height())
            #self.image.setPixmap(pixmap)
            #self.image.setMinimumSize(1,1)
            
            #self.image.setStyleSheet("border-image:url(C:/Users/Kerem_Ali/Desktop/QuizAutomation/questionImages/{}/{});".format(question.quizID,question.imageSource))
            
    

        for i,btn in enumerate(self.btns):
                btn.setText(_translate("Question", question.choices[i]))
                btn.clicked.connect(self.make_selected)
                btn.setStyleSheet("QPushButton[selected='0']\n"
                    "{\n"
                    "border-radius: 13px;\n"
                    "background-color:rgb(218, 241, 248);\n"
                    "border: 2px solid;\n"
                    "}\n"
                    "QPushButton[selected='0']:hover\n"
                    "{\n"
                    "background-color:rgb(201, 221, 227);\n"
                    "}\n"
                    "\n"
                    "QPushButton[selected='0']:pressed{\n"
                    "background-color: rgb(150, 236, 244);\n"
                    "}"
                    "QPushButton[selected='1']\n"
                    "{\n"
                    "border-radius: 13px;\n"
                    "background-color:rgb(0, 0, 255);\n"
                    "border: 2px solid;\n"
                    "}\n")
                btn.setProperty("selected", "0")
                btn.style().polish(btn)

        if self.selected!=None:
            self.selected.setProperty("selected", "1")
            self.selected.style().polish(self.selected)

    def make_selected(self):
        sender=self.sender()
        sendername=sender.objectName()
        if self.selected==sender:
            self.selected.setProperty("selected", "0")
            self.selected.style().polish(self.selected)
            self.selected=None
            self.question.selected=0
            print("selectedquestionin",self.question.selected)
            sender.clicked.disconnect()
            self.setup(self.question)
            
        elif self.selected==None:
            self.selected=sender
            self.selected.setProperty("selected", "1")
            self.selected.style().polish(self.selected)
            self.question.selected=self.btns.index(self.selected)+1
            print("selectedquestionin",self.question.selected)
            sender.clicked.disconnect()
            self.setup(self.question)

        elif self.selected!=None:
            self.selected.setProperty("selected", "0")
            self.selected.style().polish(self.selected)
            self.selected=sender
            self.selected.setProperty("selected", "1")
            self.selected.style().polish(self.selected)
            self.question.selected=self.btns.index(self.selected)+1
            print("selectedquestionin",self.question.selected)
            sender.clicked.disconnect()
            self.setup(self.question)
        print("selected",self.selected)
        print("selectedquestion",self.question.selected)

        print("imagewidth",self.image.width())
        print("imageheight",self.image.height())

        
        
        
