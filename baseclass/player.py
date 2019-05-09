import random
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")
try:
    from character import Character
    from die import Die
except ImportError:
    from .character import Character
    from .die import Die


class Player(Character):
    """Base class for playable character define basic interaction."""
    levels_list = [  # List of all level with experiments need to advance to next level
        20,  # 0
        36,  # 16 + 0
        53,  # 16 + 1
        71,  # 16 + 2
        90,  # 16 + 3
        110,  # 16 + 4
        131,  # 16 + 5
        153,  # 16 + 6
        176,  # 16 + 7
        200,  # 16 + 8
    ]
    dice = Die()

    def __init__(self, name, health_point, armor, attack, class_type, position):
        """Constructor"""
        self.name = name
        self.health_point = health_point
        self.armor = armor
        self.attack = attack
        self.class_type = class_type
        self.current_exp = 0
        self.level = 1  # Start level
        self.inventory = None
        self.position = position

    def move(self, direction):
        """
        Player move actions. Player are able to move 4 directions: NORTH, EAST, SOUTH, WEST.
        Each turn player are only move 1 time and advance 1 tile.
        """
        pass

    def interact(self):
        """
        Player interact actions. Player are able to decide which action will take place next turn.
        List of actions:
            - Attack;
            - Cast skills;
            - Use item;
            - ???
            - ...
        """
        pass

    def level_up(self):
        """Level up if player acquire enough current level experiments."""
        if self.current_exp >= self.levels_list[self.level]:
            self.level += 1

    def improve_stats(self):
        """Stats improvement when level up."""
        pass

    def __str__(self):
        """This function use for debug only."""
        return "Name: {}\nHP: {}\nArmor: {}\nAttack: {}\nClass: {}\nLevel: {}".format(self.name,
                                                                                      self.health_point,
                                                                                      self.armor,
                                                                                      self.attack,
                                                                                      self.class_type,
                                                                                      self.level,
                                                                                      )


class Fighter(Player):
    """Fighter class"""
    def __init__(self, name, position):
        """Constructor"""
        super().__init__(name=name,
                         health_point=(random.randrange(15, 20) + self.dice.roll()),
                         armor=(3 + self.dice.roll()),
                         attack=self.dice.roll(),
                         class_type="Fighter",
                         position=position,
                         )

    def improve_stats(self):
        self.health_point += 0
        self.armor += 0
        self.attack += 0


class Archer(Player):
    """Archer class"""
    def __init__(self, name, position):
        """Constructor"""
        super().__init__(name=name,
                         health_point=(random.randrange(5, 10) + self.dice.roll()),
                         armor=self.dice.roll(),
                         attack=(random.randrange(2, 7) + self.dice.roll()),
                         class_type="Archer",
                         position=position,
                         )

    def improve_stats(self):
        self.health_point += 0
        self.armor += 0
        self.attack += 0


class Assassin(Player):
    """Assassin class"""
    def __init__(self, name, position):
        """Constructor"""
        super().__init__(name=name,
                         health_point=(random.randrange(10, 15) + self.dice.roll()),
                         armor=(1 + self.dice.roll()),
                         attack=(random.randrange(2, 5) + self.dice.roll()),
                         class_type="Assassin",
                         position=position,
                         )

    def improve_stats(self):
        self.health_point += 0
        self.armor += 0
        self.attack += 0
