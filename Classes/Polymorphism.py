from abc import ABC, abstractmethod


# Base class with abstractmethod: draw
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# a function for controlling all controls
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
# a list of both controls: dropdownlist and textbox
draw([ddl, textbox])
