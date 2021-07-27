# Changed filename so that default time class can be used in server.
class Time:
    """A simple time class that may be replaced"""

    def __init__(self, date="mm/dd/yy", start=0, end=0):

        self._date = date
        self._start = start
        self._end = end
        self._interval = [self.start, self.end]

    def __eq__(self, other):
        if self.date == other.date:
            if self.range == other.range:
                return True
        return False

    def __ne__(self, other):
        if self.date == other.date:
            if self.range == other.range:
                return False
        return True

    def __str__(self):
        return "Date: %s\nStart: %d\nEnd: %d" % (self.date, self.start, self.end)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start
        
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end
        
    @property
    def interval(self):
        return [self.start, self.end]
