import config

class Robot(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "North"

    # PLACE will put the toy robot on the table in position X,Y and facing NORTH,
    # SOUTH, EAST or WEST
    def place(self, X, Y, Facing):

        if Facing.lower() not in config.direction:
            print("Not Valid Direction: {0}, please use {1}".format(Facing, config.direction))
            return 0
        if not self._in_range(X):
            return 0
        if not self._in_range(Y):
            return 0

        self.x = X
        self.y = Y
        self.facing = Facing

        return 1

    # MOVE will move the toy robot one unit forward in the direction it is
    # currently facing.
    def move(self):
        # 0,4	1,4  2,4  3,4	 4,4
        # 0,3	1,3	 2,3  3,3	 4,3
        # 0,2	1,2	 2,2  3,2	 4,2
        # 0,1	1,1	 2,1  3,1	 4,1
        # 0,0	1,0	 2,0  3,0	 4,0

        if self.facing.lower() == 'north':
            if self._in_range(self.y + 1):
                self.y += 1
        if self.facing.lower() == 'east':
            if self._in_range(self.x + 1):
                self.x += 1
        if self.facing.lower() == 'south':
            if self._in_range(self.y - 1):
                self.y -= 1
        if self.facing.lower() == 'west':
            if self._in_range(self.x - 1):
                self.x -= 1

        return 1

    # LEFT and RIGHT will rotate the robot 90 degrees in the
    # specified direction without changing the position of the robot
    # Turn 90 degrees left
    def left(self):
        # direction = ["north", "east", "south", "west"]
        compass_direction = config.direction.index(self.facing.lower())
        if compass_direction > 0:
            self.facing = config.direction[compass_direction-1]
        elif compass_direction == 0:
            self.facing = config.direction[-1]
        else:
            print("Some Error")
        return 1

    # Turn 90 degrees right
    def right(self):
        # direction = ["north", "east", "south", "west"]
        compass_direction = config.direction.index(self.facing.lower())
        if compass_direction == len(config.direction)-1:
            self.facing = config.direction[0]
        elif 0 <= compass_direction <= len(config.direction)-1:
            self.facing = config.direction[compass_direction+1]
        else:
            print("Some Error")
        return 1

    # REPORT will announce the X,Y and F of the robot
    def report(self):
        print("Output: {0}, {1}, {2}".format(self.x, self.y, self.facing))


    # Test if robot will fall if moved there
    def _in_range(self, coordinate):
        if coordinate in range(0,5):
            return 1
        return 0

