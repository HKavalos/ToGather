class Event:
    """A class that containts a list of options, a description and is either """
    "compelte or incomplete"

    def __init__(self, description, options, status):
        self._description = description
        self._options = options
        self._status = status

    @property
    def description(self):
        return self._description

    @description.setter
    def activity(self, description):
        self._description = description

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = self._options.append(options)

    @property
    def status(self):
        return self._options

    @status.setter
    def options(self, status):
        self._status = status

