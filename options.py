from time import time
class options:
    """A class that contains a list of completed events and availabilities, this belongs to a group"""
    "complete or incomplete"

    "availabilities is a list of a user availability pair"

    def __init__(self, activity, time=time(), chosen=False, votes=[]):
        self._activity = activity
        self._time = time
        self._chosen = chosen
        self._votes = votes


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
    def chosen(self):
        return self._chosen

    @chosen.setter
    def chosen(self, chosen):
        self._chosen = chosen

    @property
    def votes(self):
        return self._votes

    @chosen.setter
    def votes(self, votes):
        self._votes = votes
