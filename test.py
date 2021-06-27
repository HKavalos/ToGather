# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\LuckyCat\PycharmProjects\ToGather\framework.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.uic import loadUi
from group import Group
from user import User
from event import Event
from VoteButton import VoteButton


class Ui_MainWindow(QMainWindow):  # changed to QMainWindow from object
    # Dummy event data. Each event has its own ranked choice value.
    # - Rebecca Ling
    e1 = Event("Arcade", "12:00 p.m.", "Party Pizazz Plaza")
    e2 = Event("Donut Taste Testing", "1:00 p.m.", "Silly Sweet Shop")
    e3 = Event("Paintball", "12:00 p.m.", "Hazel's House")
    event_ranks = {1: e1, 2: e2, 3: e3}

    def setupUi(self, MainWindow):

        # Main
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTab.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.mainTab.setAutoFillBackground(True)
        self.mainTab.setObjectName("mainTab")

        # Home
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.home_votes_widget = QtWidgets.QTabWidget(self.home_tab)
        self.home_votes_widget.setGeometry(QtCore.QRect(40, 170, 291, 341))
        self.home_votes_widget.setObjectName("home_votes_widget")
        self.finished_vote_tab = QtWidgets.QWidget()
        self.finished_vote_tab.setObjectName("finished_vote_tab")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.finished_vote_tab)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 30, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.finished_vote_tab)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(10, 80, 185, 41))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.home_votes_widget.addTab(self.finished_vote_tab, "")
        self.progress_votes_tab = QtWidgets.QWidget()
        self.progress_votes_tab.setObjectName("progress_votes_tab")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.progress_votes_tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 20, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.progress_votes_tab)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 80, 185, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.home_votes_widget.addTab(self.progress_votes_tab, "")
        self.home_upcoming_events = QtWidgets.QTextBrowser(self.home_tab)
        self.home_upcoming_events.setGeometry(QtCore.QRect(730, 350, 351, 251))
        self.home_upcoming_events.setObjectName("home_upcoming_events")
        self.home_login = QtWidgets.QPushButton(self.home_tab)
        self.home_login.setGeometry(QtCore.QRect(920, 20, 75, 23))
        self.home_login.setObjectName("home_login")
        self.home_logout = QtWidgets.QPushButton(self.home_tab)
        self.home_logout.setGeometry(QtCore.QRect(1010, 20, 75, 23))
        self.home_logout.setObjectName("home_logout")
        self.home_new_messages = QtWidgets.QLabel(self.home_tab)
        self.home_new_messages.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.home_new_messages.setObjectName("home_new_messages")
        self.home_image = QtWidgets.QLabel(self.home_tab)
        self.home_image.setGeometry(QtCore.QRect(470, 20, 211, 101))
        self.home_image.setObjectName("home_image")
        self.mainTab.addTab(self.home_tab, "")

        # User Settings
        self.user_settings_tab = QtWidgets.QWidget()
        self.user_settings_tab.setObjectName("user_settings_tab")
        self.user_settings_name = QtWidgets.QLabel(self.user_settings_tab)
        self.user_settings_name.setGeometry(QtCore.QRect(120, 30, 131, 31))
        self.user_settings_name.setObjectName("user_settings_name")
        self.user_settings_profile_pic = QtWidgets.QGraphicsView(self.user_settings_tab)
        self.user_settings_profile_pic.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.user_settings_profile_pic.setObjectName("user_settings_profile_pic")
        self.notification_settings = QtWidgets.QLabel(self.user_settings_tab)
        self.notification_settings.setGeometry(QtCore.QRect(70, 210, 111, 21))
        self.notification_settings.setObjectName("notification_settings")
        self.checkBox = QtWidgets.QCheckBox(self.user_settings_tab)
        self.checkBox.setGeometry(QtCore.QRect(80, 250, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.user_settings_tab)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 280, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        # self.checkBox_3 = QtWidgets.QCheckBox(self.user_settings_tab)
        # self.checkBox_3.setGeometry(QtCore.QRect(80, 310, 70, 17))
        # self.checkBox_3.setObjectName("checkBox_3")
        self.privacy_settings = QtWidgets.QLabel(self.user_settings_tab)
        self.privacy_settings.setGeometry(QtCore.QRect(450, 210, 101, 16))
        self.privacy_settings.setObjectName("privacy_settings")
        self.checkBox_4 = QtWidgets.QCheckBox(self.user_settings_tab)
        self.checkBox_4.setGeometry(QtCore.QRect(450, 250, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.user_settings_tab)
        self.checkBox_5.setGeometry(QtCore.QRect(450, 280, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.submit_settings = QtWidgets.QPushButton(self.user_settings_tab)
        self.submit_settings.setGeometry(QtCore.QRect(450, 310, 110, 30))
        self.submit_settings.setObjectName("submit_settings")
        # self.checkBox_6 = QtWidgets.QCheckBox(self.user_settings_tab)
        # self.checkBox_6.setGeometry(QtCore.QRect(450, 310, 70, 17))
        # self.checkBox_6.setObjectName("checkBox_6")
        self.mainTab.addTab(self.user_settings_tab, "")

        # Events
        self.events_tab = QtWidgets.QWidget()
        self.events_tab.setObjectName("events_tab")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.events_tab)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 180, 441, 371))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.upcoming_events_title = QtWidgets.QLabel(self.events_tab)
        self.upcoming_events_title.setGeometry(QtCore.QRect(160, 70, 111, 21))
        self.upcoming_events_title.setObjectName("upcoming_events_title")
        self.add_event = QtWidgets.QPushButton(self.events_tab)
        self.add_event.setGeometry(QtCore.QRect(1100, 50, 91, 23))
        self.add_event.setObjectName("add_event")
        self.event_title = QtWidgets.QLabel(self.events_tab)
        self.event_title.setGeometry(QtCore.QRect(850, 70, 111, 21))
        self.event_title.setObjectName("event_title")
        self.event_date = QtWidgets.QLabel(self.events_tab)
        self.event_date.setGeometry(QtCore.QRect(850, 90, 111, 21))
        self.event_date.setObjectName("event_date")
        self.event_place = QtWidgets.QLabel(self.events_tab)
        self.event_place.setGeometry(QtCore.QRect(850, 110, 111, 21))
        self.event_place.setObjectName("event_author")
        # self.stackedWidget_2 = QtWidgets.QStackedWidget(self.events_tab)
        # self.stackedWidget_2.setGeometry(QtCore.QRect(530, 60, 521, 471))
        # self.stackedWidget_2.setObjectName("stackedWidget_2")
        # self.page_4 = QtWidgets.QWidget()
        # self.page_4.setObjectName("page_4")
        # self.stackedWidget_2.addWidget(self.page_4)
        # self.page_5 = QtWidgets.QWidget()
        # self.page_5.setObjectName("page_5")
        # self.stackedWidget_2.addWidget(self.page_5)
        self.mainTab.addTab(self.events_tab, "")

        # Schedule
        self.schedule_tab = QtWidgets.QWidget()
        self.schedule_tab.setObjectName("schedule_tab")
        self.frame = QtWidgets.QFrame(self.schedule_tab)
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
        self.frame_2 = QtWidgets.QFrame(self.schedule_tab)
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
        self.frame_3 = QtWidgets.QFrame(self.schedule_tab)
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
        self.mainTab.addTab(self.schedule_tab, "")

        # Circles
        self.circles_tab = QtWidgets.QWidget()
        self.circles_tab.setObjectName("circles_tab")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.circles_tab)
        self.stackedWidget_3.setGeometry(QtCore.QRect(230, 80, 641, 431))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_4 = QtWidgets.QFrame(self.page_6)
        self.frame_4.setGeometry(QtCore.QRect(70, 20, 501, 391))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.circle_name = QtWidgets.QLabel(self.frame_4)
        self.circle_name.setGeometry(QtCore.QRect(230, 10, 151, 16))
        self.circle_name.setObjectName("circle_name")
        self.add_group = QtWidgets.QPushButton(self.frame_4)
        self.add_group.setGeometry(QtCore.QRect(380, 270, 91, 23))
        self.add_group.setObjectName("add_group")
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
        self.mainTab.addTab(self.circles_tab, "")

        # Voting
        self.voting_tab = QtWidgets.QWidget()
        self.voting_tab.setObjectName("voting_tab")
        self.label_21 = QtWidgets.QLabel(self.voting_tab)
        self.label_21.setGeometry(QtCore.QRect(560, 20, 61, 51))
        self.label_21.setObjectName("label_21")

        # Generates each event and their ranked voting options in voting tab
        # Each event gets a unique frame with its own label and ranked choice voting options
        # - Rebecca Ling
        count = 0
        for x in self.event_ranks.values():

            self.f = QtWidgets.QFrame(self.voting_tab)
            self.f.setGeometry(QtCore.QRect(220, 80 + (60 * count), 721, 61))
            self.f.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.f.setFrameShadow(QtWidgets.QFrame.Raised)
            self.f.setObjectName("f" + str(count))

            self.l = QtWidgets.QLabel(self.f)
            self.l.setGeometry(QtCore.QRect(20, 20, 150, 13))
            self.l.setObjectName("l" + str(count))
            self.l.setText(QtCore.QCoreApplication.translate("MainWindow", x.description))

            temp = 0
            i = 1
            for y in self.event_ranks:
                self.r = VoteButton(self.f)
                self.r.ev = x
                self.r.value = i
                self.r.setGeometry(QtCore.QRect(180 + (110 * temp), 20, 82, 17))
                self.r.setObjectName("r{0}".format(i))
                self.r.setText(QtCore.QCoreApplication.translate("MainWindow", "Choice {0}".format(i)))
                self.r.clicked.connect(lambda checked, a=x, b=i: ui.vote(a, b))

                temp += 1
                i += 1
            count += 1

        self.submitVote = QtWidgets.QPushButton(self.voting_tab)
        self.submitVote.setGeometry(QtCore.QRect(1000, 610, 75, 23))
        self.submitVote.setObjectName("submitVote")
        self.mainTab.addTab(self.voting_tab, "")

        # Messages
        self.messages_tab = QtWidgets.QWidget()
        self.messages_tab.setObjectName("messages_tab")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.messages_tab)
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
        self.mainTab.addTab(self.messages_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(5)
        self.home_votes_widget.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome Page"))

        # Home
        self.commandLinkButton_3.setText(_translate("MainWindow", "Vote 1"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Vote 2"))
        self.home_votes_widget.setTabText(self.home_votes_widget.indexOf(self.finished_vote_tab),
                                          _translate("MainWindow", "Finished Votes"))
        self.commandLinkButton.setText(_translate("MainWindow", "Vote 1"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Vote 2"))
        self.home_votes_widget.setTabText(self.home_votes_widget.indexOf(self.progress_votes_tab),
                                          _translate("MainWindow", "In-Progress Votes"))
        self.home_upcoming_events.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Upcoming Events</span></p></body></html>"))
        self.home_login.setText(_translate("MainWindow", "Log In"))
        self.home_logout.setText(_translate("MainWindow", "Log Out "))
        self.home_new_messages.setText(_translate("MainWindow", "x New Messages"))
        self.home_image.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\">ToGather </p><p align=\"center\">(logo not implemented remotely yet)</p></body></html>"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.home_tab), _translate("MainWindow", "Home"))

        # User Settings
        self.user_settings_name.setText(_translate("MainWindow", "Name"))
        self.notification_settings.setText(_translate("MainWindow", "Notification Settings"))
        self.checkBox.setText(_translate("MainWindow", "On"))
        self.checkBox_2.setText(_translate("MainWindow", "Off"))
        # self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.privacy_settings.setText(_translate("MainWindow", "Privacy Settings"))
        self.checkBox_4.setText(_translate("MainWindow", "Public"))
        self.checkBox_5.setText(_translate("MainWindow", "Private"))
        self.submit_settings.setText(_translate("MainWindow", "Submit Settings"))
        # self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.user_settings_tab), _translate("MainWindow", "User Settings"))

        # Events
        self.upcoming_events_title.setText(_translate("MainWindow", "Upcoming Events"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.events_tab), _translate("MainWindow", "Events"))

        # Schedule
        self.label_6.setText(_translate("MainWindow", "Sunday"))
        self.label_7.setText(_translate("MainWindow", "to"))
        self.label_8.setText(_translate("MainWindow", "Not Available"))
        self.label_9.setText(_translate("MainWindow", "Monday"))
        self.label_10.setText(_translate("MainWindow", "to"))
        self.label_11.setText(_translate("MainWindow", "Not Available"))
        self.label_12.setText(_translate("MainWindow", "Tuesday"))
        self.label_13.setText(_translate("MainWindow", "to"))
        self.label_14.setText(_translate("MainWindow", "Not Available"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.schedule_tab), _translate("MainWindow", "Schedule"))

        # Circles
        self.circle_name.setText(_translate("MainWindow", "Circle Name"))
        self.add_group.setText(_translate("MainWindow", "Add Circle"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Member"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove Member"))
        self.add_event.setText(_translate("MainWindow", "Add Event"))
        self.event_date.setText(_translate("MainWindow", "Event Date"))
        self.event_place.setText(_translate("MainWindow", "Event Place"))
        self.event_title.setText(_translate("MainWindow", "Event Title"))
        self.label_16.setText(_translate("MainWindow", "Username"))
        self.label_17.setText(_translate("MainWindow", "Username"))
        self.label_18.setText(_translate("MainWindow", "Username"))
        self.label_19.setText(_translate("MainWindow", "Username"))
        self.label_20.setText(_translate("MainWindow", "Username"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.circles_tab), _translate("MainWindow", "Circles"))

        # Voting
        self.label_21.setText(_translate("MainWindow", "Voting"))
        self.submitVote.setText(_translate("MainWindow", "Submit"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.voting_tab), _translate("MainWindow", "Voting"))

        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">First Last</span></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))

        # Messages
        self.mainTab.setTabText(self.mainTab.indexOf(self.messages_tab), _translate("MainWindow", "Messages"))

    # Determines which event won among the submitted results.
    # A notification popup informs the user that they successfully submitted their vote.
    # After the winner is chosen, another popup appears stating which event won.
    # - Rebecca Ling
    def voteResults(self, MainWindow):

        submit_msg = QtWidgets.QMessageBox()
        submit_msg.setWindowTitle("Submit Successful")
        submit_msg.setText("Your vote has been submitted.")
        submit_msg.setIcon(QtWidgets.QMessageBox.Information)

        top = float('inf')
        standings = ""
        winner = ""
        for x, y in self.event_ranks.items():
            if(x < top):
                top = x
                winner = y.description
            standings += "\n"+str(x)+". "+y.description
        submit_msg.setInformativeText(standings)
        submit_msg.exec_()
        winner_msg = QtWidgets.QMessageBox()
        winner_msg.setWindowTitle("Voting Results")
        winner_msg.setText(winner+" has won the masses.")
        winner_msg.setIcon(QtWidgets.QMessageBox.Information)
        winner_msg.exec_()

    # Finds the rank of a passed in event.
    # - Rebecca Ling
    def key(self, k):
        for x, y in self.event_ranks.items():
            if (k == y):
                return x
        return "Error: event doesn't exist."

    # Switches the rankings between different events based on the option the user picks.
    # - Rebecca Ling
    def vote(self, x, y):
        swap = self.key(x)
        self.event_ranks[y], self.event_ranks[swap] = self.event_ranks[swap], self.event_ranks[y]

    def gotologin(self):
        login_page = LogIn()
        widget.addWidget(login_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        groupcreate = GroupCreate()
        widget.addWidget(groupcreate)  # should be changed to insertWidget and removeWidget
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoadd(self):
        addmember = AddMember()
        widget.addWidget(addmember)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoremove(self):
        removemember = RemoveMember()
        widget.addWidget(removemember)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoaddevent(self):
        newevent = NewEvent()
        widget.addWidget(newevent)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def update_group(self, new_group):
        self.circle_name.setText("Circle Name: " + new_group.name)
        # self.groups.append(new_group)
        # print(len(self.groups))

    def add_member_group(self, new_user, the_group):
        new_name = new_user  # need to find a way to get
        print(new_user)
        print(the_group)
        # print(len(self.groups))

        # for x in self.groups:
        #     print(x.name)
        #     if x.name == the_group:
        #         print("Setting things up")
        #         new_user.groups.append(x)
        #         x.users.append(new_user)
        #
        #         for y in x.users:
        #             new_name = new_name + str(x.name) + " "
        #
        #         break
        # else:
        #     print("Group not found")

        if new_name != "":
            self.label_16.setText(new_name)

    def update_event(self, event):
        self.event_title.setText(event.description)
        self.event_date.setText(event.options)  # time equals place??
        self.event_place.setText(event.status)


class LogIn(QMainWindow):
    def __init__(self):
        super(LogIn, self).__init__()
        loadUi("login.ui", self)
        self.login_password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_acc_button.clicked.connect(self.login_acc)
        self.signup_button.clicked.connect(self.nav)

    def login_acc(self):
        print("Logged In")
        mwindow = MainWindow
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def nav(self):
        print("To Signup!")
        signup_window = SignUp()
        widget.addWidget(signup_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("signup.ui", self)
        self.signup_password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_c_password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_submit_button.clicked.connect(self.submit)

    def submit(self):
        print("Submitted")
        login_window = LogIn()
        widget.addWidget(login_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class GroupCreate(QMainWindow):
    def __init__(self):
        super(GroupCreate, self).__init__()
        loadUi("popup.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Submitted")
        mwindow = MainWindow
        new_group = Group("not available", str(self.group_name_entry.text()))
        # mwindow.groups.append(new_group)
        ui.update_group(new_group)
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AddMember(QMainWindow):
    def __init__(self):
        super(AddMember, self).__init__()
        loadUi("newmember.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Added New Member")
        mwindow = MainWindow
        new_user = self.name_entry.text()
        ui.add_member_group(new_user, str(self.group_name_entry.text()))
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class RemoveMember(QMainWindow):
    def __init__(self):
        super(RemoveMember, self).__init__()
        loadUi("removemember.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Removed Member")
        mwindow = MainWindow
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class NewEvent(QMainWindow):
    def __init__(self):
        super(NewEvent, self).__init__()
        loadUi("newevent.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Added Event")
        mwindow = MainWindow
        new_event = Event(str(self.name_entry.text()), str(self.date_entry.text()), str(self.place_entry.text()))
        ui.update_event(new_event)
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    MainWindow = QtWidgets.QMainWindow()
    widget.addWidget(MainWindow)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.home_login.clicked.connect(ui.gotologin)
    ui.submitVote.clicked.connect(ui.voteResults)
    ui.add_group.clicked.connect(ui.gotocreate)
    ui.pushButton_6.clicked.connect(ui.gotoadd)
    ui.pushButton_7.clicked.connect(ui.gotoremove)
    ui.add_event.clicked.connect(ui.gotoaddevent)

    widget.setMinimumWidth(1280)
    widget.setMinimumHeight(720)
    widget.show()
    sys.exit(app.exec_())