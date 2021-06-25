from dataclasses import dataclass

from builder_pattern.abc_computer_builder import AbcComputerBuilder


@dataclass
class Director:
    _builder: AbcComputerBuilder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.set_computer_version()
        self._builder.get_case()
        self._builder.get_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()

    def get_computer(self):
        return self._builder.get_computer()