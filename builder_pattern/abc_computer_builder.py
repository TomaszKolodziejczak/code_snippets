from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

from builder_pattern.computer import Computer


@dataclass
class AbcComputerBuilder(ABC):

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abstractmethod
    def set_computer_version(self):
        pass

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def get_mainboard(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass
