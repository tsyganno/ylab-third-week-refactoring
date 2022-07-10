from abc import abstractmethod, ABC


class Place(ABC):

    @abstractmethod
    def find_antagonist(self):
        pass


class Kostroma(Place):
    city_name = 'Kostroma'

    def find_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def find_antagonist(self):
        print('Godzilla stands near a skyscraper')
