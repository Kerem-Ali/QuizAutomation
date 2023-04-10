from PyQt5 import QtCore, QtGui, QtWidgets


class Login_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(540, 467)
        self.setMaximumSize(QtCore.QSize(540, 470))
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
"#inputEmail,#inputPassword{ \n"
"border: 2px solid;\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
"}\n"
"\n"
"#inputPassword:hover{\n"
"border:1px solid \"black\";\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
"}\n"
"#inputEmail:hover{\n"
"border:1px solid \"black\";\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
"}\n"
"\n"
"#inputEmail:focus{\n"
"border:2px solid \"cyan\";\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
"}\n"
"#inputPassword:focus{\n"
"border:2px solid \"cyan\";\n"
"border-radius: 8px;\n"
"padding: 10px;\n"
"margin-bottom:10px;\n"
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
"#loginButton{\n"
"color: #fff;\n"
"background-color: #06283D;\n"
"padding: 10px;\n"
"border-radius: 11px;\n"
"border: 2px solid #fff;\n"
"}\n"
"\n"
"#loginButton:hover{\n"
"color:#256D85;\n"
"background-color: #fff;\n"
"border: 2px solid #256D85;\n"
"}\n"
"#loginButton:pressed{\n"
"color: #fff;\n"
"background-color: #06283D;\n"
"padding: 10px;\n"
"border-radius: 11px;\n"
"border: 1px solid #fff;\n"
"}\n"
"\n"
"\n"
"#registerButton{\n"
"border: none;\n"
"text-align:center;\n"
"font-size:15px;\n"
"color:\"black\";\n"
"}\n"
"\n"
"#registerButton:hover{\n"
"border: none;\n"
"color:#256D85;\n"
"}\n"
"#registerButton:pressed{\n"
"border: none;\n"
"font-size:15px;\n"
"color:\"black\";\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputEmail = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputEmail.sizePolicy().hasHeightForWidth())
        self.inputEmail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        self.inputEmail.setFont(font)
        self.inputEmail.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.inputEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputEmail.setStyleSheet("")
        self.inputEmail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhSensitiveData)
        self.inputEmail.setInputMask("")
        self.inputEmail.setText("")
        self.inputEmail.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputEmail.setClearButtonEnabled(False)
        self.inputEmail.setObjectName("inputEmail")
        self.verticalLayout.addWidget(self.inputEmail)
        self.inputPassword = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPassword.sizePolicy().hasHeightForWidth())
        self.inputPassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setKerning(False)
        self.inputPassword.setFont(font)
        self.inputPassword.setStyleSheet("")
        self.inputPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.verticalLayout.addWidget(self.inputPassword)
        self.loginButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.registerButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.registerButton.setFont(font)
        self.registerButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.registerButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.title, 0, 0, 1, 1)
        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.gridLayout_3.addWidget(self.statusBar, 2, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.inputEmail.setPlaceholderText(_translate("self", "Email"))
        self.inputPassword.setPlaceholderText(_translate("self", "Password"))
        self.loginButton.setText(_translate("self", "Log In"))
        self.registerButton.setText(_translate("self", "Register"))
        self.title.setText(_translate("self", "QUIZ AUTOMATION"))
