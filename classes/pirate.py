import random

from classes.character import Character

class Pirate(Character):

    def __init__( self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 10
        self.health = 100

    def attack ( self , target ):
        roll = random.randint(1, 20)
        if roll == 20:
            target.health -= (self.strength * 2)
            print(f'{self.name} uses hand cannon, critical hit! {target.name} left with {target.health} health')
        elif roll > target.speed:
            target.health -= self.strength
            print(f'{target.name} takes {self.strength} damage, left with {target.health} health.')
            return self
        elif roll < target.speed:
            target.miss()

    def heal(self):
        self.health += 20
        print(f'{self.name} eats an orange! Health is now {self.health}')

    @classmethod

    def miss(cls):
        print('The pirate champion blocks with his cutlass!')

    def intro():
        print('Pirates cross their gangplank!')

    @staticmethod

    def crowd(victor):
        print(f'Pirates cheer for {victor}!')

class Swashbuckler(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.speed = 12
        self.health = 150

    @classmethod

    def miss(cls):
        print('The swashbuckler champion blocks with his buckler!')

    def intro():
        print('Swashbucklers swing in off a rope!')

    @staticmethod

    def crowd(victor):
        print(f'Swashbucklers cheer for {victor}!')