import sys
import re
from robot import Robot

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    """The robot routine."""

    robot = Robot.Robot()

    place = raw_input("Place Robot:")
    wordList = re.sub("[^\w]", " ",  place).split()

    while not place.lower().startswith('place'):
        place = raw_input("Place Robot2:")
        wordList = re.sub("[^\w]", " ",  place).split()

    if len(wordList) == 4:
        robot.place(int(wordList[1]),int(wordList[2]),wordList[3])

    while(1):
        command = raw_input("Enter Command:")

        lowercase_command = command.lower()

        if lowercase_command == 'q':
            sys.exit(0)
        if lowercase_command == 'move':
            robot.move()
        if lowercase_command == 'left':
            robot.left()
        if lowercase_command == 'right':
            robot.right()
        if lowercase_command == 'report':
            robot.report()
        if lowercase_command.startswith('place'):
            wordList = re.sub("[^\w]", " ",  command).split()
            if len(wordList) == 4:
                robot.place(int(wordList[1]),int(wordList[2]),wordList[3])


if __name__ == "__main__":
    main()
