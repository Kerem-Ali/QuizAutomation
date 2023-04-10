import os
print("yer",os.getcwd())
import sys
sys.path.insert(0, "UI/base/")

from about.about import About
from leaderboard.leaderboard import LeaderBoard
from ViewQuestions.viewQuestions import ViewQuestions
from ViewQuestions.results import Results
from settings.settings import Settings
from createTest.baseCreateQuizUI import BaseCreateQuizUI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *



class BaseUI(QtWidgets.QWidget):
    def __init__(self,acm,qdm,tdm,rdm,user,mainUI):
        self.acm=acm
        self.qdm=qdm
        self.tdm=tdm
        self.rdm=rdm
        self.user=user
        self.mainUI=mainUI
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        #self.setupViewquestions()
        #self.setupCreateQuiz()
        self.setupHome()

    def deleteAll(self):
        while self.layout().count():
            child =  self.layout().takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()

    def setupHome(self):
        self.deleteAll()
        self.layout().addWidget( Results(self.rdm,self.user))
        self.mainUI.statusbar.showMessage("Entered Home")
        pass
    def setupAbout(self):
        self.deleteAll()
        self.layout().addWidget( About(self.rdm,self.user))
        self.mainUI.statusbar.showMessage("Entered About")

    def setupLeaderboard(self):
        self.deleteAll()
        self.layout().addWidget( LeaderBoard(self.acm,self.rdm,self.tdm))
        self.mainUI.statusbar.showMessage("Entered Leaderboard")

    def setupViewquestions(self):
        self.deleteAll()
        self.layout().addWidget(ViewQuestions(self.tdm,self.acm,self.rdm,self.user))
        self.mainUI.statusbar.showMessage("Entered ViewQuestions")

    def setupCreateQuiz(self):
        self.deleteAll()
        self.layout().addWidget(BaseCreateQuizUI(self.tdm,self.rdm,self.user))
        self.mainUI.statusbar.showMessage("Entered CreatingQuiz")

    def setupSettings(self):
        self.deleteAll()
        self.layout().addWidget(Settings(self.user,self.acm,self.mainUI))
        self.mainUI.statusbar.showMessage("Entered Settings")

    def Quit(self):
        self.mainUI.windowManager.setupLogin()
        self.mainUI.close()

                    

        
