import socket
import threading
import pickle
import sqlite3
import os
from user import User
from event import event
from message import message
from group import group
# TODO: Use CamelCase for class names


# TODO: Implementing compression on blobs may be needed if object sizes become large.
# TODO: Apparently this would be more Pythonic as a module instead of a class?
# Using name as primary key, storing serialized class objects as blobs (Binary Large Objects) in a sqlite3 database.
# Each method uses a new database connection because sqlite throws an error if a single connection is accessed by more
# than one thread.
class Data:
    def __init__(self):
        # Create database connection and create tables and as static variables if they don't already exist.
        try:
            db_connection = sqlite3.connect("db.db")
            cursor = db_connection.cursor()
            # Wrapping identifiers in `` prevents conflicts with SQLite keywords i.e. GROUP
            cursor.execute('''CREATE TABLE `groups` (`name` TEXT, `group` BLOB)''')
            cursor.execute('''CREATE TABLE `users` (`name` TEXT, `user` BLOB)''')
            cursor.execute('''CREATE TABLE `events` (`name` TEXT, `event` BLOB)''')
            db_connection.commit()
            db_connection.close()
        except Exception as e:
            print(e)

    @staticmethod
    def reset():
        try:
            os.remove("db.db")  # Dangerous :)
        except Exception as e:
            print(e)

    # TODO: Create a method to add an object that has already been serialized
    @staticmethod
    def add_user(user):
        try:
            db_connection = sqlite3.connect("db.db")
            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO `users` VALUES (?, ?)", (user.name, pickle.dumps(user)))
            db_connection.commit()
            db_connection.close()
        except Exception as e:
            print(e)  # Can't have duplicate name.

    @staticmethod
    def get_users(name=None):  # Returns selected user if parameter is given, otherwise returns list of all users
        try:
            if name is None:
                db_connection = sqlite3.connect("db.db")
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users`")
                users = cursor.fetchall()
                db_connection.commit()
                db_connection.close()
                return users
            else:
                db_connection = sqlite3.connect("db.db")
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users` WHERE `name`=?", (name,))  # Parameter must be tuple
                user = cursor.fetchone()
                db_connection.commit()
                db_connection.close()
                return user
        except Exception as e:
            print(e)  # User not found


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
                msg = self._sock.recv(4096)
                if msg:
                    unpickled_message = pickle.loads(msg)
                    if type(unpickled_message) is User:
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
            print("4. Test database.")
            print("0. Exit")

            # TODO: Implement menu w/ UI
            # Create and send dummy class objects for testing.
            # If there are other clients connected, they should receive what is sent with their receive thread
            selection = input("\nEnter selection:")
            while selection != "0":
                if selection == "1":
                    first_user = User("Ryan")
                    first_user.groups = ["Group1", "Group2"]
                    print("first_user created, sending.")
                    Client.send(srv, first_user)
                    second_user = User("RyRy")
                    second_user.groups = ["Group2"]
                    print("second_user created, sending.")
                    Client.send(srv, second_user)
                elif selection == "2":
                    Client.send(srv, event("activity1", "time to shine", "florida"))
                    Client.send(srv, event("activity2", "afternoon", "texas"))
                elif selection == "3":
                    Client.send(srv, message("test_sender","test_recipient", "test_message"))
                    Client.send(srv, message("test_sender2", "test_recipient2", "test_message2"))
                elif selection == "4":  # Test database
                    # First, get some sample data
                    first_user = User("Ryan")
                    first_user.groups = ["Group1", "Group2"]
                    second_user = User("RyRy")
                    second_user.groups = ["Group2"]
                    Data.reset()  # Delete the database file if it exists.  Prints error if it doesn't
                    Data()  # Initialize Data class to create tables.
                    Data.add_user(first_user)  # Add first user to table.
                    # Print all users.  get_users() returns a list of singular tuples that must be unpickled.
                    # TODO: Unpickle in get_users() instead of here? Or at least get rid of singular tuples.
                    for user in Data.get_users():
                        print(pickle.loads(user[0]))
                    # Repeat for second user.
                    Data.add_user(second_user)
                    for user in Data.get_users():
                        print(pickle.loads(user[0]))
                    # Search for each user by name
                    print(pickle.loads(Data.get_users(first_user.name)[0]))
                    print(pickle.loads(Data.get_users(second_user.name)[0]))

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
