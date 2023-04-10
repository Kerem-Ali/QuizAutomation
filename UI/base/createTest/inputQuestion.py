from PyQt5 import QtCore, QtGui, QtWidgets


class InputQuestion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("#self\n"
"{\n"
"background-color: #256D85;\n"
"}\n"
"#frame{\n"
"background-color: #DFF6FF;\n"
"border-radius: 20px;\n"
"}\n"

"QLineEdit{\n"
"background-color:\"gray\";\n"
"color:\"white\";}\n"
"\n"
"\n"
"\n"
"")

        self.filename=""
        
        self.setGeometry(QtCore.QRect(100, 80, 511, 371))
        self.setObjectName("questionInputWidget")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputQuestion = QtWidgets.QTextEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputQuestion.sizePolicy().hasHeightForWidth())
        self.inputQuestion.setSizePolicy(sizePolicy)
        self.inputQuestion.setMinimumSize(QtCore.QSize(100, 0))
        self.inputQuestion.setMaximumSize(QtCore.QSize(16777215, 75))
        self.inputQuestion.setObjectName("inputQuestion")
        self.inputQuestion.setStyleSheet("QTextEdit{\nheight:50px;\nbackground-color:rgb(25,75,200);\ncolor:rgb(255,255,255);\nborder-radius:2px;\n}\n")
        
        self.verticalLayout.addWidget(self.inputQuestion)

        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addImage = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addImage.sizePolicy().hasHeightForWidth())
        self.addImage.setSizePolicy(sizePolicy)
        self.addImage.setObjectName("addImage")
        self.horizontalLayout.addWidget(self.addImage)
        
        self.image = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.image.setMinimumSize(QtCore.QSize(100, 100))
        self.image.setMaximumSize(QtCore.QSize(1000, 600))
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setText("")
        self.image.setObjectName("image")
        self.horizontalLayout.addWidget(self.image)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.image.setMinimumSize(1,1)
        """
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        """
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.rd0 = QtWidgets.QRadioButton(self)
        self.rd0.setChecked(True)
        self.rd0.setObjectName("rd0")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rd0)

        

        self.answer1Input = QtWidgets.QLineEdit(self)
        self.answer1Input.setObjectName("answer1Input")
        self.answer1Input.setStyleSheet("QLineEdit{\nheight:15px;\nbackground-color:rgb(50,50,200);\ncolor:rgb(255,255,255)\nborder-radius:2px;\n}\n")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.answer1Input)
        

        self.rd1 = QtWidgets.QRadioButton(self)
        self.rd1.setObjectName("rd1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rd1)
        self.answer2Input = QtWidgets.QLineEdit(self)
        self.answer2Input.setObjectName("answer2Input")
        self.answer2Input.setStyleSheet("QLineEdit{\nheight:15px;\nbackground-color:rgb(50,50,200);\ncolor:rgb(255,255,255)\nborder-radius:2px;\n}\n")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.answer2Input)
        


        self.rd2 = QtWidgets.QRadioButton(self)
        self.rd2.setObjectName("rd2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rd2)

        self.answer3Input = QtWidgets.QLineEdit(self)
        self.answer3Input.setObjectName("answer3Input")
        self.answer3Input.setStyleSheet("QLineEdit{\nheight:15px;\nbackground-color:rgb(50,50,200);\ncolor:rgb(255,255,255)\nborder-radius:2px;\n}\n")
        
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.answer3Input)


        self.rd3 = QtWidgets.QRadioButton(self)
        self.rd3.setObjectName("rd3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rd3)

        self.answer4Input = QtWidgets.QLineEdit(self)
        self.answer4Input.setObjectName("answer4Input")
        self.answer4Input.setStyleSheet("QLineEdit{\nheight:15px;\nbackground-color:rgb(50,50,200);\ncolor:rgb(255,255,255)\nborder-radius:2px;\n}\n")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.answer4Input)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.rdbtns=[self.rd0,self.rd1,self.rd2,self.rd3]


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.addImage.clicked.connect(self.changeImage)


        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.inputQuestion.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addImage.setText(_translate("self", "Add image"))
        self.inputQuestion.setText("keremali")
        self.rd0.setText(_translate("self", "A"))
        self.rd1.setText(_translate("self", "B"))
        self.rd2.setText(_translate("self", "C"))
        self.rd3.setText(_translate("self", "D"))



    def changeImage(self):
        
        import os
        print("off",os.getcwd())
        directory=os.getcwd().replace("\\","/")
        file_list=[f for f in os.listdir(directory) if f.endswith(".jpg") or f.endswith(".png")]
        
        options=QtWidgets.QFileDialog.Options()
        self.filename, a =QtWidgets.QFileDialog.getOpenFileName(self,"Open File","","Image Files (*.png;*.jpg)",
                                                     options=options)
        if self.filename.endswith(".jpg") or self.filename.endswith(".png") or self.filename.endswith(".JPG") or self.filename.endswith(".PNG"):
            
            print(self.filename)
            
            
            pixmap=QtGui.QPixmap(self.filename)
            pixmap=pixmap.scaled(self.image.width(),self.image.height())
            self.image.setPixmap(pixmap)
            self.image.update()
            
            self.question.imageSource=self.filename
            

    def resizeEvent(self,event):
        try:
            pixmap=QtGui.QPixmap(self.filename)
        except:
            pixmap=QtGui.QPixmap("default.png")

        pixmap=pixmap.scaled(self.image.width(),self.image.height())
        self.image.setPixmap(pixmap)
        self.image.resize(self.image.width(),self.image.height())


    def setup(self,question):
        self.question=question
        
        self.filename=self.question.imageSource
        
        
        self.selected=self.rdbtns[self.question.selected-1]
        self.inputQuestion.setText(self.question.question)
        self.answer1Input.setText(self.question.choice1)
        self.answer2Input.setText(self.question.choice2)
        self.answer3Input.setText(self.question.choice3)
        self.answer4Input.setText(self.question.choice4)

        if self.question.imageSource=="":
            self.image.setStyleSheet("")
            self.image.setPixmap(QtGui.QPixmap())
            self.image.update()
        else:

            pixmap=QtGui.QPixmap(self.filename)
            pixmap=pixmap.scaled(self.image.width(),self.image.height())
            self.image.setPixmap(pixmap)
            self.image.update()
        print("selected",self.question.selected)
        if self.question.selected!=0:
            match self.question.selected:
                case 1:
                    self.rd0.setChecked(True)
                case 2:
                    self.rd1.setChecked(True)
                case 3:
                    self.rd2.setChecked(True)
                case 4:
                    self.rd3.setChecked(True)

        for btn in self.rdbtns:
            btn.toggled.connect(self.change_selected)

    def change_selected(self):
        self.selected=self.sender()
        self.question.selected=self.rdbtns.index(self.selected)+1
                

        
            

