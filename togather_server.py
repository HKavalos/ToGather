from socketserver import *
import pickle
import socket


# Overrides socketserver.BaseRequestHandler class.
# Class methods setup, handle, and finish are called automatically by superclass constructor.
class PythonHandler(BaseRequestHandler):
    _connections = []  # Static variable to keep track of active connections

    def setup(self):
        print("setting up new connection")
        PythonHandler._connections.append(self.request)  # self.request is the socket object being handled.

    def handle(self):
        data = ""
        print("Connected to client: %s:%d" % self.client_address)

        while data != "exit()":
            data = self.request.recv(4096)
            # Call broadcast method if data is pickled, otherwise test for "exit()" string
            try:
                pickle.loads(data)  # Try to unpickle received data
                # This is where we could test for type of unpickled object and process on server if needed.
                PythonHandler.broadcast(data, self.request)  # Call broadcast method
            except (pickle.UnpicklingError, EOFError):
                try:
                    # This is where we can receive and then execute remote commands to server.
                    # At this point, we already know it's not a pickled object, so we'll assume it's an encoded string.
                    data = data.decode()
                    # TODO: Commands for server. Ping?

                except TypeError:
                    print("Invalid data.")

    def finish(self):
        print("Connection to %s:%d closed" % self.client_address)
        PythonHandler._connections.remove(self.request)

    # Sends a message to all connected clients.
    @staticmethod  # Static method has access to static variable connections[]
    def broadcast(message, source):
        # Iterate through connections and send data if remote address is not same as source's
        print("Broadcasting from ", source)
        for connection in PythonHandler._connections:
            if connection.getpeername() != source.getpeername():  # getpeername() returns remote address.
                connection.sendall(message)


if __name__ == '__main__':
    # TODO: Run server in a thread to allow for exit command that calls _server.shutdown()
    # Creates an instance of PythonHandler class whenever connection is received from server.
    # ThreadingTCPServer uses threads to connect to each client.
    with ThreadingTCPServer((socket.gethostname(), 55557), PythonHandler) as _server:
        print("Python server started.")
        _server.serve_forever()
        _server.shutdown()
