from socketserver import *
import pickle
import socket


# Overrides socketserver.BaseRequestHandler class.
# Class methods setup, handle, and finish are called automatically by superclass constructor.
class PythonHandler(BaseRequestHandler):
    _connections = []  # Static variable to keep track of active connections
    _db_requester = socket.socket()

    def setup(self):
        print("setting up new connection")
        PythonHandler._connections.append(self.request)  # self.request is the socket object being handled.

    def handle(self):
        data = ""
        print("Connected to client: %s:%d" % self.client_address)

        # TODO: Exit command needs to close connection
        # TODO: Create method to handle header
        while data != "exit()":
            length = int.from_bytes(self.request.recv(4), "big")  # Get length of message from first 4 bytes
            is_db = int.from_bytes(self.request.recv(1), "big")
            data = self.request.recv(length)
            prefix = length.to_bytes(4, "big")  # Convert length to bytes
            is_db = is_db.to_bytes(1, "big")
            data = bytes(bytearray(prefix + is_db + data))  # Create bytearray to append then convert back to bytes.

            # Added a check to prevent server from sending db to everyone
            if int.from_bytes(is_db, "big") == 0:  # Broadcast to everyone
                PythonHandler.broadcast(data, self.request)
            if int.from_bytes(is_db, "big") == 1:  # Broadcast db to requester only.
                PythonHandler.send(data, PythonHandler._db_requester)
            if int.from_bytes(is_db, "big") == 2:  # Broadcast db request to second newest connection.
                # TODO: Handle if second newest connection was caller
                # TODO: Handle if no other users request database from
                PythonHandler._db_requester = self.request
                target = PythonHandler._connections.pop(-2)
                PythonHandler.send(data, target)
                PythonHandler._connections.insert(-2, target)

    def finish(self):
        print("Connection to %s:%d closed" % self.client_address)
        PythonHandler._connections.remove(self.request)

    # Sends a message to all connected clients.
    @staticmethod  # Static method has access to static variable connections[]
    def broadcast(message, source):
        # Iterate through connections and send data if remote address is not same as source's
        print("Broadcasting from: %s:%d" % source.getpeername())
        for connection in PythonHandler._connections:
            if connection.getpeername() != source.getpeername():  # getpeername() returns remote address.
                connection.sendall(message)

    # Sends a message to one client.
    @staticmethod  # Static method has access to static variable connections[]
    def send(message, destination):
        print("Sending to: %s:%d" % destination.getpeername())
        destination.sendall(message)


if __name__ == '__main__':
    # TODO: Run server in a thread to allow for exit command that calls _server.shutdown()
    # Creates an instance of PythonHandler class whenever connection is received from server.
    # ThreadingTCPServer uses threads to connect to each client.
    with ThreadingTCPServer(("localhost", 55557), PythonHandler) as _server:
        _server.allow_reuse_address = True
        print("Python server started.")
        _server.serve_forever()
        _server.shutdown()
