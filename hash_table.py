

class Hash_Table:
    def __init__(self, max=100):
        self.max = max
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for k,v in self.arr[h]:
            if k == key:
                return v
        else:
            raise KeyError(f'Given key {key} is not present in the Hash Table')
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        element = self.arr[h]
        for idx,ele in enumerate(element):
            if ele[0] == key:
                element[idx] = (key, value)
                return element [idx]
        else:
            element.append((key,value))
            return element[-1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        element = self.arr[h]
        for idx,ele in enumerate(element):
            if ele[0] == key:
                element.pop(idx)
                break
        else:
            raise KeyError(f'Given key {key} is not present in the Hash Table')


hsh = Hash_Table(10)
hsh['March 10'] = 50
print(hsh['March 10'])
hsh['March 10'] = 100
hsh['March 6'] = 320
hsh['march 6'] = 167
hsh['March 17'] = 106
print(hsh['March 10'])
print(hsh['March 6'])
print(hsh['march 6'])
del hsh['March 17']
print(hsh.arr)