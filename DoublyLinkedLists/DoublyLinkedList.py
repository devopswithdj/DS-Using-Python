class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(temp.value)
            temp = temp.next
        print(" -> ".join(map(str, nodes)))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

DLL = DoublyLinkedList(7)
DLL.print_list()

print("<<<<<<<<<Trying out Append method>>>>>>>>>")
DLL.append(6)
DLL.print_list()