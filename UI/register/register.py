from PyQt5 import QtCore, QtGui, QtWidgets


class Register_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(540, 470)
        self.setMaximumSize(QtCore.QSize(584, 555))
        font = QtGui.QFont()
        font.setKerning(False)
        self.setFont(font)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: #DFF6FF;\n"
"}\n"
"\n"
"\n"
"#inputName,#inputSurname,#inputEmail,#inputPassword,#inputPasswordAgain{ \n"
"border: 2px solid \"black\";\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
"}\n"
"\n"
"#inputName:hover{\n"
"border:1px solid \"black\";\n"
"}\n"
"#inputSurname:hover{\n"
"border:1px solid \"black\";\n"
"}\n"
"#inputEmail:hover{\n"
"border:1px solid \"black\";\n"
"}\n"
"#inputPassword:hover{\n"
"border:1px solid \"black\";\n"
"}\n"
"#inputPasswordAgain:hover{\n"
"border:1px solid \"black\";\n"
"}\n"
"\n"
"\n"
"#inputName:focus{\n"
"border:2px solid \"cyan\";\n"
"}\n"
"#inputSurname:focus{\n"
"border:2px solid \"cyan\";\n"
"}\n"
"#inputEmail:focus{\n"
"border:2px solid \"cyan\";\n"
"}\n"
"#inputPassword:focus{\n"
"border:2px solid \"cyan\";\n"
"}\n"
"#inputPasswordAgain:focus{\n"
"border:2px solid \"cyan\";\n"
"}\n"
"\n"
"\n"
"\n"
"#inputPassword{\n"
"text-decoration: hidden;\n"
"}\n"
"#title{\n"
"background-color: #06283D;\n"
"border: 2px solid #256D85;\n"
"border-radius: 10px;\n"
"font-size: 34px;\n"
"padding-top: 17px;\n"
"color: \"white\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#registerButton{\n"
"color: #fff;\n"
"background-color: #06283D;\n"
"padding: 10px;\n"
"border-radius: 11px;\n"
"border: 2px solid #fff;\n"
"}\n"
"\n"
"#registerButton:hover{\n"
"color:#256D85;\n"
"background-color: #fff;\n"
"border: 2px solid #256D85;\n"
"}\n"
"#registerButton:pressed{\n"
"color: #fff;\n"
"background-color: #06283D;\n"
"padding: 10px;\n"
"border-radius: 11px;\n"
"border: 2px solid #fff;\n"
"}\n"
"\n"
"\n"
"#loginButton{\n"
"border: none;\n"
"text-align:center;\n"
"padding-left: 2px;\n"
"font-size:15px;\n"
"color:\"black\";\n"
"}\n"
"\n"
"#loginButton:hover{\n"
"border: none;\n"
"color:#256D85;\n"
"}\n"
"#loginButton:pressed{\n"
"border: none;\n"
"font-size:15px;\n"
"color:\"black\";\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputName = QtWidgets.QLineEdit(self.frame)
        self.inputName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputName.setStyleSheet("")
        self.inputName.setInputMask("")
        self.inputName.setText("")
        self.inputName.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputName.setClearButtonEnabled(False)
        self.inputName.setObjectName("inputName")
        self.horizontalLayout.addWidget(self.inputName)
        self.inputSurname = QtWidgets.QLineEdit(self.frame)
        self.inputSurname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputSurname.setStyleSheet("")
        self.inputSurname.setInputMask("")
        self.inputSurname.setText("")
        self.inputSurname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputSurname.setClearButtonEnabled(False)
        self.inputSurname.setObjectName("inputSurname")
        self.horizontalLayout.addWidget(self.inputSurname)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.inputEmail = QtWidgets.QLineEdit(self.frame)
        self.inputEmail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputEmail.setStyleSheet("")
        self.inputEmail.setInputMask("")
        self.inputEmail.setText("")
        self.inputEmail.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputEmail.setClearButtonEnabled(False)
        self.inputEmail.setObjectName("inputEmail")
        self.verticalLayout_2.addWidget(self.inputEmail)
        self.inputPassword = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setKerning(False)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout_2.addWidget(self.inputPassword)
        self.inputPasswordAgain = QtWidgets.QLineEdit(self.frame)
        self.inputPasswordAgain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputPasswordAgain.setStyleSheet("")
        self.inputPasswordAgain.setInputMask("")
        self.inputPasswordAgain.setText("")
        self.inputPasswordAgain.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPasswordAgain.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputPasswordAgain.setClearButtonEnabled(False)
        self.inputPasswordAgain.setObjectName("inputPasswordAgain")
        self.verticalLayout_2.addWidget(self.inputPasswordAgain)
        self.registerButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_2.addWidget(self.registerButton)
        self.loginButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("text-align:center;")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.verticalLayout_3.addWidget(self.statusBar)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.title.setText(_translate("self", "QUIZ AUTOMATION"))
        self.inputName.setPlaceholderText(_translate("self", "Name"))
        self.inputSurname.setPlaceholderText(_translate("self", "Surname"))
        self.inputEmail.setPlaceholderText(_translate("self", "Email"))
        self.inputPassword.setPlaceholderText(_translate("self", "Password"))
        self.inputPasswordAgain.setPlaceholderText(_translate("self", "Confirm Password"))
        self.registerButton.setText(_translate("self", "Register"))
        self.loginButton.setText(_translate("self", "Log In"))
