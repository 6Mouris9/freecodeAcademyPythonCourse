# A funcao hashing somara valores unicode de cada caractere na chave
# O valor hash sera usado para a chave real para armazenar o valor associado

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str):
        list_values = []
        for char in key:
            list_values.append(ord(char))
        return sum(list_values)

    def add(self, key, value):
        if not key or not value:
            raise ValueError("Must be not empty, key and value")
        if not isinstance(key, str):
            raise TypeError("Key argument must be an str type")

        dict_key = self.hash(key)

        if dict_key not in self.collection:
            self.collection[dict_key] = {}
        self.collection[dict_key][key] = value
        return dict_key

    def remove(self, key):
        if not key:
            raise ValueError("The Key must be not empty")
        if not isinstance(key, str):
            raise TypeError("Key argument must be an str type")
        
        index = self.hash(key)
        
        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

            if not self.collection[index]:
                del self.collection[index]
            return True
        return None

    def lookup(self, key):
        if not key:
            raise ValueError("The Key must be not empty")
        if not isinstance(key, str):
            raise TypeError("Key argument must be an str type")
            
        hash_value = self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        
        return None