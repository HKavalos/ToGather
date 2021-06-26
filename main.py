import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("circles.ui", self)
        self.addCircle_button.clicked.connect(self.gotocreate)
        self.add_member_button.clicked.connect(self.gotoadd)

    def gotocreate(self):
        groupcreate = GroupCreate()
        widget.addWidget(groupcreate)  # should be changed to insertWidget and removeWidget
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoadd(self):
        addmember = AddMember()
        widget.addWidget(addmember)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class GroupCreate(QMainWindow):
    def __init__(self):
        super(GroupCreate, self).__init__()
        loadUi("popup.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Submitted")
        mwindow = MainWindow()
        mwindow.group_name.setText(self.group_name_entry.text())
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class AddMember(QMainWindow):
    def __init__(self):
        super(AddMember, self).__init__()
        loadUi("newmember.ui", self)
        self.submission_button.clicked.connect(self.submit)

    def submit(self):
        print("Added New Member")
        mwindow = MainWindow()
        mwindow.member.setText(self.name_entry.text())
        widget.addWidget(mwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setMinimumWidth(800)
    widget.setMinimumHeight(600)
    widget.show()
    app.exec_()
