import random

class Character:

    def __init__( self , name ):
        self.name = name
        self.strength = 7
        self.speed = 7
        self.health = 75

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , target):
        roll = random.randint(1, 20)
        if roll == 20:
            target.health -= (self.strength * 2)
            print(f'{self.name} surprisingly landed a good shot, critical hit! {target.name} left with {target.health} health')
        elif roll > target.speed:
            target.health -= self.strength
            print(f'{target.name} takes {self.strength} damage, left with {target.health} health.')
            return self
        elif roll < target.speed:
            target.miss()

    def heal(self):
        self.health += 13
        print(f'{self.name} calls a time out and applies a bandaid! Health is now {self.health}')

    def action(self, target):
        if self.health < 80:
            roll = random.randint(1, 20)
            if roll <= 5:
                self.heal()
            elif roll > 5:
                self.attack(target)
        else:
            self.attack(target)

    def surrender(self):
        print(f"{self.name} has surrendered!!!")

    @classmethod

    def miss(cls):
        print('The random fan slipped on the ground and managed to avoid an attack!')

    def intro():
        print('Random fan wanders into ring!')

    @staticmethod

    def crowd(victor):
        print(f'Crowd is awestruck at {victor}!')