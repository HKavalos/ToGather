# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(108, 96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setObjectName("date_label")
        self.verticalLayout.addWidget(self.date_label)
        self.vote_go_button = QtWidgets.QPushButton(Form)
        self.vote_go_button.setObjectName("vote_go_button")
        self.verticalLayout.addWidget(self.vote_go_button)
        self.op_go_button = QtWidgets.QPushButton(Form)
        self.op_go_button.setObjectName("op_go_button")
        self.verticalLayout.addWidget(self.op_go_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_label.setText(_translate("Form", "Name:"))
        self.date_label.setText(_translate("Form", "Date:"))
        self.vote_go_button.setText(_translate("Form", "Vote"))
        self.op_go_button.setText(_translate("Form", "Options"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
