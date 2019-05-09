import random
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")
try:
    import items
    import monsters
except ImportError:
    from . import items
    from . import monsters


class Tile(object):
    """Base class for all map tile"""
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def intro_text(self):
        """Appear when player enter this tile."""
        raise NotImplementedError()

    # def modify_player(self, player):
    #     """Show how player interact with object in this tile."""
    #     raise NotImplementedError()


class SpawnPoint(Tile):
    """Start point when player start a game."""
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    # def modify_player(self, player):
    #     """This room has no action on player."""
    #     pass

    def __str__(self):
        return "Start"


class TreasureChest(Tile):
    """This is where player find a treasure chess."""
    def __init__(self, x, y):
        self.number = random.randrange(5)
        items_list = [items.RustyKnife,
                      items.Gold,
                      items.Rock,
                      items.ClothArmor,
                      items.LeatherArmor,
                      items.ChainArmor,
                      items.SteelArmor,
                      ]
        self.item = [random.choice(items_list) for _ in range(self.number)]
        super().__init__(x, y)

    def intro_text(self):
        if self.number == 0:
            return """You found a treasure chess but there's nothing in it!"""
        return """You find a treasure chess at the corner. There is a {} in it.""".format(self.item)

    def __str__(self):
        return "Treasure"
    # def modify_player(self, player):
    #     self.add_treasure(player)


class EnemyRoom(Tile):
    """This is where player encounter enemy(s)."""
    def __init__(self, x, y, player):
        self.number = random.randrange(3) * player.level
        self.monster = [random.choice([monsters.Zombie, monsters.Orge]) for _ in range(self.number)]
        super().__init__(x, y)

    def intro_text(self):
        if self.monster:
            return "Unlucky for you, there're a group of {} monsters stay here.".format(len(self.monster))
        return "There're only corpse of defeated monsters."

    def __str__(self):
        return "Monsters"
    # def modify_player(self, player):
    #     for each in self.monster:
    #         if each.is_alive():
    #             player.health_point -= each.damage
    #             print("A {} inflicted {} damage to you.".format(each.name, each.damage))


class Path(Tile):
    """This is an empty space with nothing in it."""
    def intro_text(self):
        return "Empty space. Nothing in here."

    def modify_player(self, player):
        """This place has no action with player."""
        pass

    def __str__(self):
        return "Path"


class Wall(Tile):
    """This is an impassable wall."""
    def intro_text(self):
        return "An impassable wall. You cannot cross here! Find another way."

    def modify_player(self, player):
        """This place has no action with player."""
        pass

    def __str__(self):
        return "Wall"
