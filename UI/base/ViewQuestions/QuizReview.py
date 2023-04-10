from PyQt5 import QtCore, QtGui, QtWidgets
from .QuestionUIReview import QuestionUIReview


class QuizReview(QtWidgets.QWidget):
    def __init__(self,quiz):
        self.quiz=quiz
        
        super().__init__()
        self.currentIndex=0


        self.setGeometry(QtCore.QRect(120, 10, 531, 531))
        self.setObjectName("mainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setStyleSheet("background-color: rgb(166, 184, 190);\n""border-radius: 20px;\n")
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
        self.widget =QuestionUIReview()
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
        self.previousQ.setStyleSheet("*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
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
        self.nextQ.setStyleSheet("*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
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
        self.finish = QtWidgets.QPushButton(self.frame_2)
        self.finish.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.finish.setFont(font)
        self.finish.setStyleSheet("QPushButton{\n""background-color:\"blue\";\n""color:\"white\";\n""}\n""*:pressed{\n""background-color:rgb(203, 224, 230);\n""border-radius: 5px\n""}")
        self.finish.setObjectName("finish")
        self.verticalLayout_2.addWidget(self.finish)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        

        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.previousQ.clicked.connect(self.previous)
        self.nextQ.clicked.connect(self.next)
        self.finish.clicked.connect(self.commitResult)


        self.setupQuiz()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("self", "Test Name:"))
        self.testName.setText(_translate("self", "null"))
        self.label.setText(_translate("self", "Category:"))
        self.testCategory.setText(_translate("self", "null"))
        self.questionTop.setText(_translate("self", "1/10"))
        self.finish.setText(_translate("self", "OK"))

    
    def previous(self):
        if self.currentIndex!=0:
            self.currentIndex-=1
            self.setupQuestion()

    def next(self):
        if self.currentIndex!=len(self.quiz.questions)-1:
            self.currentIndex+=1
            self.setupQuestion()



    def setupQuiz(self):
        self.currentIndex=0
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_3.setText(_translate("self", "Test Name:"))
        self.testName.setText(_translate("self", f"{self.quiz.testName}"))
        self.label.setText(_translate("self", "Category:"))
        self.testCategory.setText(_translate("self", f"{self.quiz.category}"))
        self.questionTop.setText(_translate("self", f"{self.currentIndex+1}/{len(self.quiz.questions)}"))
        self.finish.setText(_translate("self", "Finish"))
        self.setupQuestion()


    def setupQuestion(self):
        _translate = QtCore.QCoreApplication.translate
        self.questionTop.setText(_translate("self", f"{self.currentIndex+1}/{len(self.quiz.questions)}"))

        self.widget.setup(self.quiz.questions[self.currentIndex])
        for i,x in enumerate(self.quiz.questions):
            print(i+1,self.quiz.questions[i].selected)


    def commitResult(self):

        self.close()
        
        


        
        
        

