
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt



class NavBar(QtWidgets.QWidget):
    def __init__(self,bgcolor="#DFF6FF",hover="rgb(25,50,250)",focus="rgb(214, 236, 75)" ):
        super().__init__()
        
        self.bgcolor=bgcolor
        self.hover=hover
        self.focus=focus
        
        self.setObjectName("NavBar")
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )

        self.setGeometry(QtCore.QRect(100, 100, 240,50))
        self.setStyleSheet("#frame{\n"
f"background-color:{self.bgcolor} ;\n"
"\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"border: 0px;\n"
"background-color: none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
f"background-color: {self.hover};\n"
"}\n"
"\n"
"")
        self.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()

        ##########


        icon.addPixmap(QtGui.QPixmap("../icons/home-alt-outline.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QtCore.QSize(30, 30))
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.me = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me.setIcon(icon1)
        self.me.setIconSize(QtCore.QSize(30, 30))
        self.me.setObjectName("me")
        self.horizontalLayout.addWidget(self.me)
        self.viewTest = QtWidgets.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/file-find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewTest.setIcon(icon2)
        self.viewTest.setIconSize(QtCore.QSize(30, 30))
        self.viewTest.setObjectName("viewTest")
        self.horizontalLayout.addWidget(self.viewTest)
        self.createTest = QtWidgets.QPushButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createTest.setIcon(icon3)
        self.createTest.setIconSize(QtCore.QSize(30, 30))
        self.createTest.setObjectName("createTest")
        self.horizontalLayout.addWidget(self.createTest)
        self.leaderboard = QtWidgets.QPushButton(self.frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/user-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leaderboard.setIcon(icon4)
        self.leaderboard.setIconSize(QtCore.QSize(30, 30))
        self.leaderboard.setObjectName("leaderboard")
        self.horizontalLayout.addWidget(self.leaderboard)
        self.settings = QtWidgets.QPushButton(self.frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon5)
        self.settings.setIconSize(QtCore.QSize(30, 30))
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.exit = QtWidgets.QPushButton(self.frame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon6)
        self.exit.setIconSize(QtCore.QSize(30, 30))
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        print(self.width())

        self.code()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("NavBar", "NavBar"))
        self.home.setText(_translate("NavBar", "Home"))
        self.me.setText(_translate("NavBar", "Me"))
        self.viewTest.setText(_translate("NavBar", "View Tests"))
        self.createTest.setText(_translate("NavBar", "Create Test"))
        self.leaderboard.setText(_translate("NavBar", "LeaderBoard"))
        self.settings.setText(_translate("NavBar", "Settings"))
        self.exit.setText(_translate("NavBar", "Log out"))
        
        

    def code(self):
        print(self.width())
        self.selected=self.home
        self.choice_buttons=[self.home,self.me,self.viewTest,self.createTest,self.leaderboard,self.settings,self.exit]
        #print(id(self.home)==id(self.choice_buttons[0]))
        #print(self.home==self.choice_buttons[0])
        for button in self.choice_buttons:
            button.clicked.connect(self.change_selected)
        self.selected.setStyleSheet(" background-color: {0}  ;".format(self.focus))
        

    def change_selected(self):
        print(dir(self.sender().objectName))
        sender=self.sender()
        sendername=sender.objectName()
        print(sendername)
        self.selected.setStyleSheet("*{"
                "border-radius: 13px;\n"
                "border: 0px;\n"
                "background-color: none;\n"
                "}\n"
                "*:hover"
                "{\n"
                f"background-color: {self.hover};\n"
                "}\n")

        self.selected=sender
        print(type(self.selected))
        print(sendername+" ekranına geçildi")
        self.selected.setStyleSheet(" background-color: {0}  ;".format(self.focus))
        self.update()
        
       

    def sizeHint(self):
        return QtCore.QSize(240,50)

    def resizeEvent(self,event):
        _translate = QtCore.QCoreApplication.translate

        if self.width()<591:
            for btn in self.choice_buttons:
                
                btn.setText(_translate("NavBar", ""))
        else:
            self.retranslateUi()
        self.update()




    """def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
                
        except:
            print("hata kodu:000x0")"""
