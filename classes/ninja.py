import random

from classes.character import Character

class Ninja(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 13
        self.health = 100

    def attack( self , target ):
        roll = random.randint(1, 20)
        if roll == 20:
            target.health -= (self.strength * 2)
            print(f'{self.name} added poison to his weapon, critical hit! {target.name} left with {target.health} health')
        elif roll >= target.speed:
            target.health -= self.strength
            print(f'{target.name} takes {self.strength} damage, left with {target.health} health.')
            return self
        elif roll < target.speed:
            target.miss()

    def heal(self):
        self.health += 20
        print(f'{self.name} applied Tiger Balm and feels limber! Health is now {self.health}')

    @classmethod

    def miss(cls):
        print('The ninja champion deployed a smoke bomb!')

    def intro():
        print('Ninjas appear in a puff of smoke!')

    @staticmethod

    def crowd(victor):
        print(f'Ninjas cheer for {victor}!')

class Assassin(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 12
        self.health = 150

    @classmethod

    def miss(cls):
        print('The assassin champion faded from view!')

    def intro():
        print('Assassins appear from the shadows!')
    
    @staticmethod

    def crowd(victor):
        print(f'Assassins cheer for {victor}!')
