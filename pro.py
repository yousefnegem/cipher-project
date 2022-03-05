from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox




class Ui_login(object):


    def openwin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()



    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("login")
        MainWindow.setEnabled(True)
        MainWindow.resize(812, 600)
        MainWindow.setMinimumSize(QtCore.QSize(812, 600))
        MainWindow.setMaximumSize(QtCore.QSize(812, 600))
        MainWindow.setStyleSheet("*{\n"
"    font-family: century gothic;\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"#MainWindow{\n"
"         background:  #666;\n"
"}\n"
"\n"
"QFrame{\n"
"     background:  #333;\n"
"     border-radius:10px;\n"
"}\n"
"\n"
"#pushButton{\n"
"    background:  #f00;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#label_2, #label_3{\n"
"    color: #fff;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"    color:#fff;\n"
"    background:  #777;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#pushButton_2{\n"
"    background:  #00f;\n"
"    border-radius: 50%\n"
"}\n"
"\n"
"#label{\n"
"    color: #fff;\n"
"   font-size:40px;\n"
"}\n"
"\n"
"\n"
"#lineEdit{\n"
"background: transparent;\n"
"color: #fff;\n"
"border: none;\n"
"border-bottom: 1px solid #717072;\n"
"padding:10px ;\n"
"}\n"
"\n"
"\n"
"#lineEdit_2{\n"
"background: transparent;\n"
"color: #fff;\n"
"border: none;\n"
"border-bottom: 1px solid #717072;\n"
"padding:10px ;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 20, 471, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 30, 201, 51))
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 420, 371, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.loginpage)

        


        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 180, 331, 51))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 320, 331, 51))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 201, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 201, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loginpage(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username=="Admin" and password == "Admin":
            self.openwin()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Incoreect Login")
            msg.setText("Wrong Username Or Password!")
            msg.exec_()
            username = self.lineEdit.setText("")
            username = self.lineEdit_2.setText("")

                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))



