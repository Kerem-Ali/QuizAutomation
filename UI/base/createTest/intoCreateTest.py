from PyQt5 import QtCore, QtGui, QtWidgets


class IntoCreateTest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(QtCore.QRect(280, 210, 248, 121))
        self.setObjectName("introInput")
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
"QLineEdit"
"{"
"color:rgb(0,0,0);\n"
"background-color:rgb(255,255,255);"
"border:2px solid rgb(50,50,200);\n"
"height:15px;\n"
"}"

        )
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FormLayout = QtWidgets.QFormLayout()
        self.FormLayout.setObjectName("FormLayout")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setObjectName("label_4")
        self.FormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.testName = QtWidgets.QLineEdit(self)
        self.testName.setObjectName("testName")
        self.FormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.testName)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setObjectName("label_5")
        self.FormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.categoryInput = QtWidgets.QComboBox(self)
        self.categoryInput.setObjectName("categoryInput")
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.categoryInput.addItem("")
        self.FormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.categoryInput)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.FormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.questionNumber = QtWidgets.QSpinBox(self)
        self.questionNumber.setWrapping(False)
        self.questionNumber.setMinimum(5)
        self.questionNumber.setMaximum(25)
        self.questionNumber.setProperty("value", 10)
        self.questionNumber.setObjectName("questionNumber")
        self.FormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.questionNumber)
        self.verticalLayout.addLayout(self.FormLayout)
        self.OKbtn = QtWidgets.QPushButton(self)
        self.OKbtn.setObjectName("OKbtn")
        self.verticalLayout.addWidget(self.OKbtn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_4.setText(_translate("self", "Test name:"))
        self.label_5.setText(_translate("self", "Category:"))
        self.categoryInput.setItemText(0, _translate("self", "Personal"))
        self.categoryInput.setItemText(1, _translate("self", "Math"))
        self.categoryInput.setItemText(2, _translate("self", "Lecture"))
        self.categoryInput.setItemText(3, _translate("self", "General Knowledge"))
        self.categoryInput.setItemText(4, _translate("self", "Computer Science"))
        self.label_2.setText(_translate("self", "Question number: "))
        self.OKbtn.setText(_translate("self", "OK"))
