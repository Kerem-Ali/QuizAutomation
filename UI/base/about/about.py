from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtChart import  QChartView
from PyQt5.QtGui import QPainter


from .dogruyanlis import correctRate
from .linechart import Line

class About(QtWidgets.QWidget):
    def __init__(self,rdm,dbUser):
        self.dbUser=dbUser
        self.rdm=rdm
        
        super().__init__()
        self.dates=self.rdm.getDate(self.dbUser.ID)
        print(self.dates)
        self.categoryAndRates=self.rdm.getCategoryAndRates(self.dbUser.ID)
        self.categories=[x[0] for x in self.categoryAndRates]
        
        self.setGeometry(QtCore.QRect(10, 90, 821, 341))
        self.setObjectName("widget_2")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        for x in range(len(set(self.categories))+1):
            self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.chart=correctRate(0,1,0)
        self.CorrectRate= QChartView(self.chart)

        self.CorrectRate.setRenderHint(QPainter.Antialiasing)
        

        self.verticalLayout.addWidget(self.CorrectRate)
        
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        
        self.widget = Line(self.dates)

        self.verticalLayout_2.addWidget(self.widget)
        
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



        self.listele()
        self.comboBox.activated.connect(self.listele)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Category:"))
        self.comboBox.setItemText(0, _translate("self", "All"))
        
        for i,x in enumerate(set(self.categories),1):
            self.comboBox.setItemText(i, _translate("self", x))

        self.label_2.setText(_translate("self", "This Month"))

    def listele(self):
        correct=0
        incorrect=0
        notAnswered=0
        if self.comboBox.currentText()=="All":
            for x in self.categoryAndRates:
                correct+=x[1]["correct"]
                incorrect+=x[1]["incorrect"]
                notAnswered+=x[1]["notAnswered"]
                
        else:

            for x in self.categoryAndRates:
                if x[0]==self.comboBox.currentText():
                    correct+=x[1]["correct"]
                    incorrect+=x[1]["incorrect"]
                    notAnswered+=x[1]["notAnswered"]
                
           
        print("rates",correct,incorrect,notAnswered)
        self.chart.rupdate(correct,incorrect,notAnswered)

            

