

class BinarySearchTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_item(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.add_item(data)
            else:
                self.left = BinarySearchTree(data)
                return
        else:
            if self.right:
                return self.right.add_item(data)
            else:
                self.right = BinarySearchTree(data)
    
    def search(self, data):
        if data == self.data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
            elif data == self.data:
                return self
            else:
                return f'{data} not found in the Tree'
        else:
            if self.right:
                return self.right.search(data)
            elif data == self.right:
                return self
            else:
                return f'{data} not found in the Tree'
    
    def in_order_triversal(self):
        output = []
        if self.left:
            output += self.left.in_order_triversal()
        output.append(self.data)
        if self.right:
            output += self.right.in_order_triversal()
        return output
    
    def pre_order_triversal(self):
        output = [self.data]
        if self.left:
            output += self.left.pre_order_triversal()
        if self.right:
            output += self.right.pre_order_triversal()
        return output
    
    def post_order_triversal(self):
        output = []
        if self.left:
            output += self.left.post_order_triversal()
        if self.right:
            output += self.right.post_order_triversal()
        output.append(self.data)
        return output
    
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self
    
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self
    
    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min = self.right.min()
            self.data = min.data
            self.right = self.right.delete(min.data)
        return self


items = [37,16,59,14,2,5,8,9,14,37]
root = BinarySearchTree(37)
for i in items:
    root.add_item(i)

print(root.pre_order_triversal())
print(root.post_order_triversal())
print(root.min())
print(root.max())
print(root.sum())
print(root.search(59))
print(root.delete(59))
print(root.search(59))
print(root.in_order_triversal())