#===========================================================================================




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 619)
        MainWindow.setMinimumSize(QtCore.QSize(1012, 619))
        MainWindow.setMaximumSize(QtCore.QSize(1012, 619))
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
" #label_10,  #label_11, #label_12, #label_13, #label_14, #label_15, #label_16 {\n"
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
"#encrptBtn, #keygenerBtn, #verificationBtn {\n"
"    background:  #f00;\n"
"    border-radius: 10px;\n"
"}\n"
"#pushButton:hover, \n"
"#pushButton_2:hover,\n"  
" #pushButton_3:hover ,\n"
" #keygenerBtn:hover ,\n"  
" #encrptBtn:hover ,\n"  
" #verificationBtn:hover {\n"
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
"    background: #777;\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#lineEdit, #lineEdit_2, #lineEdit_3, #lineEdit_4,  #textEdit, #textEdit_2, #txtn, #txtnencypt, #textEdit_3, #keytxt_3{\n"
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
        self.tabWidget.setGeometry(QtCore.QRect(254, 9, 761, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 70, 331, 51))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 241, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(290, 140, 191, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 280, 101, 51))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(320, 10, 331, 51))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 231, 51))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(80, 370, 271, 191))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 370, 271, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.txtn = QtWidgets.QLineEdit(self.tab)
        self.txtn.setGeometry(QtCore.QRect(310, 220, 331, 51))
        self.txtn.setInputMask("")
        self.txtn.setText("")
        self.txtn.setFrame(True)
        self.txtn.setObjectName("txtn")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(220, 220, 71, 51))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(490, 310, 171, 51))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(130, 310, 171, 51))
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 380, 191, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(90, 50, 111, 51))
        self.label_5.setObjectName("label_5")
        self.messagetxt = QtWidgets.QLineEdit(self.tab_2)
        self.messagetxt.setGeometry(QtCore.QRect(240, 50, 331, 51))
        self.messagetxt.setInputMask("")
        self.messagetxt.setText("")
        self.messagetxt.setFrame(True)
        self.messagetxt.setObjectName("messagetxt")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(80, 290, 131, 51))
        self.label_6.setObjectName("label_6")
        self.encrypttxt = QtWidgets.QLineEdit(self.tab_2)
        self.encrypttxt.setGeometry(QtCore.QRect(240, 290, 331, 51))
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
        self.label_7.setGeometry(QtCore.QRect(70, 120, 161, 51))
        self.label_7.setObjectName("label_7")
        self.txtnencypt = QtWidgets.QLineEdit(self.tab_2)
        self.txtnencypt.setGeometry(QtCore.QRect(240, 210, 331, 51))
        self.txtnencypt.setInputMask("")
        self.txtnencypt.setText("")
        self.txtnencypt.setFrame(True)
        # self.txtnencypt.setReadOnly(True)
        self.txtnencypt.setObjectName("txtnencypt")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(100, 210, 101, 51))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(100, 110, 131, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(70, 30, 181, 51))
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
        self.label_10.setGeometry(QtCore.QRect(80, 190, 171, 51))
        self.label_10.setObjectName("label_10")
        self.messagetxt_2 = QtWidgets.QLineEdit(self.tab_3)
        self.messagetxt_2.setGeometry(QtCore.QRect(270, 30, 361, 51))
        self.messagetxt_2.setInputMask("")
        self.messagetxt_2.setText("")
        self.messagetxt_2.setFrame(True)
        self.messagetxt_2.setObjectName("messagetxt_2")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(90, 360, 151, 51))
        self.label_11.setObjectName("label_11")
        self.verificationBtn = QtWidgets.QPushButton(self.tab_3)
        self.verificationBtn.setEnabled(True)
        self.verificationBtn.setGeometry(QtCore.QRect(260, 490, 191, 61))
        self.verificationBtn.setObjectName("verificationBtn")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(140, 280, 171, 51))
        self.label_16.setObjectName("label_16")
        self.keytxt_3 = QtWidgets.QLineEdit(self.tab_3)
        self.keytxt_3.setGeometry(QtCore.QRect(270, 280, 361, 51))
        self.keytxt_3.setInputMask("")
        self.keytxt_3.setText("")
        self.keytxt_3.setFrame(True)
        self.keytxt_3.setReadOnly(False)
        self.keytxt_3.setObjectName("keytxt_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(270, 360, 361, 111))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.encrptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encrptBtn.setGeometry(QtCore.QRect(20, 180, 221, 81))
        self.encrptBtn.setStyleSheet("text-alian: left")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/encrypt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encrptBtn.setIcon(icon1)
        self.encrptBtn.setIconSize(QtCore.QSize(30, 30))
        self.encrptBtn.setAutoDefault(True)
        self.encrptBtn.setDefault(True)
        self.encrptBtn.setFlat(True)
        self.encrptBtn.setObjectName("encrptBtn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 300, 221, 81))
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

        self.pushButton.clicked.connect(self.keyGener)

        # self.pushButton.clicked.connect(self.isPrime(self.lineEdit.text().strip()))

        self.pushButton_2.clicked.connect(self.decrypt)


        self.verificationBtn.clicked.connect(self.verify)

    def keypage(self):
        self.tabWidget.setCurrentIndex(0)
    
    def encpage(self):
        self.tabWidget.setCurrentIndex(1)

    def verpage(self):
        self.tabWidget.setCurrentIndex(2)



    def isPrime(self, num1):
        if num1 > 1:
            for i in range(2, num1):
                if (num1 % i) == 0:
                    return (0)
                    # break
            else:
                return (1)
                
        else:
            return (0)
            



   



    def keyGener(self):
        n1 = int(self.lineEdit.text().strip()) 
        n2 = int(self.lineEdit_2.text().strip()) 
        p = (self.isPrime( n1 )) 
        q = (self.isPrime( n2 )) 
        # print(self.isPrime( n1 ))
        # print(self.isPrime( n2 ))
        if( p == 1 and q == 1):
            p = int(self.lineEdit.text())
            q = int(self.lineEdit_2.text())
            n = p * q
            self.txtn.setText(str(n))
            Pn = (p - 1) * (q - 1)
            key = []
            for i in range(2, Pn):
                gcd = self.euclid(Pn, i)
                if gcd == 1:
                    key.insert(0, i)
            numKey = 0


            self.textEdit.setText("")
            self.textEdit_2.setText("")
            
            
            for i in key:
                r, d = self.exteuclid(Pn, i)
                if r == 1:
                    d = int(d)
                if(i != d):
                    print(i, d)
                    self.textEdit.append(str(i))
                    self.textEdit_2.append(str(d))
                    numKey =numKey+1
                    if numKey == 10:
                        break
        else:
             print("the p or q are not prime ")



    # Function to find gcd
    # of two numbers
    def euclid(self, m, n):
        if n == 0:
            return m
        else:
            r = m % n
            return self.euclid(n, r)

        # Program to find





            
    # Multiplicative inverse
    def exteuclid(self, a, b):
        r1 = a
        r2 = b
        s1 = int(1)
        s2 = int(0)
        t1 = int(0)
        t2 = int(1)

        while r2 > 0:
            q = r1 // r2
            r = r1 - q * r2
            r1 = r2
            r2 = r
            s = s1 - q * s2
            s1 = s2
            s2 = s
            t = t1 - q * t2
            t1 = t2
            t2 = t

        if t1 < 0:
            t1 = t1 % a

        return (r1, t1)

  

    def decrypt(self):
        # Enter the message to be sent
        M = int(self.messagetxt.text().strip()) 
        d = int(self.keytxt.text().strip()) 
        n = int(self.txtnencypt.text().strip()) 
        # Signature is created by Alice
        S = (M ** d) % n
        self.encrypttxt.setText(str(S))

    def verify(self):
        # Enter the message to be sent
        c = int(self.messagetxt_2.text().strip()) 
        S = int(self.message2txt.text().strip()) 
        e = int(self.keytxt_2.text().strip()) 
        n = int(self.keytxt_3.text().strip()) 
        # Signature is created by Alice
        M1 = (S ** e) % n
        if( M1 == c):
            self.textEdit_3.setText("The Message is Accpet")
        else:
            self.textEdit_3.setText("The Message is Not Accpet")





    # # Enter two large prime
    # # numbers p and q
    # p = isPrime(823)
    # q = isPrime(953)
    # if p==1 and p==1:
    #     p = 823
    #     q = 953
    #     n = p * q
    #     Pn = (p - 1) * (q - 1)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.keygenerBtn.setText(_translate("MainWindow", "Key Genratoer"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Q"))
        self.label_2.setText(_translate("MainWindow", "Prime Number 1(P)"))
        self.pushButton.setText(_translate("MainWindow", "Key Generator"))
        self.label_4.setText(_translate("MainWindow", "Key List"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "P"))
        self.label_3.setText(_translate("MainWindow", "Prime Number 2(Q)"))
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
        self.txtn.setPlaceholderText(_translate("MainWindow", "p * q"))
        self.label_12.setText(_translate("MainWindow", "N"))
        self.label_14.setText(_translate("MainWindow", "Pravite Key(d)"))
        self.label_15.setText(_translate("MainWindow", "Public Key(e)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Key Generatoer"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign"))
        self.label_5.setText(_translate("MainWindow", "Message"))
        self.messagetxt.setPlaceholderText(_translate("MainWindow", "Message"))
        self.label_6.setText(_translate("MainWindow", " Signature"))
        self.encrypttxt.setPlaceholderText(_translate("MainWindow", " Signature"))
        self.keytxt.setPlaceholderText(_translate("MainWindow", "Privte Key (d)"))
        self.label_7.setText(_translate("MainWindow", "Privte Key (d)"))
        self.txtnencypt.setPlaceholderText(_translate("MainWindow", "N"))
        self.label_13.setText(_translate("MainWindow", "N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Encryption"))
        self.label_8.setText(_translate("MainWindow", " Signature"))
        self.label_9.setText(_translate("MainWindow", "Clear Message"))
        self.message2txt.setPlaceholderText(_translate("MainWindow", " Signature"))
        self.keytxt_2.setPlaceholderText(_translate("MainWindow", "Public Key (e)"))
        self.label_10.setText(_translate("MainWindow", "Public Key (e)"))
        self.messagetxt_2.setPlaceholderText(_translate("MainWindow", "Clear Message"))
        self.label_11.setText(_translate("MainWindow", "Verification"))
        self.verificationBtn.setText(_translate("MainWindow", "Verification"))
        self.label_16.setText(_translate("MainWindow", "N"))
        self.keytxt_3.setPlaceholderText(_translate("MainWindow", "N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Verification"))
        self.encrptBtn.setText(_translate("MainWindow", " Signature"))
        self.pushButton_3.setText(_translate("MainWindow", "verification"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Message Verification"))

                
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
