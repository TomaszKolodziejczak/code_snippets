from dataclasses import dataclass

from builder_pattern.abc_computer_builder import AbcComputerBuilder


@dataclass
class BComputerBuilder(AbcComputerBuilder):

    def set_computer_version(self):
        self._computer.version = "B"

    def get_case(self):
        self._computer.case = "Metal Case"

    def get_mainboard(self):
        self._computer.mainboard = "beta 231"
        self._computer.cpu = "Intel"
        self._computer.memory = "8GB"

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_disc = "64GB"
