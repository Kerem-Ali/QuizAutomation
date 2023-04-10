from PyQt5 import QtCore, QtGui, QtWidgets

from .QuizUI import QuizUI


class QuestionWidget(QtWidgets.QWidget):
    def __init__(self,test,accManager,rdm,user):
        self.test=test

        self.accManager=accManager

        self.rdm=rdm
        self.user=user
        
        super().__init__()
        self.setGeometry(QtCore.QRect(90, 10, 531, 41))
        self.setObjectName("QuestionWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.openQuiz)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", self.test.testName))
        self.label_2.setText(_translate("Form", self.test.date_created))
        self.label_3.setText(_translate("Form", self.accManager.IDtoName(self.test.authorID)))
        self.pushButton.setText(_translate("Form", "Solve"))

    def openQuiz(self):
        self.quiz = QuizUI(self.rdm,self.user)
        self.quiz.setGeometry(100,100,600,600)
        self.quiz.setupQuiz(self.test)


        self.quiz.show()
    








        
