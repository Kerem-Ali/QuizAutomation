from PyQt5 import QtCore, QtGui, QtWidgets


class ProfilePhoto(QtWidgets.QWidget):
    def __init__(self,imageSource="user.png"):
        
        self.imageSource=imageSource if imageSource else "user.png"
        
        super().__init__()
        self.setGeometry(QtCore.QRect(9, 9, 75, 75))
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setMaximumSize(QtCore.QSize(500, 500))
        self.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Profile = QtWidgets.QFrame(self)
        self.Profile.setMinimumSize(QtCore.QSize(0, 0))
        self.Profile.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Profile.setStyleSheet("background-color:rgb(151, 226, 226);\n"
"border-radius:16px;")
        self.Profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Profile.setObjectName("Profile")
        self.gridLayout = QtWidgets.QGridLayout(self.Profile)
        self.gridLayout.setObjectName("gridLayout")
        self.photo = QtWidgets.QLabel(self.Profile)
        self.photo.setMinimumSize(QtCore.QSize(0, 0))
        self.photo.setMaximumSize(QtCore.QSize(1000, 1000))
        self.photo.setStyleSheet(f"border-image:url(../ppimages/{self.imageSource})")
        self.photo.setText("")
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Profile, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
    def resizeEvent(self,event):
        mn=min([self.height(),self.width()])
        self.resize(mn,mn)
        self.update()
