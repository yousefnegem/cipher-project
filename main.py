from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 619)
        MainWindow.setStyleSheet("#MainWindow{\n"
"         background:  #666;\n"
"}\n"
"\n"
"*{\n"
"    font-family: century gothic;\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#label_2, #label_3,\n"
" #label_4,  #label_5,  #label_6,\n"
" #label_7,  #label_8,  #label_9,\n"
" #label_10,  #label_11{\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"#tab, \n"
"#tab_2,\n"
"#tab_3{\n"
"\n"
"     background:  #333;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QTabWidget{\n"
"     background:  #333;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"#pushButton, #pushButton_2, #pushButton_3, \n"
"#encrptBtn, #keygenerBtn, #verificationBtn{\n"
"    background:  #f00;\n"
"    border-radius: 10px;\n"
"}\n"
"#pushButton:hover, \n"
"#pushButton_2:hover,\n"
" #pushButton_3:hover {\n"
"    background: #777;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolButton{\n"
"    background:  #f00;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#toolButton:hover{\n"
"transform: scale(1.1);\n"
"    background: #777;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#lineEdit, #lineEdit_2, #lineEdit_3, #lineEdit_4,  #textEdit, #textEdit_2{\n"
"background: transparent;\n"
"color: #fff;\n"
"border: none;\n"
"border-bottom: 1px solid #717072;\n"
"padding:10px ;\n"
"}\n"
"\n"
" #lineEdit_3, #lineEdit_4,  #textEdit, #textEdit_2{\n"
"    border: 1px solid #717072;\n"
"}\n"
"\n"
"/*   coment */\n"
"\n"
"#encrypttxt,\n"
"#keytxt,\n"
"#messagetxt,\n"
"#messagetxt_2,\n"
"#message2txt,\n"
"#keytxt2,\n"
"#keytxt_2,\n"
"#encryptvertxt{\n"
"    background: transparent;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-bottom: 1px solid #717072;\n"
"    padding:10px ;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keygenerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.keygenerBtn.setGeometry(QtCore.QRect(20, 60, 221, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.keygenerBtn.setIcon(icon)
        self.keygenerBtn.setIconSize(QtCore.QSize(30, 30))
        self.keygenerBtn.setObjectName("keygenerBtn")
       

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(254, 0, 812, 690))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 120, 331, 51))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 201, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(290, 210, 191, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 290, 101, 51))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 331, 51))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(210, 120, 71, 51))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(80, 370, 271, 121))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 370, 271, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 280, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(100, 50, 111, 51))
        self.label_5.setObjectName("label_5")
        self.messagetxt = QtWidgets.QLineEdit(self.tab_2)
        self.messagetxt.setGeometry(QtCore.QRect(240, 50, 331, 51))
        self.messagetxt.setInputMask("")
        self.messagetxt.setText("")
        self.messagetxt.setFrame(True)
        self.messagetxt.setObjectName("messagetxt")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(100, 190, 101, 51))
        self.label_6.setObjectName("label_6")
        self.encrypttxt = QtWidgets.QLineEdit(self.tab_2)
        self.encrypttxt.setGeometry(QtCore.QRect(240, 190, 331, 51))
        self.encrypttxt.setInputMask("")
        self.encrypttxt.setText("")
        self.encrypttxt.setFrame(True)
        self.encrypttxt.setReadOnly(True)
        self.encrypttxt.setObjectName("encrypttxt")
        self.keytxt = QtWidgets.QLineEdit(self.tab_2)
        self.keytxt.setGeometry(QtCore.QRect(240, 120, 331, 51))
        self.keytxt.setInputMask("")
        self.keytxt.setText("")
        self.keytxt.setFrame(True)
        self.keytxt.setObjectName("keytxt")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(100, 120, 81, 51))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(110, 110, 131, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(110, 30, 121, 51))
        self.label_9.setObjectName("label_9")
        self.message2txt = QtWidgets.QLineEdit(self.tab_3)
        self.message2txt.setGeometry(QtCore.QRect(270, 110, 361, 51))
        self.message2txt.setInputMask("")
        self.message2txt.setText("")
        self.message2txt.setFrame(True)
        self.message2txt.setObjectName("message2txt")
        self.keytxt_2 = QtWidgets.QLineEdit(self.tab_3)
        self.keytxt_2.setGeometry(QtCore.QRect(270, 190, 361, 51))
        self.keytxt_2.setInputMask("")
        self.keytxt_2.setText("")
        self.keytxt_2.setFrame(True)
        self.keytxt_2.setReadOnly(False)
        self.keytxt_2.setObjectName("keytxt_2")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(110, 190, 101, 51))
        self.label_10.setObjectName("label_10")
        self.messagetxt_2 = QtWidgets.QLineEdit(self.tab_3)
        self.messagetxt_2.setGeometry(QtCore.QRect(270, 30, 361, 51))
        self.messagetxt_2.setInputMask("")
        self.messagetxt_2.setText("")
        self.messagetxt_2.setFrame(True)
        self.messagetxt_2.setObjectName("messagetxt_2")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(110, 270, 151, 51))
        self.label_11.setObjectName("label_11")
        self.encryptvertxt = QtWidgets.QLineEdit(self.tab_3)
        self.encryptvertxt.setGeometry(QtCore.QRect(270, 270, 361, 51))
        self.encryptvertxt.setInputMask("")
        self.encryptvertxt.setText("")
        self.encryptvertxt.setFrame(True)
        self.encryptvertxt.setReadOnly(False)
        self.encryptvertxt.setObjectName("encryptvertxt")
        self.verificationBtn = QtWidgets.QPushButton(self.tab_3)
        self.verificationBtn.setEnabled(True)
        self.verificationBtn.setGeometry(QtCore.QRect(260, 370, 191, 61))
        self.verificationBtn.setObjectName("verificationBtn")
        self.tabWidget.addTab(self.tab_3, "")
        self.encrptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encrptBtn.setGeometry(QtCore.QRect(20, 180, 221, 81))

        



        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encrptBtn.setIcon(icon1)
        self.encrptBtn.setIconSize(QtCore.QSize(30, 30))
        self.encrptBtn.setAutoDefault(True)
        self.encrptBtn.setDefault(True)
        self.encrptBtn.setFlat(True)
        self.encrptBtn.setObjectName("encrptBtn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 310, 221, 81))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #=============================================
        
        self.keygenerBtn.clicked.connect(self.keypage)
        self.encrptBtn.clicked.connect(self.encpage)
        self.pushButton_3.clicked.connect(self.verpage)

        self.tabWidget.tabBar().setVisible(False)

    def keypage(self):
        self.tabWidget.setCurrentIndex(0)
    
    def encpage(self):
        self.tabWidget.setCurrentIndex(1)

    def verpage(self):
        self.tabWidget.setCurrentIndex(2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.keygenerBtn.setText(_translate("MainWindow", "Key Genratoer"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Q"))
        self.label_2.setText(_translate("MainWindow", "P"))
        self.pushButton.setText(_translate("MainWindow", "Key Generator"))
        self.label_4.setText(_translate("MainWindow", "Key List"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "P"))
        self.label_3.setText(_translate("MainWindow", "q"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Key Generatoer"))
        self.pushButton_2.setText(_translate("MainWindow", "Signature"))
        self.label_5.setText(_translate("MainWindow", "Masssge"))
        self.messagetxt.setPlaceholderText(_translate("MainWindow", "Message"))
        self.label_6.setText(_translate("MainWindow", "Encrypt"))
        self.encrypttxt.setPlaceholderText(_translate("MainWindow", "Encrypt"))
        self.keytxt.setPlaceholderText(_translate("MainWindow", "Key"))
        self.label_7.setText(_translate("MainWindow", "Key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Encryption"))
        self.label_8.setText(_translate("MainWindow", "Message 2"))
        self.label_9.setText(_translate("MainWindow", "Message 1"))
        self.message2txt.setPlaceholderText(_translate("MainWindow", "Message 2"))
        self.keytxt_2.setPlaceholderText(_translate("MainWindow", "Key"))
        self.label_10.setText(_translate("MainWindow", "Key"))
        self.messagetxt_2.setPlaceholderText(_translate("MainWindow", "Message 1"))
        self.label_11.setText(_translate("MainWindow", "Encrypt Msg"))
        self.encryptvertxt.setPlaceholderText(_translate("MainWindow", "Encrypt"))
        self.verificationBtn.setText(_translate("MainWindow", "Verification"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Verification"))
        self.encrptBtn.setText(_translate("MainWindow", "Encryption"))
        self.pushButton_3.setText(_translate("MainWindow", "verification"))


                
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
