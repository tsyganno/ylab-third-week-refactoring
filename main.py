from typing import Union
from heroes import Superman, SuperHero, Media, Walker
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, Media, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    Media(hero.name).create_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Media, Kostroma())
    print('-' * 20)
    save_the_place(Walker(), Media, Tokyo())
