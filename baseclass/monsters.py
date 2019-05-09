import random
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")
try:
    from character import Character
except ImportError:
    from .character import Character


class Monster(Character):
    """Base class for all type of monster"""
    def __init__(self, name, health_point, armor, damage):
        """Constructor"""
        self.name = name
        self.health_point = health_point
        self.armor = armor
        self.damage = damage

    def move(self):
        pass

    def interact(self):
        pass

    def is_alive(self):
        """Return True if monster still alive (HP > 0), other wise False."""
        return self.health_point < 0

    def __str__(self):
        """This function is used for debug."""
        return "Name: {}\nHP: {}\nDamage: {}\nArmor: {}\nLevel: {}".format(self.name, self.health_point, self.damage, self.armor, self.level)


class Zombie(Monster):
    """Zombie class."""
    def __init__(self, player_level):
        super().__init__(name="Zombie",
                         health_point=(random.randrange(10, 15) * player_level),
                         armor=(random.randrange(3) * player_level),
                         damage=(random.randrange(3) * player_level),
                         )


class Orge(Monster):
    """Orge class."""
    def __init__(self, player_level):
        super().__init__(name="Orge",
                         health_point=(random.randrange(20, 30) * player_level),
                         armor=(random.randrange(3) * player_level),
                         damage=(random.randrange(3, 5) * player_level),
                         )


class Ghost(Monster):
    """Ghost class."""
    def __init__(self, player_level):
        super().__init__(name="Ghost",
                         health_point=(random.randrange(20, 30) * player_level),
                         armor=(random.randrange(3) * player_level),
                         damage=(random.randrange(3, 5) * player_level),
                         )
