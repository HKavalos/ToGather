# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framework.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTab.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.mainTab.setAutoFillBackground(True)
        self.mainTab.setObjectName("mainTab")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(370, 30, 431, 111))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget.setGeometry(QtCore.QRect(40, 170, 291, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.tab_7)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 30, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.tab_7)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(10, 80, 185, 41))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_8)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 20, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab_8)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 80, 185, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.tabWidget.addTab(self.tab_8, "")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser.setGeometry(QtCore.QRect(730, 350, 351, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(1010, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_25 = QtWidgets.QLabel(self.tab_6)
        self.label_25.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_25.setObjectName("label_25")
        self.mainTab.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 131, 31))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 111, 21))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(80, 250, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 280, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 310, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(450, 210, 101, 16))
        self.label_4.setObjectName("label_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(450, 250, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(450, 280, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(450, 310, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.mainTab.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 180, 441, 371))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(160, 70, 111, 21))
        self.label_5.setObjectName("label_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(510, 20, 581, 591))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.mainTab.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(30, 60, 191, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 20, 81, 16))
        self.label_6.setObjectName("label_6")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(50, 80, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.label_7.setObjectName("label_7")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit_2.setGeometry(QtCore.QRect(50, 140, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(230, 60, 191, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(70, 20, 81, 16))
        self.label_9.setObjectName("label_9")
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit_3.setGeometry(QtCore.QRect(50, 80, 118, 22))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.label_10.setObjectName("label_10")
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit_4.setGeometry(QtCore.QRect(50, 140, 118, 22))
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_11.setObjectName("label_11")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(430, 60, 191, 551))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(70, 20, 81, 16))
        self.label_12.setObjectName("label_12")
        self.timeEdit_5 = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit_5.setGeometry(QtCore.QRect(50, 80, 118, 22))
        self.timeEdit_5.setObjectName("timeEdit_5")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.label_13.setObjectName("label_13")
        self.timeEdit_6 = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit_6.setGeometry(QtCore.QRect(50, 140, 118, 22))
        self.timeEdit_6.setObjectName("timeEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_14.setObjectName("label_14")
        self.mainTab.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea.setGeometry(QtCore.QRect(60, 80, 221, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 200, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setGeometry(QtCore.QRect(380, 90, 501, 391))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(230, 10, 47, 13))
        self.label_15.setObjectName("label_15")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 300, 91, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 330, 91, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(30, 70, 71, 81))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(120, 70, 71, 81))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_5.setGeometry(QtCore.QRect(220, 70, 71, 81))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_6.setGeometry(QtCore.QRect(410, 70, 71, 81))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_7.setGeometry(QtCore.QRect(320, 70, 71, 81))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(40, 160, 51, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(130, 160, 51, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(230, 160, 51, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(330, 160, 51, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(420, 160, 51, 16))
        self.label_20.setObjectName("label_20")
        self.mainTab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_2.setGeometry(QtCore.QRect(60, 90, 221, 461))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 219, 459))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 200, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.frame_5 = QtWidgets.QFrame(self.tab_5)
        self.frame_5.setGeometry(QtCore.QRect(460, 90, 421, 361))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(30, 120, 51, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(30, 210, 51, 16))
        self.label_24.setObjectName("label_24")
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 120, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_5.setGeometry(QtCore.QRect(100, 210, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_6.setGeometry(QtCore.QRect(190, 160, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_7.setGeometry(QtCore.QRect(190, 210, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_8.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_9.setGeometry(QtCore.QRect(280, 210, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.mainTab.addTab(self.tab_5, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_9)
        self.scrollArea_3.setGeometry(QtCore.QRect(20, 40, 1081, 481))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1079, 479))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 1081, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 360, 1081, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 120, 1081, 121))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 240, 1081, 121))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.mainTab.addTab(self.tab_9, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome Page"))
        self.label.setText(_translate("MainWindow", "ToGather"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Vote 1"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Vote 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Finished Votes"))
        self.commandLinkButton.setText(_translate("MainWindow", "Vote 1"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Vote 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "In-Progress Votes"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Upcoming Events</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Log Out "))
        self.label_25.setText(_translate("MainWindow", "x New Messages"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_6), _translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Notification Settings"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.label_4.setText(_translate("MainWindow", "Privacy Settings"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab), _translate("MainWindow", "User Settings"))
        self.label_5.setText(_translate("MainWindow", "Upcoming Events"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), _translate("MainWindow", "Events"))
        self.label_6.setText(_translate("MainWindow", "Sunday"))
        self.label_7.setText(_translate("MainWindow", "to"))
        self.label_8.setText(_translate("MainWindow", "Not Available"))
        self.label_9.setText(_translate("MainWindow", "Monday"))
        self.label_10.setText(_translate("MainWindow", "to"))
        self.label_11.setText(_translate("MainWindow", "Not Available"))
        self.label_12.setText(_translate("MainWindow", "Tuesday"))
        self.label_13.setText(_translate("MainWindow", "to"))
        self.label_14.setText(_translate("MainWindow", "Not Available"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_2), _translate("MainWindow", "Schedule"))
        self.pushButton_2.setText(_translate("MainWindow", "Circle A"))
        self.pushButton_3.setText(_translate("MainWindow", "Circle B"))
        self.pushButton_4.setText(_translate("MainWindow", "Circle C"))
        self.pushButton_5.setText(_translate("MainWindow", "Circle D"))
        self.label_15.setText(_translate("MainWindow", "Members"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Member"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove Member"))
        self.label_16.setText(_translate("MainWindow", "Username"))
        self.label_17.setText(_translate("MainWindow", "Username"))
        self.label_18.setText(_translate("MainWindow", "Username"))
        self.label_19.setText(_translate("MainWindow", "Username"))
        self.label_20.setText(_translate("MainWindow", "Username"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), _translate("MainWindow", "Circles"))
        self.pushButton_8.setText(_translate("MainWindow", "Vote 1"))
        self.pushButton_9.setText(_translate("MainWindow", "Vote 2"))
        self.pushButton_10.setText(_translate("MainWindow", "Vote 3"))
        self.pushButton_11.setText(_translate("MainWindow", "Vote 4"))
        self.label_21.setText(_translate("MainWindow", "Name of Vote"))
        self.label_22.setText(_translate("MainWindow", "1st Choice"))
        self.label_23.setText(_translate("MainWindow", "2nd Choice"))
        self.label_24.setText(_translate("MainWindow", "3rd Choice"))
        self.radioButton.setText(_translate("MainWindow", "A"))
        self.radioButton_2.setText(_translate("MainWindow", "B"))
        self.radioButton_3.setText(_translate("MainWindow", "C"))
        self.radioButton_4.setText(_translate("MainWindow", "A"))
        self.radioButton_5.setText(_translate("MainWindow", "A"))
        self.radioButton_6.setText(_translate("MainWindow", "B"))
        self.radioButton_7.setText(_translate("MainWindow", "B"))
        self.radioButton_8.setText(_translate("MainWindow", "C"))
        self.radioButton_9.setText(_translate("MainWindow", "C"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_5), _translate("MainWindow", "Voting"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_9), _translate("MainWindow", "Messages"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
