
from PyQt5 import QtCore, QtGui, QtWidgets
import os
print("current",os.getcwd())
#os.chdir("../../../DBManagers")

class Settings(QtWidgets.QWidget):

    def __init__(self,databaseUser,acc_manager,mainUI):
        super().__init__()
        self.user=databaseUser
        self.acc_manager=acc_manager

        self.mainUI=mainUI
        
        self.setObjectName("SettingsWidget")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)
        self.resize(783, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.setFont(font)
        self.setStyleSheet("#self\n"
"{\n"
"background-color: #256D85;\n"
"}\n"
"#frame{\n"
"background-color: #DFF6FF;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(139, 154, 159);\n"
"border-radius: 5px;\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(93, 104, 107)\n"
"}\n"
"#profilePhoto{\n"
"background-color: #fff;\n"
"border-radius: 50px;\n"
"}\n"
"#password_change{\n"
"background-color:\"gray\";\n"
"color:\"white\";}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_5 = QtWidgets.QGridLayout(self)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.header = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.header.setFont(font)
        self.header.setWhatsThis("")
        self.header.setStyleSheet("background-color: rgb(214, 236, 244);")
        self.header.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.header.setWordWrap(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.header.setProperty("icon", icon)
        self.header.setObjectName("header")
        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.userInfo_2 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userInfo_2.setFont(font)
        self.userInfo_2.setStyleSheet("background-color: rgb(214, 236, 244);\n""border-radius: 20px;\n")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("user-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userInfo_2.setIcon(icon1)
        self.userInfo_2.setIconSize(QtCore.QSize(40, 40))
        self.userInfo_2.setObjectName("userInfo_2")
        self.verticalLayout_6.addWidget(self.userInfo_2)
        self.FormLayout_2 = QtWidgets.QFormLayout()
        self.FormLayout_2.setObjectName("FormLayout_2")
        self.name = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.FormLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name)
        self.userName = QtWidgets.QLabel(self.frame_3)
        self.userName.setObjectName("userName")
        self.FormLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userName)
        self.userSurname = QtWidgets.QLabel(self.frame_3)
        self.userSurname.setObjectName("userSurname")
        self.FormLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userSurname)
        self.email = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.FormLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.email)
        self.userEmail = QtWidgets.QLabel(self.frame_3)
        self.userEmail.setObjectName("userEmail")
        self.FormLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userEmail)
        self.surname = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.FormLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surname)
        self.verticalLayout_6.addLayout(self.FormLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.chSurname = QtWidgets.QPushButton(self.frame_3)
        self.chSurname.setMinimumSize(QtCore.QSize(0, 20))
        self.chSurname.setStyleSheet("")
        self.chSurname.setObjectName("chSurname")
        self.gridLayout_4.addWidget(self.chSurname, 1, 2, 1, 1)
        self.nameInput = QtWidgets.QLineEdit(self.frame_3)
        self.nameInput.setMinimumSize(QtCore.QSize(200, 25))
        self.nameInput.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.nameInput.setFont(font)
        self.nameInput.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.gridLayout_4.addWidget(self.nameInput, 0, 1, 1, 1)
        self.chEmail = QtWidgets.QPushButton(self.frame_3)
        self.chEmail.setMinimumSize(QtCore.QSize(0, 20))
        self.chEmail.setStyleSheet("")
        self.chEmail.setObjectName("chEmail")
        self.gridLayout_4.addWidget(self.chEmail, 2, 2, 1, 1)
        self.chName = QtWidgets.QPushButton(self.frame_3)
        self.chName.setMinimumSize(QtCore.QSize(0, 20))
        self.chName.setStyleSheet("")
        self.chName.setObjectName("chName")
        self.gridLayout_4.addWidget(self.chName, 0, 2, 1, 1)
        self.emailInput = QtWidgets.QLineEdit(self.frame_3)
        self.emailInput.setMinimumSize(QtCore.QSize(200, 25))
        self.emailInput.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.emailInput.setFont(font)
        self.emailInput.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.emailInput.setText("")
        self.emailInput.setObjectName("emailInput")
        self.gridLayout_4.addWidget(self.emailInput, 2, 1, 1, 1)
        self.email2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.email2.setFont(font)
        self.email2.setStyleSheet("background-color: none;")
        self.email2.setObjectName("email2")
        self.gridLayout_4.addWidget(self.email2, 2, 0, 1, 1)
        self.surnameInput = QtWidgets.QLineEdit(self.frame_3)
        self.surnameInput.setMinimumSize(QtCore.QSize(200, 25))
        self.surnameInput.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.surnameInput.setFont(font)
        self.surnameInput.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.surnameInput.setText("")
        self.surnameInput.setObjectName("surnameInput")
        self.gridLayout_4.addWidget(self.surnameInput, 1, 1, 1, 1)
        self.surname2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.surname2.setFont(font)
        self.surname2.setStyleSheet("background-color: none;")
        self.surname2.setObjectName("surname2")
        self.gridLayout_4.addWidget(self.surname2, 1, 0, 1, 1)
        self.name2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name2.setFont(font)
        self.name2.setStyleSheet("background-color: none;")
        self.name2.setObjectName("name2")
        self.gridLayout_4.addWidget(self.name2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.user_5 = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_5.sizePolicy().hasHeightForWidth())
        self.user_5.setSizePolicy(sizePolicy)
        self.user_5.setMinimumSize(QtCore.QSize(320, 191))
        self.user_5.setStyleSheet("")
        self.user_5.setObjectName("user_5")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.user_5)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 20, 291, 151))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.labelUserDescription = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUserDescription.sizePolicy().hasHeightForWidth())
        self.labelUserDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUserDescription.setFont(font)
        self.labelUserDescription.setStyleSheet("background-color: rgb(214, 236, 244);\n""border-radius: 20px;\n")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.labelUserDescription.setIcon(icon2)
        self.labelUserDescription.setIconSize(QtCore.QSize(40, 40))
        self.labelUserDescription.setObjectName("labelUserDescription")
        self.verticalLayout_13.addWidget(self.labelUserDescription)
        self.userDescription = QtWidgets.QTextEdit(self.verticalLayoutWidget_13)
        self.userDescription.setStyleSheet("background-color:rgb(226, 226, 226);\n""padding:5px 5px;\n""border-radius: 20px;\n")
        self.userDescription.setObjectName("userDescription")
        self.verticalLayout_13.addWidget(self.userDescription)
        self.chDescription = QtWidgets.QPushButton(self.user_5)
        self.chDescription.setGeometry(QtCore.QRect(310, 150, 41, 20))
        self.chDescription.setObjectName("chDescription")
        self.verticalLayout_4.addWidget(self.user_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.userInfo_3 = QtWidgets.QPushButton(self.frame_2)
        self.userInfo_3.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userInfo_3.setFont(font)
        self.userInfo_3.setStyleSheet("background-color: rgb(214, 236, 244);\n""border-radius: 20px;\n")
        self.userInfo_3.setIcon(icon1)
        self.userInfo_3.setIconSize(QtCore.QSize(40, 40))
        self.userInfo_3.setObjectName("userInfo_3")
        self.verticalLayout_3.addWidget(self.userInfo_3)
        self.password = QtWidgets.QFormLayout()
        self.password.setVerticalSpacing(8)
        self.password.setObjectName("password")
        self.label_currPass = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_currPass.setFont(font)
        self.label_currPass.setStyleSheet("background-color: none;")
        self.label_currPass.setObjectName("label_currPass")
        self.password.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_currPass)
        self.curPass = QtWidgets.QLineEdit(self.frame_2)
        self.curPass.setMinimumSize(QtCore.QSize(150, 25))
        self.curPass.setMaximumSize(QtCore.QSize(250, 25))
        self.curPass.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.curPass.setText("")
        self.curPass.setObjectName("curPass")
        self.password.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.curPass)
        self.labelNewPass = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelNewPass.setFont(font)
        self.labelNewPass.setStyleSheet("background-color: none;")
        self.labelNewPass.setObjectName("labelNewPass")
        self.password.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelNewPass)
        self.newPass = QtWidgets.QLineEdit(self.frame_2)
        self.newPass.setMinimumSize(QtCore.QSize(150, 25))
        self.newPass.setMaximumSize(QtCore.QSize(250, 25))
        self.newPass.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.newPass.setText("")
        self.newPass.setObjectName("newPass")
        self.password.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.newPass)
        self.labelPassConf = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPassConf.setFont(font)
        self.labelPassConf.setStyleSheet("background-color: none;")
        self.labelPassConf.setObjectName("labelPassConf")
        self.password.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPassConf)
        self.newPassConf = QtWidgets.QLineEdit(self.frame_2)
        self.newPassConf.setMinimumSize(QtCore.QSize(150, 25))
        self.newPassConf.setMaximumSize(QtCore.QSize(250, 25))
        self.newPassConf.setStyleSheet("background-color: #fff;\n""border-radius: 5px;")
        self.newPassConf.setText("")
        self.newPassConf.setObjectName("newPassConf")
        self.password.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newPassConf)
        self.chPass = QtWidgets.QPushButton(self.frame_2)
        self.chPass.setMinimumSize(QtCore.QSize(20, 20))
        self.chPass.setMaximumSize(QtCore.QSize(150, 25))
        self.chPass.setSizeIncrement(QtCore.QSize(0, 0))
        self.chPass.setStyleSheet("")
        self.chPass.setObjectName("chPass")
        self.password.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.chPass)
        self.verticalLayout_3.addLayout(self.password)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.chPP = QtWidgets.QPushButton(self.frame_2)
        self.chPP.setMinimumSize(QtCore.QSize(99, 25))
        self.chPP.setMaximumSize(QtCore.QSize(99, 25))
        self.chPP.setStyleSheet("*{\n"
"background-color: rgb(139, 154, 159);\n"
"border-radius: 5px;\n"
"}\n"
"*:hover{\n"
"background-color: rgb(93, 104, 107)\n"
"}")
        self.chPP.setObjectName("chPP")
        self.horizontalLayout_2.addWidget(self.chPP)
        self.profilePhoto = QtWidgets.QLabel(self.frame_2)
        self.profilePhoto.setMinimumSize(QtCore.QSize(100, 100))
        self.profilePhoto.setMaximumSize(QtCore.QSize(100, 100))
        self.profilePhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.profilePhoto.setObjectName("profilePhoto")
        self.horizontalLayout_2.addWidget(self.profilePhoto)
        spacerItem2 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        self.setTabOrder(self.userInfo_2, self.nameInput)
        self.setTabOrder(self.nameInput, self.chName)
        self.setTabOrder(self.chName, self.surnameInput)
        self.setTabOrder(self.surnameInput, self.chSurname)
        self.setTabOrder(self.chSurname, self.emailInput)
        self.setTabOrder(self.emailInput, self.chEmail)
        self.setTabOrder(self.chEmail, self.labelUserDescription)
        self.setTabOrder(self.labelUserDescription, self.userDescription)
        self.setTabOrder(self.userDescription, self.chDescription)
        self.setTabOrder(self.chDescription, self.userInfo_3)
        self.setTabOrder(self.userInfo_3, self.curPass)
        self.setTabOrder(self.curPass, self.newPass)
        self.setTabOrder(self.newPass, self.newPassConf)
        self.setTabOrder(self.newPassConf, self.chPass)
        self.setTabOrder(self.chPass, self.chPP)

        self.chName.clicked.connect(self.change_name)
        self.chSurname.clicked.connect(self.change_surname)
        self.chEmail.clicked.connect(self.change_email)
        self.chPass.clicked.connect(self.change_password)
        self.chPP.clicked.connect(self.change_profilePhoto)
        self.chDescription.clicked.connect(self.change_description)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.header.setText(_translate("self", "Settings"))
        self.userInfo_2.setText(_translate("self", "User Inselfation"))
        self.name.setText(_translate("self", "Name:"))
        self.userName.setText(_translate("self", self.user.name))
        self.userSurname.setText(_translate("self", self.user.surname))
        self.email.setText(_translate("self", "Email:"))
        self.userEmail.setText(_translate("self", self.user.email))
        self.surname.setText(_translate("self", "Surname:"))
        self.chSurname.setText(_translate("self", "Change"))
        self.chEmail.setText(_translate("self", "Change"))
        self.chName.setText(_translate("self", "Change"))
        self.email2.setText(_translate("self", "Email      :"))
        self.surname2.setText(_translate("self", "Surname :"))
        self.name2.setText(_translate("self", "Name     :"))
        self.labelUserDescription.setText(_translate("self", "User Description"))
        self.userDescription.setPlaceholderText(_translate("self", self.user.description))
        self.chDescription.setText(_translate("self", "Change"))
        self.userInfo_3.setText(_translate("self", "Change Password"))
        self.label_currPass.setText(_translate("self", "Current Password:"))
        self.labelNewPass.setText(_translate("self", "New Password:"))
        self.labelPassConf.setText(_translate("self", "New Password Confirm:"))
        self.chPass.setText(_translate("self", "change"))
        self.chPP.setText(_translate("self", "change profile photo"))
        self.profilePhoto.setText(_translate("self", ""))


        if self.user.profilepicture:
            self.profilePhoto.setStyleSheet(f"border-image:url(../ppimages/{self.user.profilepicture})")
            
        else:
            self.profilePhoto.setStyleSheet("border-image:url(../ppimages/user.png)")
            
        

    




    def _updateUser(func):
        def inner(self):
            current=os.getcwd()
            print("cur",current)
            func(self)
            os.chdir("../DBManagers")
            self.user=self.acc_manager.getUserByID(self.user.ID)

            #os.chdir(current)
            self.retranslateUi()
            

        return inner

    @_updateUser
    def change_name(self):
        if self.nameInput.text()!="": 
            self.acc_manager.updateName(self.user.ID,self.nameInput.text())
            self.nameInput.setText("")
            self.mainUI.statusbar.showMessage("Name has changed")
    
    @_updateUser
    def change_surname(self):
        if self.surnameInput.text()!="":
            self.acc_manager.updateSurname(self.user.ID,self.surnameInput.text())
            self.surnameInput.setText("")
            self.mainUI.statusbar.showMessage("Surname has changed")


    @_updateUser
    def change_email(self):
        if self.emailInput.text()!="":
            self.acc_manager.updateEmail(self.user.ID,self.emailInput.text())
            self.emailInput.setText("")
            self.mainUI.statusbar.showMessage("Email has changed")


    @_updateUser
    def change_password(self):
        if self.curPass.text()==self.user.password:
            if self.newPass.text()==self.newPassConf.text():
                if self.user.password!=self.newPass.text():
                    if self.newPass.text()!="":
                        self.acc_manager.updatePassword(self.user.ID,self.newPass.text())
                        self.curPass.setText("")
                        self.newPass.setText("")
                        self.newPassConf.setText("")
                        self.mainUI.statusbar.showMessage("Password has changed")
        
                else:
                    self.mainUI.statusbar.showMessage("New password have to be different from the old")
            else:
                self.mainUI.statusbar.showMessage("New passwords aren't same")
        else:
            self.mainUI.statusbar.showMessage("Current password is not ")
    @_updateUser
    def change_description(self):
        self.acc_manager.updateDescription(self.user.ID,self.userDescription.toPlainText())
        #self.userDescription.setText("")

    @_updateUser
    def change_profilePhoto(self):
        notchanged=os.getcwd()
        print(notchanged)
        
        os.chdir("../ppimages")
        directory=os.getcwd().replace("\\","/")
        #print(directory)
        file_list=[f for f in os.listdir(directory) if f.endswith(".jpg") or f.endswith(".png")]
        #print(file_list)

        

        options=QtWidgets.QFileDialog.Options()
        filename, a =QtWidgets.QFileDialog.getOpenFileName(self,"Open File","","Image Files (*.png;*.jpg)",
                                                     options=options)
        if filename.endswith(".jpg") or filename.endswith(".png"):

            fileName="".join([x for x in filename][len([x for x in filename])-list(reversed([x for x in filename])).index("/"):])

            state=False
            try:state=[[y for y in filename][x] for x in range(len([x for x in directory]))] == [x for x in directory]
            except:pass

            

            if state:
                current=f"{fileName}"
                os.chdir("../DBManagers")
                self.acc_manager.updateProfilePicture(self.user.ID,current)
                self.mainUI.statusbar.showMessage("Profile photo has changed")
            else:

                if any(list(map(lambda x:fileName==x,file_list))):
                    fileName="".join([x for x in filename][len([x for x in filename])-list(reversed([x for x in filename])).index("/"):])

                    ending=fileName[-4:]
                    name=fileName[:-4]
                    fileName=name+"1"+ending

                current=f"{fileName}"
                        
                
                import shutil
                shutil.copy(filename,current)
                os.chdir("../DBManagers")
                self.acc_manager.updateProfilePicture(self.user.ID,current)
                self.mainUI.statusbar.showMessage("Profile photo has changed")

        os.chdir(notchanged)
        current=f"{fileName}"
        self.mainUI.user.profilepicture=current
        print("upd",self.mainUI.user.profilepicture)
        self.mainUI.headWidget.profile.updateImage()

        


    _updateUser=staticmethod(_updateUser)

