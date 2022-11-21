class Compass:
    def __init__(self, heading) -> None:
        ...

    def get_direction(self) -> str:
        '''Find the nearest cardinal direction of the current heading'''
        direction = ...

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

    def turn(self, degrees, direction) -> None:
        ...
        print(
            f'Turned {degrees} degrees {direction}. New heading is {self.heading}, pointed roughly {self.get_direction()}')

    def __add__(self, degrees: int) -> int:
        '''Add two different compass headings together'''
        ...

    def __sub__(self, degrees: int) -> int:
        '''Subract one compass heading from another'''
        ...

    def __eq__(self, other) -> bool:
        '''Determine whether two compasses have the same heading'''
        ...

    def __gt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __lt__(self, other):
        raise TypeError('Cardinal directions cannot be greater or less than')

    def __str__(self) -> str:
        ...


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
