import random
from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    CALL_ANGEL_OR_CROW = 5
    RECALL_HERO = 6
    STUN_BOSS = 7
    ACCEPT_DAMAGE = 8

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(2, 5)
            boss.health -= self.damage * coefficient
            print(f'Warrior hits critically {self.damage * coefficient}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health += self.__heal_points
                    print(f'healed for {self.__heal_points}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        pass


class Druid(Hero):
    def __init__(self, name, health, damage):
        super(Druid, self).__init__(name, health, damage, SuperAbility.CALL_ANGEL_OR_CROW)

    def apply_super_power(self, boss, heroes):
        angel_or_crow = random.choice([round_number])
        if angel_or_crow == 1:
            if boss.health < boss.health // 2:
                print("CALL TO CROW")
                boss.damage += boss.damage // 2

        elif angel_or_crow == 2:
            print('CALL TO ANGEL')
            for hero in heroes:
                hero.health += 10


class Witcher(Hero):
    def __init__(self, name, health, damage=0):
        super(Witcher, self).__init__(name, health, damage, SuperAbility.RECALL_HERO)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0 and boss.health > 0:
                hero.health += self.health
                self.health = 0
                print(f"{self.name} отдал жизнь {hero.name}")


class Thor(Hero):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, SuperAbility.STUN_BOSS)

    def apply_super_power(self, boss, heroes):
        stun = [1, 2, 3]
        b = random.choice(stun)
        if b == 1:
            boss.damage = 0
            print("STUN BOSS")
        else:
            boss.damage = 50

class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(5, 11)
        print(f"Boost: {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_point


class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super(Golem, self).__init__(name, health, damage, SuperAbility.ACCEPT_DAMAGE)
        self.protection = protection

    def apply_super_power(self, boss, heroes):
        print(f"protection - {self.protection}")
        for hero in heroes:
            if hero.health > 0:
                self.protection = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.protection
                else:
                    hero.health -= boss.damage


round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Devil', 1000, 50)
    warrior = Warrior('Axe', 270, 10)
    doc = Medic('Invoker', 250, 5, 15)
    magic = Magic('Dambldor', 280, 15)
    berserk = Berserk('Tigril', 260, 10)
    assistant = Medic('Swan', 290, 5, 5)
    thor = Thor('thor', 200, 30)
    witcher = Witcher('witcher', 100)
    druid = Druid('druid', 200, 20)


    heroes = [warrior, doc, magic, berserk, assistant, thor, witcher, druid]

    print_statistics(boss, heroes)
    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()
