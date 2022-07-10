from places import Kostroma, Tokyo


class AntagonistFinder(Kostroma, Tokyo):

    def get_antagonist(self, place):
        place.find_antagonist()
