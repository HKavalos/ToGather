# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Logan\Documents\GitHub\ToGather\TestingGrounds\groupwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 245)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_name_label = QtWidgets.QLabel(Form)
        self.group_name_label.setObjectName("group_name_label")
        self.verticalLayout.addWidget(self.group_name_label)
        self.memberDisplay = QtWidgets.QScrollArea(Form)
        self.memberDisplay.setWidgetResizable(True)
        self.memberDisplay.setObjectName("memberDisplay")
        self.memberDisplayContents = QtWidgets.QWidget()
        self.memberDisplayContents.setGeometry(QtCore.QRect(0, 0, 333, 206))
        self.memberDisplayContents.setObjectName("memberDisplayContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.memberDisplayContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.memberDisplay.setWidget(self.memberDisplayContents)
        self.verticalLayout.addWidget(self.memberDisplay)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.group_name_label.setText(_translate("Form", "Group Name:"))
