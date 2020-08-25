from abc import ABC, abstractmethod

class AbstractDirBuilder(ABC):
    @abstractmethod
    def build(self):
        raise NotImplementedError

    @abstractmethod
    def build_json(self, indent):
        raise NotImplementedError