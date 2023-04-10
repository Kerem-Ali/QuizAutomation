

from .CreateQuizUI import CreateQuizUI
from .intoCreateTest import IntoCreateTest


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class BaseCreateQuizUI(QtWidgets.QWidget):
    def __init__(self,tdm,rdm,user):
        self.tdm=tdm
        self.rdm=rdm
        self.user=user
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setIntro()

    def deleteAll(self):
        while self.layout().count():
            child =  self.layout().takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()

    def setIntro(self):
        self.deleteAll()
        ict=IntoCreateTest()
        

        testname=""
        numberOfQuestions=0
        category=""
        def get_datas():

            
            nonlocal testname
            nonlocal numberOfQuestions
            nonlocal category

            testname=ict.testName.text()
            numberOfQuestions=ict.questionNumber.value()
            print(numberOfQuestions,type(numberOfQuestions))
            category=ict.categoryInput.currentText()

            self.setCreating(testname,category,numberOfQuestions)

        ict.OKbtn.clicked.connect(get_datas)        
            
        self.layout().addWidget(ict )
        
        

    def setCreating(self,quizName,category,numberOfQuestions):
        #self.deleteAll()
        #self.layout().addWidget( CreateQuizUI(self.user,quizName,category,numberOfQuestions,self.tdm))

        self.creating = CreateQuizUI(self.user,quizName,category,numberOfQuestions,self.tdm)
        self.creating.setGeometry(100,100,600,600)
        self.creating.show()


        
