from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout
from PyQt5 import QtWidgets,QtCore,QtGui
import pyqtgraph as pg
import numpy as np
import sys

class Line(QtWidgets.QWidget):
    def __init__(self,dates):
        self.dates=dates
        super().__init__()
        self.setStyleSheet("background-color: #00AAAA;")

        self.box=QGridLayout()
        self.box.setSpacing(5)
        self.box.setContentsMargins(5,5,5,5)
        self.setLayout(self.box)

        self.graph_one()



    def graph_one(self):
        def toformat(n):
            if n<10:
                return "0"+str(n)
            else:
                return str(n)
        from datetime import datetime
        this_month=toformat(datetime.now().month)
        print(this_month)
        self.dates=[x.split("-")[-1] for x in self.dates if x.split("-")[1]==this_month]
        print(self.dates)
        x=np.arange(1,32)
        y=[self.dates.count(toformat(y)) for y in range(1,32)]
        bars=pg.BarGraphItem(x=x,height=y,width=1,brush="#00AAAA")
        plt=pg.plot()
        plt.addItem(bars)
        plt.setLabels(left="Y",bottom="X")
        plt.setTitle("Solved Quizes")
        plt.setYRange(0, 20, padding=0)
        self.box.addWidget(plt,0,0)


    


