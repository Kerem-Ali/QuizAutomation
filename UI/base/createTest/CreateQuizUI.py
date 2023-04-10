from PyQt5 import QtCore, QtGui, QtWidgets
from .inputQuestion import InputQuestion


from CustomDataTypes import Test,FourChoiceQuestion



class CreateQuizUI(QtWidgets.QWidget):
    def __init__(self,user,quizName,category,numberOfQuestions,tdm):
        self.user=user
        super().__init__()
        
        self.quizName=quizName
        self.category=category
        self.numberOfQuestions=numberOfQuestions

        self.tdm=tdm
        
        self.quiz=None
        self.currentIndex=0


        self.setGeometry(QtCore.QRect(120, 10, 531, 531))
        self.setObjectName("mainWidget")
        
        self.setStyleSheet("#mainWidget{\nbackground-color:rgb(0,140,140);\n}")
        
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self)
        #self.frame_2.setStyleSheet("background-color: rgb(166, 184, 190);\n""border-radius: 20px;\n")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.testName = QtWidgets.QLabel(self.frame)
        self.testName.setObjectName("testName")
        self.horizontalLayout_4.addWidget(self.testName)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.testCategory = QtWidgets.QLabel(self.frame)
        self.testCategory.setObjectName("testCategory")
        self.horizontalLayout_5.addWidget(self.testCategory)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.questionTop = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.questionTop.setFont(font)
        self.questionTop.setObjectName("questionTop")
        self.horizontalLayout.addWidget(self.questionTop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        
        #quizWidget
        self.widget =InputQuestion()
        self.widget.setMinimumSize(QtCore.QSize(400, 350))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previousQ = QtWidgets.QPushButton(self.frame_2)
        self.previousQ.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousQ.sizePolicy().hasHeightForWidth())
        self.previousQ.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.previousQ.setFont(font)
        self.previousQ.setStyleSheet("QPushButton{\nbackground-color:rgb(170, 224, 230);\nborder-radius: 5px\n""}""*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
        self.previousQ.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/short-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousQ.setIcon(icon)
        self.previousQ.setIconSize(QtCore.QSize(40, 40))
        self.previousQ.setObjectName("previousQ")
        self.horizontalLayout_2.addWidget(self.previousQ)
        self.nextQ = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextQ.sizePolicy().hasHeightForWidth())
        self.nextQ.setSizePolicy(sizePolicy)
        self.nextQ.setStyleSheet("QPushButton{\nbackground-color:rgb(170, 224, 230);\nborder-radius: 5px\n""}""*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
        self.nextQ.setText("")
        icon1 = QtGui.QIcon()

        
        icon1.addPixmap(QtGui.QPixmap("../icons/short-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextQ.setIcon(icon1)
        self.nextQ.setIconSize(QtCore.QSize(40, 40))
        self.nextQ.setObjectName("nextQ")
        self.horizontalLayout_2.addWidget(self.nextQ)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.addQuiz = QtWidgets.QPushButton(self.frame_2)
        self.addQuiz.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addQuiz.setFont(font)
        self.addQuiz.setStyleSheet("QPushButton{\n""background-color:\"blue\";\n""color:\"white\";\n""}\n""*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
        self.addQuiz.setObjectName("finish")
        self.verticalLayout_2.addWidget(self.addQuiz)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        

        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.previousQ.clicked.connect(self.previous)
        self.nextQ.clicked.connect(self.next)
        self.addQuiz.clicked.connect(self.add_quiz)


        questions=[]
        for x in range(self.numberOfQuestions):
            question=FourChoiceQuestion("Question Here","answer1","answer2","answer3","answer4",1)
            question.selected=1
            questions.append(question)

        self.setupQuiz(Test(testName=self.quizName,category=self.category,
                            questions=questions,
                            authorID=self.user.ID))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("self", "Test Name:"))
        self.testName.setText(_translate("self", "null"))
        self.label.setText(_translate("self", "Category:"))
        self.testCategory.setText(_translate("self", "null"))
        self.questionTop.setText(_translate("self", "1/10"))
        self.addQuiz.setText(_translate("self", "Add Quiz"))

    
    def previous(self):
        self.setupChanges()
        if self.currentIndex!=0:
            self.currentIndex-=1
            self.setupQuestion()

    def next(self):
        self.setupChanges()
        if self.currentIndex!=len(self.quiz.questions)-1:
            self.currentIndex+=1
            self.setupQuestion()



    def setupQuiz(self,quiz):
        self.quiz=quiz
        self.currentIndex=0
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_3.setText(_translate("self", "Test Name:"))
        self.testName.setText(_translate("self", f"{self.quiz.testName}"))
        self.label.setText(_translate("self", "Category:"))
        self.testCategory.setText(_translate("self", f"{self.quiz.category}"))
        self.questionTop.setText(_translate("self", f"{self.currentIndex+1}/{len(self.quiz.questions)}"))
        self.addQuiz.setText(_translate("self", "Add Quiz"))
        self.setupQuestion()


    def setupQuestion(self):
        _translate = QtCore.QCoreApplication.translate
        self.questionTop.setText(_translate("self", f"{self.currentIndex+1}/{len(self.quiz.questions)}"))

        self.widget.setup(self.quiz.questions[self.currentIndex])

        for choice in self.widget.rdbtns:
            choice.toggled.connect(self.change_selected)

    def change_selected(self):
        self.widget.selected=self.sender()
        self.quiz.questions[self.currentIndex].selected=  self.widget.rdbtns.index(self.widget.selected)+1
        print("dogru cevap",self.widget.rdbtns.index(self.widget.selected))


    def setupChanges(self):
        self.quiz.questions[self.currentIndex].question=self.widget.inputQuestion.toPlainText()
        self.quiz.questions[self.currentIndex].choice1=self.widget.answer1Input.text()
        self.quiz.questions[self.currentIndex].choice2=self.widget.answer2Input.text()
        self.quiz.questions[self.currentIndex].choice3=self.widget.answer3Input.text()
        self.quiz.questions[self.currentIndex].choice4=self.widget.answer4Input.text()
        self.quiz.questions[self.currentIndex].selected=self.widget.rdbtns.index(self.widget.selected)+1

        self.quiz.questions[self.currentIndex].imageSource=self.widget.filename
        
        print(self.quiz.questions[self.currentIndex].__dict__)
        


    def add_quiz(self):
        import os
        here=os.getcwd()
        nextID=self.tdm.getNextQuizID()
        os.chdir("../questionImages")
        
        import shutil
        
        self.setupChanges()

        created=False

        for question in self.quiz.questions:
            if question.imageSource!="":
                if (not created) and (not os.path.exists(str(nextID))):
                    os.mkdir(str(nextID))
                    created=True
                    os.chdir(str(nextID))
                
                    
                    
                old=str(question.imageSource)
                question.imageSource=question.imageSource.replace("\\","/")
                question.imageSource=question.imageSource [question.imageSource.rindex("/")+1:]

                print("hereishere",os.getcwd())

                shutil.copy(old,os.getcwd())
            

        os.chdir(here)
        self.tdm.addTestByTest(self.quiz)
        self.close()
        
        


        
        
        

