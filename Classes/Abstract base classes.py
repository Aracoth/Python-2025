# This allows you to create abstract classes
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# base class derived from the ABC class
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # a global abstract read class
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# all subclasses must use the 'read' method
class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


stream = MemoryStream()
stream.open()
