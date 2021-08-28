from ast import Index


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head:
            current = self.head
            li_list = f'Start--{str(self.head.data)}-->>--'
            while current.next:
                current = current.next
                li_list += f'{str(current.data)}-->>--'
            return print(li_list)
        else:
            return print('Linked List is Empty!!')

    def append(self, data):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)

    def push(self, data):
        if self.head:
            head = Node(data, self.head)
            self.head = head
        else:
            self.head = Node(data)
    
    def insert(self, data, index):
        '''
        Inserts Data at given Index
        adds data to the end if index out of range
        '''
        if index == 0:
            self.push(data)
        else:
            count = 1
            current = self.head
            while current.next:
                current = current.next
                count += 1
                if count == index:
                    break
            next = current.next
            current.next = Node(data, next)
    
    def delete(self,index):
        if index == 0:
            current = self.head
            self.head = current.next
        else:
            count = 1
            current = self.head
            while current.next:
                current = current.next
                count += 1
                if count == index:
                    break
            next = current.next
            try:
                current.next = next.next
            except:
                raise IndexError('Index out of range')
    
    def index(self, data):
        if self.head:
            current = self.head
            if current.data == data:
                return 0
            index = 1
            while current.next:
                current = current.next
                if current.data == data:
                    return index
                else:
                    index += 1
            else:
                return f'{data} is not in the Linked List'
        else:
            return 'Linked list is Empty!!'


lil = LinkedList()
lil.head = Node('Item-1')
lil.head.next = Node('Item-2')
lil.append('Item-3')
lil.push('Item-0')
lil.insert('Insert-0', 10)
lil.delete(2)
lil.print()
print(lil.index('Item-5'))

