class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_nextNode(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def get_head_node(self):
        return self.head

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_nextNode(self.head)
        self.head = new_node

    def insert_end(self, new_value):
        new_node = Node(new_value)

        if not self.get_head_node():
            self.head = new_node
            return

        current = self.get_head_node()
        while current.get_next_node():
            current = current.get_next_node()
        current.set_nextNode(new_node)

    def display(self):
        strg = ""
        current = self.get_head_node()
        while current:
            if current.get_value() != None:
                strg += str(current.get_value()) + "-->"
            current = current.get_next_node()
        return strg

    def remove_value(self, value_to_remove):
        if not self.get_head_node():
            return

        current = self.get_head_node()

        if current.get_value() == value_to_remove:
            self.head = current.get_next_node()
            current = self.get_head_node()

        while current and current.get_next_node():

            if current.get_next_node().get_value() == value_to_remove:
                current.set_nextNode(current.get_next_node().get_next_node())
            else:
                current = current.get_next_node()

    def get_length(self):
        current = self.get_head_node()
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def reverse(self):
        prev = None
        current = self.get_head_node()
        while current:
            next_node = current.get_next_node()
            current.set_nextNode(prev)
            prev = current
            current = next_node

        self.head = prev

    def isPalindrome(self):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        current = self.head
        values = []
        while current:
            values.append(current.get_value())
            current = current.get_next_node()

        current = self.head
        while current:
            if current.get_value() != values.pop():
                return False
            current = current.get_next_node()
        return True


ll = LinkedList(2)
ll.insert_beginning(3)
ll.insert_beginning(5)

print(ll.display())

ll.insert_end(10)
print(ll.display())
print(ll.get_length())

ll.reverse()
print(ll.display())


ll.insert_end(3)
ll.insert_end(2)
ll.insert_end(10)


print(ll.display())
print(ll.isPalindrome())
