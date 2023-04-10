from PyQt5 import QtCore, QtGui, QtWidgets
from .ProfilePhoto import ProfilePhoto
from .NavBar import NavBar
class Header(QtWidgets.QWidget):
    def __init__(self,dbUser,baseUI):
        self.dbUser=dbUser

        self.baseUI=baseUI
        
        
        super().__init__()
        self.setGeometry(QtCore.QRect(20, 10, 771, 93))
        self.setObjectName("header")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.head = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.head.sizePolicy().hasHeightForWidth())
        self.head.setSizePolicy(sizePolicy)
        self.head.setMinimumSize(QtCore.QSize(900, 75))
        self.head.setMaximumSize(QtCore.QSize(1362, 75))
        self.head.setStyleSheet("#head{\n"
"\n"
"background-color:rgba(2,2,2,20);\n"
"\n"
"border-bottom-left-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"\n"
"}")
        self.head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.head)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.profile = ProfilePhoto(self.dbUser)
        self.profile.setObjectName("profile")
        self.horizontalLayout_3.addWidget(self.profile)
        self.frame_3 = QtWidgets.QFrame(self.head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.infos = QtWidgets.QVBoxLayout()
        self.infos.setObjectName("infos")
        self.namesurname = QtWidgets.QHBoxLayout()
        self.namesurname.setObjectName("namesurname")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.frame_3)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.userName = QtWidgets.QLabel(self.frame_3)
        self.userName.setObjectName("userName")
        self.horizontalLayout.addWidget(self.userName)
        self.namesurname.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_surname = QtWidgets.QLabel(self.frame_3)
        self.label_surname.setObjectName("label_surname")
        self.horizontalLayout_2.addWidget(self.label_surname)
        self.userSurname = QtWidgets.QLabel(self.frame_3)
        self.userSurname.setObjectName("userSurname")
        self.horizontalLayout_2.addWidget(self.userSurname)
        self.namesurname.addLayout(self.horizontalLayout_2)
        self.infos.addLayout(self.namesurname)
        self.email = QtWidgets.QHBoxLayout()
        self.email.setObjectName("email")
        self.label_email = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)
        self.label_email.setObjectName("label_email")
        self.email.addWidget(self.label_email)
        self.userEmail = QtWidgets.QLabel(self.frame_3)
        self.userEmail.setObjectName("userEmail")
        self.email.addWidget(self.userEmail)
        self.infos.addLayout(self.email)
        self.gridLayout_3.addLayout(self.infos, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.navbar = NavBar()
        self.navbar.setObjectName("navbar")
        self.horizontalLayout_3.addWidget(self.navbar)
        self.title = QtWidgets.QLabel(self.head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(291, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        self.gridLayout.addWidget(self.head, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        for btn in self.navbar.choice_buttons:
            btn.clicked.connect(self.change_UI)


        self.changes=[self.baseUI.setupHome,
                      self.baseUI.setupAbout,
                      self.baseUI.setupViewquestions,
                      self.baseUI.setupCreateQuiz,
                      self.baseUI.setupLeaderboard,
                      self.baseUI.setupSettings,
                      self.baseUI.Quit]


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Name:"))
        self.userName.setText(_translate("Form", f"{self.dbUser.name}"))
        self.label_surname.setText(_translate("Form", "Surname:"))
        self.userSurname.setText(_translate("Form", f"{self.dbUser.surname}"))
        self.label_email.setText(_translate("Form", "email:"))
        self.userEmail.setText(_translate("Form", f"{self.dbUser.email}"))
        self.title.setText(_translate("Form", "QUIZ AUTOMATION"))

    def change_UI(self):
        self.changes[self.navbar.choice_buttons.index(self.sender())]()
