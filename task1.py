class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        current = self.head
        res = []
        while current:
            res.append(current.data)
            current = current.next
        print(res)
    
    def reverse(self):
        if not self.head or not self.head.next:
            return
      
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head
    
    def concat(self, llist):
        current = llist.head
        while current:
            self.insert_at_end(current.data)
            current = current.next
        self.insertion_sort()
            

llist = LinkedList()
for i in [5,7,3,8,9,11,2]:
    llist.insert_at_end(i)

print("Зв'язний список")
llist.print_list()

llist.reverse()   
print("\n Зв'язний список після реверсування ")
llist.print_list()

llist.insertion_sort()
print("\n Зв'язний список після sort ")
llist.print_list()


llist1 = LinkedList()
for i in [1, 23, 17, 33, 4]:
    llist1.insert_at_end(i)

llist.concat(llist1)
print("\n Зв'язний список після concat ")
llist.print_list()

    
