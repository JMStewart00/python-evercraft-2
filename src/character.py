class Character:
    def __init__(self):
        self.name = 'Cletus'
        self.alignment = 'Good'

    def attack(self, roll, character_being_attacked):
        # what happens when an attack occurs
            # do something
        if roll == 20:
            character_being_attacked.take_damage()
    def take_damage(self):
        # something in here to affect self.hp