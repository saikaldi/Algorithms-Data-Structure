class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def display(self):
        linked_list = ""
        current = self.get_head_node()
        while current:
            if current.get_value() != None:
                linked_list += str(current.get_value()) + "-> "
            current = current.get_next_node()
        return linked_list

    def remove_value(self, value_to_remove):
        if not self.get_head_node():
            print("Empty")
            return
        current = self.get_head_node()
        if current.get_value() == value_to_remove:
            self.head_node = current.get_next_node()
        else:
            while current:
                next_node = current.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current.set_next_node(next_node.get_next_node())
                    return
                current = current.get_next_node()


ll = LinkedList(2)
ll.insert_beginning(3)
ll.insert_beginning(5)
ll.insert_beginning(8)
ll.insert_beginning(10)
ll.insert_beginning(12)

print(ll.display())
ll.remove_value(5)
print(ll.display())
