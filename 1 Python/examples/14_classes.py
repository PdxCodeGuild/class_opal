import random
from math import floor


class Animal:
    # class names should be singular, WordCase
    def __init__(self, name, species, noise, hp, attack, defense, speed):
        '''
        Class Animal includes important information about each declared animal
        - name: The animal's name
        - species: The animal's species
        - noise: The noise that the animal makes
        - hp: Hit points
        - damage: The amount of damage their attack does
        - defense: Defense gets subtracted from total damage done to self
        - speed: Speed determines how often the animal can attack
        '''
        # after passing in the attributes, we assign them to "self"
        # self is like "this particular Animal"
        self.name: str = name
        self.species: str = species
        self.noise: str = noise
        self.hp: int = hp
        self.damage: int = attack
        self.defense: int = defense
        self.speed: int = speed
        is_animal: bool = True  # attributes can be hard coded

    def make_noise(self) -> None:
        print((self.noise + ' ') * 3)

    def attack(self, opponent) -> int:
        '''Attempt to attack opponent, returns damage done'''
        # speed is the % of rounds that they will attack
        if random.random()*100 <= self.speed:
            this_attack: float = random.uniform(self.damage/2, self.damage)
            damage_done: int = floor(this_attack - opponent.defense)
            return damage_done
        return 0

    def fight(self, opponent):
        '''Initiate a fight with opponent, print the winner'''
        while self.hp > 0 and opponent.hp > 0:
            self_attack = max((self.attack(opponent), 0))
            opponent.hp -= self_attack
            print(
                f'{self.name} did {self_attack} points of damage to {opponent.name}')

            opponent_attack = max((opponent.attack(self), 0))
            self.hp -= opponent_attack
            print(
                f'{opponent.name} did {opponent_attack} points of damage to {self.name}')
        winner = self
        if self.hp < opponent.hp:
            winner = opponent
        print(f'{winner.name} wins the fight')

    def __str__(self) -> str:
        return f'This {self.species} is named {self.name}'


kyle = Animal('Kyle', 'honey badger', 'rawr', 100, 50, 20, 90)
lucy = Animal('Lucy', 'hippopotamus', '....', 200, 90, 30, 5)

# kyle.fight(lucy)
# lucy.fight(kyle)


class Kitten(Animal):
    '''
    Kitten "inherits from" the Animal class
    Kitten is the "subclass" and Animal is the "superclass"
    The parent/superclass can be accessed with the super() function
    '''
    # You can overwrite the parent's __init__ function or not, it's optional
    # If you do, you can use the parent's __init__ if you want

    def __init__(self, name, hp, attack, defense, speed):
        super().__init__(name, 'baby cat', 'purrr', hp, attack, defense, speed)
        self.is_the_cutest = True
        self.hp = 0

    # ... or you can add all the attributes manually
    # def __init__(self, name):
    #     self.name = name
    #     self.species = 'baby cat'
    #     self.noise = 'purrrr'
    #     self.hp = 5
    #     self.damage = 0
    #     self.defense = 5
    #     self.speed = 5

    # Writing a new method definition will "override" the parent's method
    def attack(self, opponent) -> int:
        print(f'{self.name} just wants to snuggle')
        return -100

    def fight(self, opponent) -> None:
        print(f'{self.name} never wanted to hurt anybody :(')


snowball = Kitten('Snowball')
# We didn't overwrite the __str__ method or the make_noise method
# so those will come directly from the parent (Animal) class
print(snowball)
snowball.make_noise()

# We did overwrite the fight method, so this will do something different from the parent
snowball.fight(kyle)
