class User:
    """A class to store data about each user"""

    def __init__(self, name, groups=None):
        self._name = name
        self._groups = groups

    @property
    def name(self):
        return self._name

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups):
        self._groups = groups
