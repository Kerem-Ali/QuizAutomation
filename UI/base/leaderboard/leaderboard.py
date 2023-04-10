from PyQt5 import QtCore, QtGui, QtWidgets
from .user import UserWidget



class LeaderBoard(QtWidgets.QWidget):
    def __init__(self,adb,rdb,tdb):
        self.adb=adb
        self.rdb=rdb
        self.tdb=tdb

        self.users=self.adb.getUsers()
        self.usersInfo=[[user.profilepicture,
                         self.adb.IDtoName(user.ID),
                         self.tdb.howManyCreated(user.ID),
                         len(self.rdb.getSolvedQuizIDs(user.ID))] for user in self.users]

        
        super().__init__()

        self.horizontalLayout=QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("base")
        

        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(130, 110, 481, 351))
        
        
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 316))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)

        
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 40, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.listele()

        

        self.comboBox.activated.connect(self.listele)


        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.groupBox.setTitle(_translate("self", "Users"))
        self.label_4.setText(_translate("self", "Sort by:"))
        self.comboBox.setItemText(0, _translate("self", "Solved"))
        self.comboBox.setItemText(1, _translate("self", "Created Quiz"))


    def listele(self):
        while self.verticalLayout.count():
            child =  self.verticalLayout.takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()
       
        if self.comboBox.currentIndex()==0:
            self.usersInfo=sorted(self.usersInfo,key=lambda user: user[2],reverse=True)
        else:
            self.usersInfo=sorted(self.usersInfo,key=lambda user:user[3],reverse=True)
            
        for user in self.usersInfo:
            self.verticalLayout.addWidget(UserWidget(*user))
        

    
