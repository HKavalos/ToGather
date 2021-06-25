class calendar:
    """A class that contains a list of completed events, fthis belongs to a group"""

    def __init__(self, events=[]):
        self._events = events

    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, events):
        self._events = events
