"""
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, 
and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.



NOTE: This is a SEPARATE FUNCTION that is NOT a method within the LinkedList class.  
    This means you need to indent the function all the way to the LEFT. 

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


  
 
  
def find_kth_from_end(ll, k):       
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while(fast):
        slow = slow.next
        fast = fast.next
    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

