#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from abc import ABC
import random
import sys


class GameUnit(ABC):
    """
    Базовый класс для игровых юнитов
    Имеет поля "Уникальный id" и "Принадлежность к команде"
    """
    def __init__(self, unique_id, team):
        self.unique_id = unique_id
        self.team = team


class Hero(GameUnit):
    """
    Класс "Герой", наследуется от игрового юнита
    Имеет поле "Уровень"
    """
    def __init__(self, unique_id, team):
        super().__init__(unique_id, team)
        self.level = 1

    def level_up(self):
        """
        Метод для повышения собственного уровня на 1
        """
        self.level += 1


class Soldier(GameUnit):
    """
    Класс "Солдат", наследуется от игрового юнита
    Имеет поле "Следует за героем" - в этом поле указывается объект "Герой", за которым следует текущий солдат
    """
    def __init__(self, unique_id, team):
        super().__init__(unique_id, team)
        self.follows_hero = None

    def follow(self, hero: Hero):
        """
        Метот для следования за героем
        """
        self.follows_hero = hero


class UniqueIdGenerator:
    """
    Класс для генерации последовательного id
    """
    def __init__(self):
        # Счетчик начинается с 0
        self.index = 0

    def generate_unique_id(self):
        # При каждой генерации нового числа - увеличиваем текущий счетчик на 1
        self.index = self.index + 1
        return self.index


if __name__ == '__main__':
    # Генератор уникальных id
    id_generator = UniqueIdGenerator()
    # Герой красной команды
    red_hero = Hero(id_generator.generate_unique_id(), "red")
    # Герой синей команды
    blue_hero = Hero(id_generator.generate_unique_id(), "blue")

    soldiers_count = int(input("Введите общее количество солдат: "))
    # Два массива для хранения солдатов красной и синей команд
    red_soldiers = []
    blue_soldiers = []

    # Генерируем героев
    for x in range(soldiers_count):
        # Случайным образом определяем к какой команде будет причислен созданный герой
        team = "red" if random.randint(1, 100) % 2 == 0 else "blue"
        new_soldier = Soldier(id_generator.generate_unique_id(), team)

        team_to_append = red_soldiers if team == "red" else blue_soldiers
        team_to_append.append(new_soldier)

    if len(red_soldiers) == 0 and len(blue_soldiers) == 0:
        print("Ни одна из команд не содержит солдатов")
        sys.exit()

    # Определяем в какой команде большее количество солдат
    [hero, soldiers] = [red_hero, red_soldiers] if len(red_soldiers) > len(blue_soldiers) else [blue_hero,
                                                                                                blue_soldiers]

    # Повышаем уровень этому герою
    hero.level_up()
    # Самый первый солдат теперь следует за своим героем
    soldiers[0].follow(hero)

    print(f"Герой: (unique_id: {hero.unique_id}, level: {hero.level}, team: {hero.team})")
    print(f"Идентификатор солдата, который следует за героем: {soldiers[0].unique_id}")
