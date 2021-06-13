import threading
import socket
import os


# TODO: Keep track of User object that is created at each connection.
# TODO: Maybe keep track of Event objects?
# TODO: Broadcast which User disconnects.
"""Server script, currently will only broadcast serialized objects, does not interpret them."""


class Server(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port

    # Taken from example at https://python.plainenglish.io/build-a-chatroom-app-with-python-458fc435025a
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))

        sock.listen(1)
        print('Listening at', sock.getsockname())

        while True:
            # Accept new connection
            sc, sockname = sock.accept()
            print('Accepted a new connection from {} to {}'.format(sc.getpeername(), sc.getsockname()))

            # Create new thread
            server_socket = ServerSocket(sc, sockname, self)

            # Start new thread
            server_socket.start()

            # Add thread to active connections
            self.connections.append(server_socket)
            print('Ready to receive messages from', sc.getpeername())

    # Send to all connected clients except the source client
    def broadcast(self, message, source):
        for connection in self.connections:
            if connection.sockname != source:
                connection.send(message)

    # Removes a ServerSocket thread from the connections attribute.
    def remove_connection(self, connection):
        self.connections.remove(connection)


# This is where we communicate with a connected client.
class ServerSocket(threading.Thread):
    def __init__(self, sc, sockname, server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server

    def run(self):
        while True:
            message = self.sc.recv(4096)
            if message:
                self.server.broadcast(message, self.sockname)
            else:
                print('{} has closed the connection'.format(self.sockname))
                self.sc.close()
                server.remove_connection(self)
                return

    def send(self, message):
        self.sc.sendall(message)


# Taken from example at https://python.plainenglish.io/build-a-chatroom-app-with-python-458fc435025a
def exit(server):
    """
    Allows the server administrator to shut down the server.
    Typing 'q' in the command line will close all active connections and exit the application.
    """

    while True:
        ipt = input('')
        if ipt == 'q':
            print('Closing all connections...')
            for connection in server.connections:
                connection.sc.close()
            print('Shutting down the server...')
            os._exit(0)


if __name__ == '__main__':
    server = Server('0.0.0.0', 1060)
    server.start()

    # Start thread to listen for exit command.
    exit = threading.Thread(target=exit, args=(server,))
    exit.start()
