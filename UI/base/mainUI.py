from PyQt5 import QtCore, QtGui, QtWidgets

from .customNavBar.header import Header
from .baseUI.baseUI import BaseUI

class MainUI(QtWidgets.QMainWindow):
    def __init__(self,acm,qdm,tdm,rdm,user,windowManager):
        self.acm=acm
        self.qdm=qdm
        self.tdm=tdm
        self.rdm=rdm
        
        self.user=user

        self.windowManager=windowManager
        
        super().__init__()

        self.setObjectName("self")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.mainWidget =BaseUI(self.acm,self.qdm,self.tdm,self.rdm,self.user,self)
        
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout.addWidget(self.mainWidget)
        self.setCentralWidget(self.centralwidget)
        
        
        
        self.headWidget = Header(self.user,self.mainWidget)
        self.headWidget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.headWidget.setObjectName("headWidget")
        self.verticalLayout.addWidget(self.headWidget)




        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))





