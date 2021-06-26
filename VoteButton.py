from PyQt5 import QtCore, QtGui, QtWidgets
from event import Event

class VoteButton(QtWidgets.QRadioButton):
    def __init__(self, f):
        super(VoteButton, self).__init__()
        QtWidgets.QRadioButton.__init__(self, f)
        self._value = 0
        self._ev = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def ev(self):
        return self._ev

    @ev.setter
    def ev(self, e):
        self._ev = e