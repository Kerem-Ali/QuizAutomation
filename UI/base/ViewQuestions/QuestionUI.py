from PyQt5 import QtCore, QtGui, QtWidgets
from abc import abstractmethod

class QuestionUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:gray;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-color:rgb(218, 241, 248);\n"
"border: 2px solid;\n"
"}\n"
)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_text = QtWidgets.QTextBrowser(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.question_text.setFont(font)
        self.question_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.question_text.setStyleSheet("QTextBrowser{\n"
"padding:10px;\n"
"background-color:rgba(85, 255, 255,125);\n"
"\n"
"}")
        self.question_text.setObjectName("question_text")
        self.verticalLayout.addWidget(self.question_text)
        
        self.image = QtWidgets.QLabel(self.frame_2)
        self.image.setMinimumSize(QtCore.QSize(0, 200))
        #self.image.setStyleSheet("border-image:url(ppimages/user.png);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.abtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abtn.sizePolicy().hasHeightForWidth())
        self.abtn.setSizePolicy(sizePolicy)
        self.abtn.setMinimumSize(QtCore.QSize(250, 100))
        self.abtn.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abtn.setFont(font)
        self.abtn.setStyleSheet("")
        self.abtn.setObjectName("abtn")
        self.gridLayout.addWidget(self.abtn, 0, 0, 1, 1)
        self.bbtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bbtn.sizePolicy().hasHeightForWidth())
        self.bbtn.setSizePolicy(sizePolicy)
        self.bbtn.setMinimumSize(QtCore.QSize(250, 100))
        self.bbtn.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bbtn.setFont(font)
        self.bbtn.setStyleSheet("")
        self.bbtn.setObjectName("bbtn")
        self.gridLayout.addWidget(self.bbtn, 0, 1, 1, 1)
        self.dbtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbtn.sizePolicy().hasHeightForWidth())
        self.dbtn.setSizePolicy(sizePolicy)
        self.dbtn.setMinimumSize(QtCore.QSize(250, 100))
        self.dbtn.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbtn.setFont(font)
        self.dbtn.setStyleSheet("")
        self.dbtn.setObjectName("dbtn")
        self.gridLayout.addWidget(self.dbtn, 1, 1, 1, 1)
        self.cbtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbtn.sizePolicy().hasHeightForWidth())
        self.cbtn.setSizePolicy(sizePolicy)
        self.cbtn.setMinimumSize(QtCore.QSize(250, 100))
        self.cbtn.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbtn.setFont(font)
        self.cbtn.setStyleSheet("")
        self.cbtn.setObjectName("cbtn")
        self.gridLayout.addWidget(self.cbtn, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.btns=[self.abtn,self.bbtn,self.cbtn,self.dbtn]


        
            

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Question", "Question"))
        self.question_text.setHtml(_translate("Question",""))

    @abstractmethod
    def setup(self,question):
        pass
        
        
