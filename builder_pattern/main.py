from builder_pattern.a_computer_builder import AComputerBuilder
from builder_pattern.b_computer_builder import BComputerBuilder
from builder_pattern.director import Director

# computer ver 1
builder_1 = AComputerBuilder()
d = Director(builder_1)
d.build_computer()
computer = d.get_computer()
computer.display()

# computer ver 2
builder_2 = BComputerBuilder()
d = Director(builder_2)
d.build_computer()
computer = d.get_computer()
computer.display()
