class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reverse(self):
        l = LinkedList()
        if self.head is None:
            print('List is empty')
            return
      
        cur = self.head
        while cur:
            l.insert_at_beginning(cur.data)
            self.delete_node(cur.data)
            cur = cur.next
            
        current = l.head
        while current:
            self.insert_at_end(current.data)
            current = current.next
            
    # def insertion_sort(self):
    #     current = self.head
    #     lst = []
    #     while current:
    #         lst.append(current.data)
    #         self.delete_node(current.data)
    #         current = current.next
            
    #     for i in range(1, len(lst)):
    #         key = lst[i]
    #         j = i-1
    #         while j >=0 and key < lst[j] :
    #                 lst[j+1] = lst[j]
    #                 j -= 1
    #         lst[j+1] = key 
            
    #     for el in lst:
    #         self.insert_at_end(el)
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

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")

llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

llist.reverse()   
print("\n Зв'язний список після реверсування ")
llist.print_list()

llist.insertion_sort()
print("\n Зв'язний список після sort ")
llist.print_list()


llist1 = LinkedList()

llist1.insert_at_beginning(1)
llist1.insert_at_beginning(23)
llist1.insert_at_beginning(17)
llist1.insert_at_beginning(33)
llist1.insert_at_beginning(3)

llist.concat(llist1)
print("\n Зв'язний список після concat ")
llist.print_list()

    
