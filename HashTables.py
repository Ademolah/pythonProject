
class HashTables:       #these are the implementations of dictionaries by assigning a value to a key

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size    #index all through the bucket
        self.values =[None] * self.size  #values all through the bucket



    def insert(self, key, data):

        index = self.hashFunction(key)

        #handling possible collisions, is not None means if there is already an index in that position
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data

                return

            #rehash by linear probing by checking for other index position
            index = (index +1 ) % self.size

        #insert these new data
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):

        index = self.hashFunction(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.size


        return None #this is incase the key is not found



    def hashFunction(self, key):
        sum = 0
        for x in range(len(key)):
            sum = sum + ord(key[x])

        return sum % self.size


h = HashTables()

h.insert('Demola','Software engineer')
h.insert('Country', 'Nigeria')
h.insert('age',22)
h.insert('religion','christianity')

print(h.get('Demola'))