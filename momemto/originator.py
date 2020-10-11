"""
Originator class support getter and setter object values from the currently
targeted Memento. Create new MemenTo and assign new values to them

"""


from momemto import MemenTo


class Originator:
    def __init__(self, file, content):
        self.file = file
        self.content = ''

    def write(self, string):
        self.content += string

    def save(self):
        return MemenTo(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content
