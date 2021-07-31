class User:
    """A class to store data about each user, a user name, a list of groups they are a part of"""
    "and list of constraint times. constraints are a pair of time variables to signify ranges"

    def __init__(self, name="", password="", constraints=None, groups=None):
        self._name = name
        self._password = password
        self._groups = groups
        if self._groups is None:
            self._groups = []
        self._constraints = constraints
        if self._constraints is None:
            self._constraints = []

    def __eq__(self, other):
        if self.name == other.name:
            if self.password == other.password:
                if self.constraints == other.constraints:
                    if self.groups == other.groups:
                        return True
        return False

    def __ne__(self, other):
        if self.name == other.name:
            if self.password == other.password:
                if self.constraints == other.constraints:
                    if self.groups == other.groups:
                        return False
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def constraints(self):
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        self._constraints = constraints

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups):
        self._groups = groups
