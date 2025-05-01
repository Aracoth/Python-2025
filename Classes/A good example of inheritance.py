# A Custom exception: must inherit from 'Exception' class
class InvalidOperationError(Exception):
    pass


# A 'stream' of data class.
class Stream:
    def __init__(self):
        self.opened = False

    # open stream: or raise custom exception
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    # close: or raise exception
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


# Read data from a file
class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


# Read data from a network
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
