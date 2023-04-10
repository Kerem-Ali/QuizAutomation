from PyQt5 import QtCore, QtGui, QtWidgets
from .QuizReview import QuizReview

class QuizResult(QtWidgets.QWidget):
    def __init__(self,quiz,result):
        self.quiz=quiz
        self.result=result
        
        super().__init__()
        
        self.setGeometry(QtCore.QRect(110, 90, 439, 75))
        self.setMaximumSize(QtCore.QSize(16777215, 75))
        self.setObjectName("quizWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.date = QtWidgets.QLabel(self)
        self.date.setObjectName("date")
        self.horizontalLayout.addWidget(self.date)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.incorrect = QtWidgets.QLabel(self)
        self.incorrect.setObjectName("incorrect")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.incorrect)
        self.not_answered = QtWidgets.QLabel(self)
        self.not_answered.setObjectName("not_answered")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.not_answered)
        self.correct = QtWidgets.QLabel(self)
        self.correct.setObjectName("correct")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.correct)
        self.horizontalLayout.addLayout(self.formLayout)
        self.seebtn = QtWidgets.QPushButton(self)
        self.seebtn.setObjectName("seebtn")
        self.horizontalLayout.addWidget(self.seebtn)

        self.seebtn.clicked.connect(self.openResult)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        

    def retranslateUi(self):

        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", f"{self.quiz.testName}"))
        self.date.setText(_translate("self", f"{self.quiz.date_created}"))
        self.label_4.setText(_translate("self", "Correct:"))
        self.label_5.setText(_translate("self", "Incorrect:"))
        self.label_6.setText(_translate("self", "Not Answered:"))
        self.incorrect.setText(_translate("self", f'{self.result["incorrect"]}'))
        self.not_answered.setText(_translate("self", f'{self.result["notAnswered"]}'))
        self.correct.setText(_translate("self", f'{self.result["correct"]}'))
        self.seebtn.setText(_translate("self", "See"))

    def openResult(self):
        self.window=QuizReview(self.quiz)
        self.window.setGeometry(100,100,600,600)
        self.window.show()
