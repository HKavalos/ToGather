class Event:
    """A class to store data about each event"""

    def __init__(self, activity, time):
        self._activity = activity
        self._time = time

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, activity):
        self._activity = activity

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time