class Message:
    def __init__(self, name, delivery, sender="", group=""):
        self._name = name
        self._delivery = delivery
        self._sender = sender
        self._group = group

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def delivery(self):
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        self._delivery = delivery

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group
