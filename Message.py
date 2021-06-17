class Message:
    """A class to store message data about each event"""

    def __init__(self, sender, reciever, message):
        self._sender = sender
        self._reciever = reciever
        self._message = message

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def reciever(self):
        return self._reciever

    @reciever.setter
    def reciever(self, reciever):
        self._reciever = reciever

    @property
    def message(self):
        return self._message

    @message.setter
    def sender(self, message):
        self._message = message
