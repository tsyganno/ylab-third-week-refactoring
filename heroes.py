from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)


class Media:

    def __init__(self, name):
        self.name = name

    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')


class Gun:

    def fire_a_gun(self):
        print('PIU PIU')


class Laser:

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class Kick:

    def roundhouse_kick(self):
        print('Bump')


class Superman(SuperHero, Laser):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        if self.can_use_ultimate_attack:
            self.incinerate_with_lasers()

    def attack(self):
        if not self.can_use_ultimate_attack:
            pass


class Walker(SuperHero, Gun):

    def __init__(self):
        super(Walker, self).__init__('Chack Norris', True)

    def ultimate(self):
        if not self.can_use_ultimate_attack:
            pass

    def attack(self):
        self.fire_a_gun()
