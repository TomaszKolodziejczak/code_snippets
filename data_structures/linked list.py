from node import Node


# head - first element of the list
# tail - last element of the list


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_node_beginning(self, new_value):  # O(1)
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, value_to_remove):  # O(n)
        current_node = self.head_node

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()

        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def stringfy_list(self):  # O(n)
        string_list = ""
        current_node = self.get_head_node()

        while current_node:
            string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()

        return string_list


if __name__ == "__main__":
    l = LinkedList(34)
    l.insert_node_beginning(20)
    l.insert_node_beginning(45)
    l.insert_node_beginning(23)

    print(l.stringfy_list())

    l.remove_node(20)

    print(l.stringfy_list())
