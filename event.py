class Event:
    """A class to store data about each event"""

    def __init__(self, activity, time, place):
        self._activity = activity
        self._time = time
        self._place = place

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

    @property
    def place(self):
        return self._place

    @place.setter
    def time(self, place):
        self._place = place