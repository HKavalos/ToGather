class message:
    """A class to store message data about each event"""

    def __init__(self, sender, receiver, message):
        self._sender = sender
        self._receiver = receiver
        self._message = message

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
