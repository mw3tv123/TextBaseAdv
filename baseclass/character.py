from abc import ABC, ABCMeta, abstractmethod
import sentry_sdk
sentry_sdk.init("https://42508ae8bd6040a097bca6b8e500dcd8@sentry.io/1439826")


class Character(ABC):
    """Base class for monsters and player."""
    metaclass = ABCMeta
    @abstractmethod
    def move(self, *args, **keyword):
        pass

    @abstractmethod
    def interact(self, *args, **keyword):
        pass
