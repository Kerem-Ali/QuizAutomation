from PyQt5 import QtCore, QtGui, QtWidgets
from .ProfilePhoto import ProfilePhoto

class UserWidget(QtWidgets.QWidget):
    def __init__(self,profilepicture,username,solved,created):
        super().__init__()
        self.setStyleSheet("*{background-color:rgb(200,200,255);}")
        self.username=username
        self.solved1=solved
        self.created=created

        self.setGeometry(QtCore.QRect(190, 100, 341, 75))
        self.setMaximumSize(QtCore.QSize(16777215, 75))
        self.setObjectName("userWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        

        self.profilepicture = ProfilePhoto(profilepicture)
        self.horizontalLayout.addWidget(self.profilepicture)


        self.userName = QtWidgets.QLabel(self)
        self.userName.setObjectName("userName")
        self.horizontalLayout.addWidget(self.userName)
        self.solved = QtWidgets.QLabel(self)
        self.solved.setObjectName("solved")
        self.horizontalLayout.addWidget(self.solved)
        self.createdQuiz = QtWidgets.QLabel(self)
        self.createdQuiz.setObjectName("createdQuiz")
        self.horizontalLayout.addWidget(self.createdQuiz)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.userName.setText(_translate("self", self.username))
        self.solved.setText(_translate("self", str(self.solved1)))
        self.createdQuiz.setText(_translate("self",str(self.created)))
