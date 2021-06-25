from dataclasses import dataclass


@dataclass
class Computer:

    def display(self):
        print("------")
        print(f'My Computer version {self.version}: ')
        print(f'Case: {self.case}')
        print(f'Mainboard: {self.mainboard}')
        print(f'CPU: {self.cpu}')
        print("------")
