from abc import ABC, abstractmethod


# UIControl is not needed, but good practice
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


# object must be iterable
def draw(controls):
    for control in controls:
        control.draw()
