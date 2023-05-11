
class RollingHash:
    def __init__(self, text, size, prime=101, modulo=2**64):
        self.text = text
        self.hash = 0
        self.size = size
        self.prime = prime
        self.modulo = modulo


        self.start = 0
        self.end = size

    def move_hash(self):
        if self.end <= len(self.text) - 1:
            self.hash = (self.hash - ord(self.text(self.start)) * (self.prime ** (self.size - 1)) % self.modulo)
            self.hash =

def hash(string, prime, modulo):
    hash_value = 0
    for character in string:
        hash_value = (hash_value * prime + ord(character)) % modulo
    return hash_value


def find_KR(string, text):
    pattern_hash = hash(string)
    position_list = []
    for index in range(len(text) - len(string) + 1):
        substring = text[(index):(index + len(string) - 1)]
        substring_hash = hash(substring)
        if substring_hash == pattern_hash:
            if substring == string:
                position_list.append(index)
    return position_list
