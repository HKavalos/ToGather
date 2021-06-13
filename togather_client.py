import threading
import socket
import os
import user
import event
import pickle
import sys


# TODO: Implement setters/getters
# TODO: Periodically retransmit data to update other users that signed on later.
class Send(threading.Thread):
    def __init__(self, sock, my_user):  # Inherits from Thread superclass
        super().__init__()
        self._sock = sock
        self._user = my_user

    def run(self):
        pickled_user = pickle.dumps(self._user)  # Serialize user object before we send to server.
        # Test if size of object is too large for sendall(4096) call
        # print("size of user: ", sys.getsizeof(pickled_user))
        self._sock.sendall(pickled_user)

        while True:  # TODO: Implement menu.
            menu_selection = input("0 to quit, 1 to add event")
            if menu_selection == '0':
                break
            else:
                activity = input("Activity: ")
                time = input("Time: ")
                my_event = event.Event(activity, time)
                self._sock.sendall(pickle.dumps(my_event))
                print("Event sent.")

        print('\nExiting')
        self._sock.close()
        os._exit(0)  # TODO: Exit more gracefully


# TODO: Implement list/set to keep track of users/events received from server.
class Receive(threading.Thread):
    def __init__(self, sock, my_user):  # Inherits from Thread superclass
        super().__init__()
        self._sock = sock
        self._user = my_user

    # If a message is received from server, unpickle it.  Otherwise, keep listening until connection closed.
    def run(self):
        while True:
            message = self._sock.recv(4096)
            if message:
                unpickled_message = pickle.loads(message)
                if type(unpickled_message) is user.User:
                    print("\nNew user added, say hello to", unpickled_message.name)
                elif type(unpickled_message) is event.Event:
                    print("\nNew event added:")
                    print(unpickled_message.activity)
                    print(unpickled_message.time)
                else:
                    print("Error: Invalid pickle received.")
            else:
                print("Connection closed by server.")
                self._sock.close()
                os._exit(0)  # TODO: Exit more gracefully


class Client:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO: Implement menu options to create events
    def start(self):
        print('Trying to connect to {}:{}...'.format(self._host, self._port))
        self._sock.connect((self._host, self._port))
        print('Successfully connected to {}:{}\n'.format(self._host, self._port))

        my_user = user.User(input('Your name: '))  # Create a new User object to be sent to server.
        print('Welcome, {}!'.format(my_user.name))
        print('Creating send/receive threads')

        send = Send(self._sock, my_user)
        receive = Receive(self._sock, my_user)
        send.start()
        receive.start()


if __name__ == '__main__':
    client = Client("18.222.171.207", 1060)  # IP/Port of the server.  May change.
    client.start()
