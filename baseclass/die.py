from random import randint
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")


class Die(object):
    """Represents single die."""
    def __init__(self, sides=6):
        """Set the number of sides (defaults to six)."""
        self.sides = sides

    def roll(self):
        """Roll the die."""
        return randint(1, self.sides)
