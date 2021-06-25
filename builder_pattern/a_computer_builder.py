from dataclasses import dataclass

from builder_pattern.abc_computer_builder import AbcComputerBuilder


@dataclass
class AComputerBuilder(AbcComputerBuilder):

    def set_computer_version(self):
        self._computer.version = "A"

    def get_case(self):
        self._computer.case = "Transparent Case"

    def get_mainboard(self):
        self._computer.mainboard = "ZZZ 5000"
        self._computer.cpu = "AMD 1K456"
        self._computer.memory = "512GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_disc = "Seagate 512GB"