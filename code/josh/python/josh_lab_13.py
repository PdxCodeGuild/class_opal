# Lab 13: Compass


class Compass:
    def __init__(self, heading) -> None:
        self.heading = heading

# Returns 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', or 'NW' depending upon range of nearest heading
    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = int(round(self.heading / 45) * 45)
        
        match direction:
            case 0:
                return 'N'
            case 45:
                return 'NE'
            case 90:
                return 'E'
            case 135:
                return 'SE'
            case 180:
                return 'S'
            case 225:
                return 'SW'
            case 270:
                return 'W'
            case 315:
                return 'NW'

# Turns 'Compass' left or right based upon user input of turn direction and amount of turn
    def turn(self, degrees, direction) -> None:
        if direction == 'left':
            if self.heading - degrees < 0:
                self.heading = self.heading - degrees + 360
            else:
                self.heading = self.heading - degrees
        elif direction == 'right':
            if self.heading + degrees > 359:
                self.heading = self.heading + degrees - 360
            else:
                self.heading = self.heading + degrees
        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

# Returns remainder when heading is over 360 degrees
    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        return (self.heading + degrees) % 360


# Returns remainder when heading is below 0 degrees


    def __sub__(self, degrees: int) -> int:
        '''Subtract one compass heading from another'''
        return (self.heading - degrees) % 360


# Override the __eq__ method to return True when two compasses with the same heading are compared.


    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        if self.heading == other.heading:
            return True
        else:
            return False

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        return f'Hello there.  You are currently heading {self.get_direction()}.  Enjoy your trip!'


'''Automated tests for class Compass (DO NOT CHANGE ANYTHING BELOW THIS LINE!) '''

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

    heading3 = Compass(2)
    heading3.turn(1, 'left')
    assert heading3.heading == 1
    heading3.turn(1, 'right')
    assert heading3.heading == 2


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
    assert sw != e
