import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")


class Item(object):
    """The base class for all item."""
    def __init__(self, name, description, value):
        """Constructor"""
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        """This function use for debug."""
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    """"""
    def __init__(self, amount):
        """Constructor"""
        self.amount = amount
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amount)),
                         value=self.amount)


class Weapon(Item):
    """Base class for all weapons."""
    def __init__(self, name, description, value, damage, duration, attack_range):
        """Constructor"""
        self.damage = damage
        self.duration = duration
        self.attack_range = attack_range
        super().__init__(name, description, value)

    def __str__(self):
        """For debug only."""
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDuration:{}\nAttack range: {}".format(self.name,
                                                                                            self.description,
                                                                                            self.value,
                                                                                            self.damage,
                                                                                            self.duration,
                                                                                            self.attack_range,
                                                                                            )


class Rock(Weapon):
    """Rock is a beginner weapon, low damage, range attack."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5,
                         duration=30,
                         attack_range=3,
                         )


class RustyKnife(Weapon):
    """Rusty Knife is a beginner weapon, low damage, melee attack."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Rusty Knife",
                         description="A small knife with some rust. A suitable for new adventurer.",
                         value=0,
                         damage=5,
                         duration=30,
                         attack_range=1
                         )


class Armor(Item):
    """Base class for all armor."""
    def __init__(self, name, description, value, duration, armor):
        """Constructor"""
        self.duration = duration
        self.armor = armor
        super().__init__(name=name, description=description, value=value)

    def __str__(self):
        """For debug only."""
        return "{}\n=====\n{}\nValue: {}\nArmor: {}\nDuration:{}".format(self.name,
                                                                         self.description,
                                                                         self.value,
                                                                         self.armor,
                                                                         self.duration,
                                                                         )


class ClothArmor(Armor):
    """Clothes texture are basic material."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Cloth Armor",
                         description="Armor made from cloth. Suitable for beginner.",
                         value=0,
                         armor=1,
                         duration=30,
                         )


class LeatherArmor(Armor):
    """Leather texture are improved material."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Leather Armor",
                         description="Armor made from leather. Improve combat effectiveness.",
                         value=10,
                         armor=3,
                         duration=45,
                         )


class ChainArmor(Armor):
    """Armor made from chain of metal."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Chain Armor",
                         description="Armor made from chain of metal. Greater improve combat effectiveness.",
                         value=20,
                         armor=5,
                         duration=60,
                         )


class SteelArmor(Armor):
    """Steel material are advanced material."""
    def __init__(self):
        """Constructor"""
        super().__init__(name="Steel Armor",
                         description="Armor made from steel. Combat effectiveness step into another level.",
                         value=30,
                         armor=10,
                         duration=80,
                         )
