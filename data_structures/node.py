class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


if __name__ == "__main__":
    n1 = Node(33)
    n2 = Node(34, n1)

    print(n2.get_next_node().get_value())
