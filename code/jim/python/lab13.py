class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading

    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = int(round(self.heading / 45) * 45)

        if direction == 0:
            return 'N'
        elif direction == 45:
            return 'NE'
        elif direction == 90:
            return 'E'
        elif direction == 135:
            return 'SE'
        elif direction == 180:
            return 'S'
        elif direction == 225:
            return 'SW'
        elif direction == 270:
            return 'W'
        elif direction == 315:
            return 'NW'
        else:
            return 'Invalid direction'

    def turn(self, degrees, direction) -> None:
        if direction == 'left':
            self.heading = self.__sub__(degrees)
        else:
            self.heading = self.__add__(degrees) 
        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        return (self.heading + degrees) % 360

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another'''
        return (self.heading - degrees) % 360

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        return self.get_direction() == other.get_direction()

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        return f"This compass has heading {self.heading}, pointed roughly {self.get_direction()}"
        

'''
DON'T CHANGE ANYTHING BELOW HERE
'''
ne = Compass(40)
sw = Compass(240)
e = Compass(104)


def test_get_direction():
    assert ne.get_direction() == 'NE'
    assert sw.get_direction() == 'SW'
    assert e.get_direction() == 'E'


def test_turn():
    heading1 = Compass(90)
    heading1.turn(190, 'left')
    assert heading1.heading == 260
    heading1.turn(10, 'right')
    assert heading1.heading == 270

    heading2 = Compass(320)
    heading2.turn(150, 'right')
    assert heading2.heading == 110
    heading2.turn(120, 'left')
    assert heading2.heading == 350


def test_addition():
    assert ne + 30 == 70
    assert sw + 200 == 80
    assert sw + 120 == 0


def test_subtraction():
    assert ne - 90 == 310
    assert ne - 40 == 0
    assert sw - 10 == 230


def test_equality():
    new_sw = Compass(240)
    assert new_sw == sw
