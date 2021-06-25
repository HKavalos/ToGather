import socket
import threading
import pickle
from user import user
from event import event
from message import message


class Receive(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self._sock = sock

    # If a message is received from server, unpickle it.  Otherwise, keep listening until the connection is closed.
    # Only prints data for now.
    # TODO: Implement list/set to keep track of each type of data received from server.
    def run(self):
        while True:
            try:
                message = self._sock.recv(4096)
                if message:
                    unpickled_message = pickle.loads(message)
                    if type(unpickled_message) is user:
                        print("User data received from server.")
                        print("Name:", unpickled_message.name)
                        print("Groups:", unpickled_message.groups)
                    elif type(unpickled_message) is event:
                        print("Event data received from server.")
                        print("Activity:", unpickled_message.activity)
                        print("Time:", unpickled_message.time)
                        print("Place:", unpickled_message.place)
                    elif type(unpickled_message) is message:
                        print("Event data received from server.")
                        print("Sender:", unpickled_message.sender)
                        print("Recipient:", unpickled_message.reciever)
                        print("Message:", unpickled_message.message)
            except OSError:  # Catch exception when loop trys to connect after program closes socket.
                break


# Client class calls listener thread to run perpetually and sender method as needed to send data.
class Client(threading.Thread):
    def __init__(self, addr):
        super().__init__()
        self._address = addr

    def run(self):
        with socket.create_connection(address) as srv:
            # Start Receive thread to listen for data from server.
            rcv = Receive(srv)
            rcv.start()

            print("Connected to server: %s:%d\n" % address)
            print("Menu:")
            print("1. Send user")
            print("2. Send event")
            print("3. Send message")
            print("0. Exit")

            # TODO: Implement menu w/ UI
            # Create and send dummy class objects for testing.
            # If there are other clients connected, they should receive what is sent with their receive thread
            selection = input("\nEnter selection:")
            while selection != "0":
                if selection == "1":
                    first_user = user("Ryan")
                    first_user.groups = ["Group1", "Group2"]
                    print("first_user created, sending.")
                    Client.send(srv, first_user)
                    second_user = user("RyRy")
                    second_user.groups = ["Group2"]
                    print("second_user created, sending.")
                    Client.send(srv, second_user)
                elif selection == "2":
                    Client.send(srv, event("activity1", "time to shine", "florida"))
                    Client.send(srv, event("activity2", "afternoon", "texas"))
                elif selection == "3":
                    Client.send(srv, message("test_sender","test_recipient", "test_message"))
                    Client.send(srv, message("test_sender2", "test_recipient2", "test_message2"))
                selection = input("\nEnter selection:")
            srv.sendall("exit()".encode())  # Send exit command to server.

    # TODO: Send data in separate thread?
    # Accepts an object and then pickles before sending to server.
    @staticmethod
    def send(sock, obj):
        sock.sendall(pickle.dumps(obj))  # TODO: Implement compression, catch socket errors


if __name__ == '__main__':
    # TODO: Make host IP configurable by user.
    address = ("99.167.109.219", 55557)
    client = Client(address)
    client.start()
    print("Client started.")
