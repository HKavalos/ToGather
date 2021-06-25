class group:
    "the group class contains a list of users, a list of events and a calendar"
    def __init__(self, name, users, events, calendar):
        self._name
        self._users
        self._events
        self._calendar

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self._name

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users):
        self._users = users.append(users)

    @property
    def events(self):
        return self._events

    @events.setter
    def users(self, events):
        self._events = events.append(events)

    @property
    def calendar(self):
        return self._calendar

    @calendar.setter
    def users(self, calendar):
        self._calendar = calendar

