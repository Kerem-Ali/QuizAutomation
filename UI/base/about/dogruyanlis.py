from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen,QFont
from PyQt5.QtCore import Qt
from PyQt5 import  QtChart
 

class correctRate(QChart):
    def __init__(self,correct,incorrect,notAnswered):
        super().__init__()
        series = QPieSeries()
        series.append("Dogru", correct)
        series.append("Yanlis", incorrect)
        series.append("Bos", notAnswered)
        series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
         
                 
        dogru = QPieSlice()
        dogru = series.slices()[0]
        dogru.setLabelVisible(True)
        dogru.setPen(QPen(Qt.black, 2))
        dogru.setBrush(Qt.green)
        dogru.setLabelColor(Qt.white)

        yanlis = QPieSlice()
        yanlis = series.slices()[1]
        yanlis.setLabelVisible(True)
        yanlis.setPen(QPen(Qt.black, 2))
        yanlis.setBrush(Qt.red)
        yanlis.setLabelColor(Qt.white)


        bos = QPieSlice()
        bos = series.slices()[2]
        bos.setLabelVisible(True)
        bos.setPen(QPen(Qt.black, 2))
        bos.setBrush(Qt.gray)
        bos.setLabelColor(Qt.white)
        for slice in series.slices():
            slice.setLabel("{:.0f}%".format(100 * slice.percentage()))
         
        self.legend().hide()
        self.addSeries(series)
        self.createDefaultAxes()
        #chart.setAnimationOptions(QChart.SeriesAnimations)
        #chart.setTitle("Dogru yanlis Orani")
         
        #chart.legend().setVisible(True)
        self.legend().setAlignment(Qt.AlignBottom)
        self.legend().markers(series)[0].setLabel("Dogru")
        self.legend().markers(series)[1].setLabel("Yanlis")
        self.legend().markers(series)[2].setLabel("Bos")

    def rupdate(self,correct,incorrect,notAnswered):
        series = QPieSeries()
        series.append("Dogru", correct)
        series.append("Yanlis", incorrect)
        series.append("Bos", notAnswered)
        series.setLabelsPosition(QtChart.QPieSlice.LabelInsideHorizontal)
         
                 
        dogru = QPieSlice()
        dogru = series.slices()[0]
        dogru.setLabelVisible(True)
        dogru.setPen(QPen(Qt.black, 2))
        dogru.setBrush(Qt.green)
        dogru.setLabelColor(Qt.white)

        yanlis = QPieSlice()
        yanlis = series.slices()[1]
        yanlis.setLabelVisible(True)
        yanlis.setPen(QPen(Qt.black, 2))
        yanlis.setBrush(Qt.red)
        yanlis.setLabelColor(Qt.white)


        bos = QPieSlice()
        bos = series.slices()[2]
        bos.setLabelVisible(True)
        bos.setPen(QPen(Qt.black, 2))
        bos.setBrush(Qt.gray)
        bos.setLabelColor(Qt.white)
        for slice in series.slices():
            slice.setLabel("{:.0f}%".format(100 * slice.percentage()))
         
        self.legend().hide()
        self.addSeries(series)
        self.createDefaultAxes()
        #chart.setAnimationOptions(QChart.SeriesAnimations)
        #chart.setTitle("Dogru yanlis Orani")
         
        #chart.legend().setVisible(True)
        self.legend().setAlignment(Qt.AlignBottom)
        self.legend().markers(series)[0].setLabel("Dogru")
        self.legend().markers(series)[1].setLabel("Yanlis")
        self.legend().markers(series)[2].setLabel("Bos")

        
       
        
