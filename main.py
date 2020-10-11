"""
This means that if this script is executed then
main() will be executed

Memento Design pattern is the way to store previous states on Object
easily
"""

from momemto import Originator, CareTaker


if __name__ == '__main__':
    """  create care taker object """
    care_taker = CareTaker()

    """ create Originator object """
    writer = Originator('Hello.txt', '')

    writer.write('Hello! how are you!!!')
    print(writer.content + "\n\n")

    care_taker.save(writer)

    """again write using the writer """
    writer.write(" Are you fun with this pattern \n")

    print(writer.content + "\n\n")

    """undo the file"""
    care_taker.undo(writer)

    print(writer.content + "\n\n")
