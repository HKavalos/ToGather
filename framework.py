# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Logan\Desktop\QtDesigner Layouts\framework.ui'
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
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(470, 20, 211, 101))
        self.label.setObjectName("label")
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
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab_3)
        self.stackedWidget_2.setGeometry(QtCore.QRect(530, 60, 521, 471))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget_2.addWidget(self.page_5)
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
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.tab_4)
        self.stackedWidget_3.setGeometry(QtCore.QRect(230, 80, 641, 431))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_4 = QtWidgets.QFrame(self.page_6)
        self.frame_4.setGeometry(QtCore.QRect(70, 20, 501, 391))
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
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_3.addWidget(self.page_7)
        self.mainTab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_5)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 50, 711, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_7 = QtWidgets.QFrame(self.page)
        self.frame_7.setGeometry(QtCore.QRect(110, 20, 421, 361))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_34 = QtWidgets.QLabel(self.frame_7)
        self.label_34.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_7)
        self.label_35.setGeometry(QtCore.QRect(30, 120, 51, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_7)
        self.label_36.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_7)
        self.label_37.setGeometry(QtCore.QRect(30, 210, 51, 16))
        self.label_37.setObjectName("label_37")
        self.radioButton_28 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_28.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton_28.setObjectName("radioButton_28")
        self.radioButton_29 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_29.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.radioButton_29.setObjectName("radioButton_29")
        self.radioButton_30 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_30.setGeometry(QtCore.QRect(290, 120, 82, 17))
        self.radioButton_30.setObjectName("radioButton_30")
        self.radioButton_31 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_31.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton_31.setObjectName("radioButton_31")
        self.radioButton_32 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_32.setGeometry(QtCore.QRect(100, 210, 82, 17))
        self.radioButton_32.setObjectName("radioButton_32")
        self.radioButton_33 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_33.setGeometry(QtCore.QRect(190, 160, 82, 17))
        self.radioButton_33.setObjectName("radioButton_33")
        self.radioButton_34 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_34.setGeometry(QtCore.QRect(190, 210, 82, 17))
        self.radioButton_34.setObjectName("radioButton_34")
        self.radioButton_35 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_35.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.radioButton_35.setObjectName("radioButton_35")
        self.radioButton_36 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_36.setGeometry(QtCore.QRect(280, 210, 82, 17))
        self.radioButton_36.setObjectName("radioButton_36")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(410, 120, 421, 361))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_38 = QtWidgets.QLabel(self.frame_8)
        self.label_38.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame_8)
        self.label_39.setGeometry(QtCore.QRect(30, 120, 51, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_8)
        self.label_40.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_8)
        self.label_41.setGeometry(QtCore.QRect(30, 210, 51, 16))
        self.label_41.setObjectName("label_41")
        self.radioButton_37 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_37.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton_37.setObjectName("radioButton_37")
        self.radioButton_38 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_38.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.radioButton_38.setObjectName("radioButton_38")
        self.radioButton_39 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_39.setGeometry(QtCore.QRect(290, 120, 82, 17))
        self.radioButton_39.setObjectName("radioButton_39")
        self.radioButton_40 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_40.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton_40.setObjectName("radioButton_40")
        self.radioButton_41 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_41.setGeometry(QtCore.QRect(100, 210, 82, 17))
        self.radioButton_41.setObjectName("radioButton_41")
        self.radioButton_42 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_42.setGeometry(QtCore.QRect(190, 160, 82, 17))
        self.radioButton_42.setObjectName("radioButton_42")
        self.radioButton_43 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_43.setGeometry(QtCore.QRect(190, 210, 82, 17))
        self.radioButton_43.setObjectName("radioButton_43")
        self.radioButton_44 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_44.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.radioButton_44.setObjectName("radioButton_44")
        self.radioButton_45 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_45.setGeometry(QtCore.QRect(280, 210, 82, 17))
        self.radioButton_45.setObjectName("radioButton_45")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setGeometry(QtCore.QRect(110, 20, 421, 361))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_42 = QtWidgets.QLabel(self.frame_9)
        self.label_42.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_9)
        self.label_43.setGeometry(QtCore.QRect(30, 120, 51, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_9)
        self.label_44.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_9)
        self.label_45.setGeometry(QtCore.QRect(30, 210, 51, 16))
        self.label_45.setObjectName("label_45")
        self.radioButton_46 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_46.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton_46.setObjectName("radioButton_46")
        self.radioButton_47 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_47.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.radioButton_47.setObjectName("radioButton_47")
        self.radioButton_48 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_48.setGeometry(QtCore.QRect(290, 120, 82, 17))
        self.radioButton_48.setObjectName("radioButton_48")
        self.radioButton_49 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_49.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton_49.setObjectName("radioButton_49")
        self.radioButton_50 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_50.setGeometry(QtCore.QRect(100, 210, 82, 17))
        self.radioButton_50.setObjectName("radioButton_50")
        self.radioButton_51 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_51.setGeometry(QtCore.QRect(190, 160, 82, 17))
        self.radioButton_51.setObjectName("radioButton_51")
        self.radioButton_52 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_52.setGeometry(QtCore.QRect(190, 210, 82, 17))
        self.radioButton_52.setObjectName("radioButton_52")
        self.radioButton_53 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_53.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.radioButton_53.setObjectName("radioButton_53")
        self.radioButton_54 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_54.setGeometry(QtCore.QRect(280, 210, 82, 17))
        self.radioButton_54.setObjectName("radioButton_54")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(410, 120, 421, 361))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_46 = QtWidgets.QLabel(self.frame_10)
        self.label_46.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_10)
        self.label_47.setGeometry(QtCore.QRect(30, 120, 51, 16))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame_10)
        self.label_48.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_10)
        self.label_49.setGeometry(QtCore.QRect(30, 210, 51, 16))
        self.label_49.setObjectName("label_49")
        self.radioButton_55 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_55.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton_55.setObjectName("radioButton_55")
        self.radioButton_56 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_56.setGeometry(QtCore.QRect(200, 120, 82, 17))
        self.radioButton_56.setObjectName("radioButton_56")
        self.radioButton_57 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_57.setGeometry(QtCore.QRect(290, 120, 82, 17))
        self.radioButton_57.setObjectName("radioButton_57")
        self.radioButton_58 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_58.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButton_58.setObjectName("radioButton_58")
        self.radioButton_59 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_59.setGeometry(QtCore.QRect(100, 210, 82, 17))
        self.radioButton_59.setObjectName("radioButton_59")
        self.radioButton_60 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_60.setGeometry(QtCore.QRect(190, 160, 82, 17))
        self.radioButton_60.setObjectName("radioButton_60")
        self.radioButton_61 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_61.setGeometry(QtCore.QRect(190, 210, 82, 17))
        self.radioButton_61.setObjectName("radioButton_61")
        self.radioButton_62 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_62.setGeometry(QtCore.QRect(290, 160, 71, 21))
        self.radioButton_62.setObjectName("radioButton_62")
        self.radioButton_63 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_63.setGeometry(QtCore.QRect(280, 210, 82, 17))
        self.radioButton_63.setObjectName("radioButton_63")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
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
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome Page"))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ToGather </p><p align=\"center\">(logo not implemented remotely yet)</p></body></html>"))
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
        self.label_15.setText(_translate("MainWindow", "Members"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Member"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove Member"))
        self.label_16.setText(_translate("MainWindow", "Username"))
        self.label_17.setText(_translate("MainWindow", "Username"))
        self.label_18.setText(_translate("MainWindow", "Username"))
        self.label_19.setText(_translate("MainWindow", "Username"))
        self.label_20.setText(_translate("MainWindow", "Username"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), _translate("MainWindow", "Circles"))
        self.label_34.setText(_translate("MainWindow", "Vote A"))
        self.label_35.setText(_translate("MainWindow", "1st Choice"))
        self.label_36.setText(_translate("MainWindow", "2nd Choice"))
        self.label_37.setText(_translate("MainWindow", "3rd Choice"))
        self.radioButton_28.setText(_translate("MainWindow", "A"))
        self.radioButton_29.setText(_translate("MainWindow", "B"))
        self.radioButton_30.setText(_translate("MainWindow", "C"))
        self.radioButton_31.setText(_translate("MainWindow", "A"))
        self.radioButton_32.setText(_translate("MainWindow", "A"))
        self.radioButton_33.setText(_translate("MainWindow", "B"))
        self.radioButton_34.setText(_translate("MainWindow", "B"))
        self.radioButton_35.setText(_translate("MainWindow", "C"))
        self.radioButton_36.setText(_translate("MainWindow", "C"))
        self.label_38.setText(_translate("MainWindow", "Name of Vote"))
        self.label_39.setText(_translate("MainWindow", "1st Choice"))
        self.label_40.setText(_translate("MainWindow", "2nd Choice"))
        self.label_41.setText(_translate("MainWindow", "3rd Choice"))
        self.radioButton_37.setText(_translate("MainWindow", "A"))
        self.radioButton_38.setText(_translate("MainWindow", "B"))
        self.radioButton_39.setText(_translate("MainWindow", "C"))
        self.radioButton_40.setText(_translate("MainWindow", "A"))
        self.radioButton_41.setText(_translate("MainWindow", "A"))
        self.radioButton_42.setText(_translate("MainWindow", "B"))
        self.radioButton_43.setText(_translate("MainWindow", "B"))
        self.radioButton_44.setText(_translate("MainWindow", "C"))
        self.radioButton_45.setText(_translate("MainWindow", "C"))
        self.label_42.setText(_translate("MainWindow", "Vote B"))
        self.label_43.setText(_translate("MainWindow", "1st Choice"))
        self.label_44.setText(_translate("MainWindow", "2nd Choice"))
        self.label_45.setText(_translate("MainWindow", "3rd Choice"))
        self.radioButton_46.setText(_translate("MainWindow", "A"))
        self.radioButton_47.setText(_translate("MainWindow", "B"))
        self.radioButton_48.setText(_translate("MainWindow", "C"))
        self.radioButton_49.setText(_translate("MainWindow", "A"))
        self.radioButton_50.setText(_translate("MainWindow", "A"))
        self.radioButton_51.setText(_translate("MainWindow", "B"))
        self.radioButton_52.setText(_translate("MainWindow", "B"))
        self.radioButton_53.setText(_translate("MainWindow", "C"))
        self.radioButton_54.setText(_translate("MainWindow", "C"))
        self.label_46.setText(_translate("MainWindow", "Name of Vote"))
        self.label_47.setText(_translate("MainWindow", "1st Choice"))
        self.label_48.setText(_translate("MainWindow", "2nd Choice"))
        self.label_49.setText(_translate("MainWindow", "3rd Choice"))
        self.radioButton_55.setText(_translate("MainWindow", "A"))
        self.radioButton_56.setText(_translate("MainWindow", "B"))
        self.radioButton_57.setText(_translate("MainWindow", "C"))
        self.radioButton_58.setText(_translate("MainWindow", "A"))
        self.radioButton_59.setText(_translate("MainWindow", "A"))
        self.radioButton_60.setText(_translate("MainWindow", "B"))
        self.radioButton_61.setText(_translate("MainWindow", "B"))
        self.radioButton_62.setText(_translate("MainWindow", "C"))
        self.radioButton_63.setText(_translate("MainWindow", "C"))
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
