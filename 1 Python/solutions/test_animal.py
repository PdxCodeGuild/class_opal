from animal import Animal

testy = Animal('Testy', 'crab', 'click click', 100, 100, 100, 100)
angel = Animal('Angel', 'slow loris', 'love me', 1, 0, 0, 0)


def test_animal_creation():
    assert testy.name == 'Testy'
    assert testy.species == 'crab'
    assert testy.noise == 'click click'
    assert testy.hp == 100
    assert testy.damage == 100
    assert testy.defense == 100
    assert testy.speed == 100


def test_attack():
    assert type(testy.attack(angel)) is int
    assert testy.attack(angel) >= 50
    assert angel.attack(testy) == 0


def fight():
    ...
