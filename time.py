class time:
    """A class that contains a list of completed events and availabilities, this belongs to a group"""
    "complete or incomplete"

    "availabilities is a list of a user availability pair"

    def __init__(self, date="mm/dd/yy", hour=""):
        self._date = date
        self._hour = hour

    @property
    def date(self):
        return self._date

    @date.setter
    def users(self, date):
        self._date = date

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def users(self, hour):
        self._hour = hour
