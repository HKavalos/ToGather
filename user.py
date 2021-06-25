class user:
    """A class to store data about each user, contains a user name, what groups they are a part of"""
    "and constraint times. constraints are a pair of time variables to signify ranges"

    def __init__(self, name="", constraints=[], groups=[]):
        self._name = name
        self._groups = groups
        self._constraints = constraints

    @property
    def name(self):
        return self._name

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups):
        self._groups = groups

    @property
    def constraints(self):
        return self._constraints

    @constraints.setter
    def availabilities(self, constraints):
        self._constraints = constraints
