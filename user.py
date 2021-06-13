class User:
    """A class to store data about each user"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name