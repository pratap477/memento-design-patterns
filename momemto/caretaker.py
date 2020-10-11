"""
CareTaker  class hold list of array all history states of the MemenTo.
It can store and retrieve stored MemenTO

"""


class CareTaker:
    # save class method
    def __init__(self):
        self.obj = ''

    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)
