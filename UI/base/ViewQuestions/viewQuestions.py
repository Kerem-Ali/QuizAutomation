from PyQt5 import QtCore, QtGui, QtWidgets
from .QuestionWidget import QuestionWidget

class ViewQuestions(QtWidgets.QWidget):
    def __init__(self,testmanager,accmanager,resultmanager,user):
        self.testmanager=testmanager
        self.accmanager=accmanager
        self.resultmanager=resultmanager
        self.user=user
        self.tests=self.testmanager.getTests()
        super().__init__()

        self.setObjectName("ViewQuestions")
        self.setStyleSheet("*\n"
"{"
"background-color: rgb(0,140,140);\n"

"color:rgb(255,255,255);\n"
"}"
"QPushButton"
"{"
"background-color:rgb(200,200,50);"
"border:2px solid rgb(50,50,200);\n"
"height:15px;\n"
"}"
"QPushButton:hover"
"{"
"background-color:rgb(200,200,50);"
"border:2px solid rgb(100,100,150);\n"
"height:15px;\n"
"}"
        )
        
        
        self.horizontalLayout=QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("base")


        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(140, 93, 481, 351))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 316))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        print("tests",self.tests)
        for test in self.tests:
            self.verticalLayout.addWidget(QuestionWidget(test,self.accmanager,self.resultmanager,self.user) )
            
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.horizontalLayout.addWidget(self.groupBox)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.groupBox.setTitle(_translate("self", "Questions"))

