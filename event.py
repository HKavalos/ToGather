class Event:
    """A class that contains a list of options, a description and is either"""
    "complete or incomplete, completes are in the calendar, both are in the group"

    def __init__(self, description="", options=[], status=False):
        self._description = description
        self._options = options
        self._status = status

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

