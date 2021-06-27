import io
import socket
import sys
import threading
import pickle
import sqlite3
import os
import traceback

from user import User
from event import event
from message import message
from group import group
# TODO: Use CamelCase for class names


# TODO: Implementing compression on blobs may be needed if object sizes become large.
# TODO: Remove traceback from exception handlers before release. Useful for testing right now.  Logging instead?
# TODO: Apparently this would be more Pythonic as a module instead of a class? Or with class methods instead of static?
# Using name as primary key, storing serialized class objects as blobs (Binary Large Objects) in a sqlite3 database.
# Each method uses a new database connection because sqlite throws an error if a single connection is accessed by more
# than one thread.
class Data(threading.local):
    DB_FILENAME = "db.db"

    # Method to create database connection and create tables and as static variables if they don't already exist.
    @staticmethod
    def create_tables():
        try:
            db_connection = sqlite3.connect(Data.DB_FILENAME)
            cursor = db_connection.cursor()
            # Wrapping identifiers in `` prevents conflicts with SQLite keywords i.e. GROUP
            cursor.execute('''CREATE TABLE `groups` (`name` TEXT, `group` BLOB)''')
            cursor.execute('''CREATE TABLE `users` (`name` TEXT, `user` BLOB)''')
            cursor.execute('''CREATE TABLE `events` (`name` TEXT, `event` BLOB)''')
            db_connection.commit()
            db_connection.close()
        except Exception as e:
            print(e)

    # Delete database file. Useful if corrupted.
    @staticmethod
    def db_reset():
        try:
            os.remove(Data.DB_FILENAME)  # Dangerous :)
            Data.create_tables()
        except Exception as e:
            print(e.with_traceback())

    # Request a copy of database from server.  Fulfilled by other clients.
    @staticmethod
    def db_request():
        sender = Client.Send("request_db()", 2)
        sender.start()

    # Method to regenerate database using file received from server.
    @staticmethod
    def db_reload(db):
        Data.db_reset()
        try:
            with open(Data.DB_FILENAME, "wb") as file:  # Write bytes back to file
                file.write(db)
        except Exception as e:
            print(e.with_traceback())

    # Method to send pickled db to server when requested.  Unpickle will let us know it's a file in Receive class.
    @staticmethod
    def db_send():
        try:
            with open(Data.DB_FILENAME, "rb") as file:
                db_file = file.read()
                sender = Client.Send(db_file, 1)
                sender.start()
        except Exception as e:
            print(e)

    @staticmethod
    def add_user(user):
        try:
            db_connection = sqlite3.connect(Data().DB_FILENAME)
            cursor = db_connection.cursor()
            if Data.get_users(user.name) is None:
                cursor.execute("INSERT INTO `users` VALUES (?, ?)", (user.name, pickle.dumps(user)))
                db_connection.commit()
                sender = Client.Send(pickle.dumps(user))
                sender.start()
            db_connection.close()
        except Exception as e:
            print(e.with_traceback())  # Can't have duplicate name.

    @staticmethod
    def get_users(name=None):  # Returns User object if parameter is given, otherwise returns list of all users
        try:
            if name is None:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users`")
                users = cursor.fetchall()
                db_connection.commit()
                db_connection.close()

                # Unpickle each object into new list to return.
                unpickled_users = []
                for user in users:
                    unpickled_users.append(pickle.loads(user[0]))
                return unpickled_users
            else:
                db_connection = sqlite3.connect(Data().DB_FILENAME)
                cursor = db_connection.cursor()
                cursor.execute("SELECT `user` FROM `users` WHERE `name`=?", (name,))  # Parameter must be tuple
                user = cursor.fetchone()  # Returns None if nothing found.
                db_connection.commit()
                db_connection.close()
                if user is not None:
                    user = pickle.loads(user[0])
                return user
        except Exception as e:
            print(e)
            return None


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
                length = int.from_bytes(self._sock.recv(4), "big")  # Get length of message from first 4 bytes
                is_db = int.from_bytes(self._sock.recv(1), "big")
                msg = self._sock.recv(length)
                if msg:
                    try:  # Parse for string commands received from server.
                        cmd = msg.decode()
                        if cmd == "request_db()":  # Send db if requested
                            print("Request for database file received. Sending.")
                            Data.db_send()
                    except UnicodeDecodeError:
                        try:  # Try to unpickle if you can't decode
                            unpickled_message = pickle.loads(msg)
                            # Add received user to local db.
                            if type(unpickled_message) is User:
                                Data.add_user(unpickled_message)
                            elif type(unpickled_message) is event:
                                pass
                            elif type(unpickled_message) is message:
                                pass
                        except pickle.PickleError as e:
                            # Must be a database file we need to load.
                            # TODO: Check if received file is actually db.db
                            try:
                                print("Database file received.  Reloading.")
                                Data.db_reload(msg)
                            except Exception as e:
                                # print(e.with_traceback())
                                pass

            except OSError as e:  # Catch exception when loop trys to connect after program closes socket.
                print(e)
                break


# Client class calls listener thread to run perpetually and sender method as needed to send data.
# Changed so that connection is stored as class variable and can be accessed from other classes we define.
class Client(threading.Thread):

    sock = socket.socket()  # Store connection info outside of instances.

    def __init__(self, addr):
        super().__init__()
        self._address = addr
        data = Data()

    def run(self):
        with socket.create_connection(address) as srv:
            Client.sock = srv

            # Start Receive thread to listen for data from server.
            rcv = Receive(srv)
            rcv.start()

            print("Connected to server: %s:%d\n" % address)
            print("Menu:")
            print("1. Send user")
            print("2. Send event")
            print("3. Send message")
            print("4. Test database.")
            print("5. Request database.")
            print("6. Print users.")
            print("7. Reset database.")
            print("0. Exit")

            # TODO: Implement menu w/ UI
            # Create and send dummy class objects for testing.
            # If there are other clients connected, they should receive what is sent with their receive thread.
            selection = input("\nEnter selection:")
            while selection != "0":

                if selection == "1":
                    Data.add_user(User("Ryan", ["Constraint1"], ["Group1", "Group2"]))
                    Data.add_user(User("RyRy", ["Constraint1", "Constraint2"], ["Group2"]))

                elif selection == "2":
                    Client.Send(event("activity1", "time to shine", "florida"))
                    Client.Send(event("activity2", "afternoon", "texas"))

                elif selection == "3":
                    Client.Send(message("test_sender","test_recipient", "test_message"))
                    Client.Send(message("test_sender2", "test_recipient2", "test_message2"))

                elif selection == "4":  # Test database
                    pass

                elif selection == "5":  # Request database from server.
                    Data.db_request()

                elif selection == "6":  # Print users from local database
                    for user in Data().get_users():
                        print(user.name, user.constraints, user.groups)

                elif selection == "7":  # Deletes database and reinitializes.
                    Data.db_reset()

                selection = input("\nEnter selection:")

            srv.sendall("exit()".encode())  # Send exit command to server.

    # Creates a thread to accept an object and then encode or pickle before sending to server, depending on object type.
    # Attaches a 4 byte header to the object that specifies size
    # is_db is added to header, let's server know to only request from newest connection
    class Send(threading.Thread):
        def __init__(self, obj, is_db=0):
            super().__init__()
            self.obj = obj
            self.is_db = is_db

        def run(self):
            if type(self.obj) is str:
                self.obj = self.obj.encode()

            self.attach_header()
            Client.sock.sendall(self.obj)

        # Appends length of object being sent to beginning of it's byte string
        # Also adds a byte to specify if this is a database file.
        def attach_header(self):
            prefix = sys.getsizeof(self.obj)  # Get length of message so we can create header.
            prefix = prefix.to_bytes(4, "big")  # Convert length to bytes
            self.is_db = bytes([self.is_db])
            # Create bytearray to add header then convert back to bytes.
            self.obj = bytes(bytearray(prefix + self.is_db + self.obj))


if __name__ == '__main__':
    # TODO: Make host IP configurable by user.
    address = ("localhost", 55557)
    client = Client(address)
    client.start()
    print("Client started.")
