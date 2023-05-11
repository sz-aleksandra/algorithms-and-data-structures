
class RollingHash:
    def __init__(self, text, size, prime=101, modulo=2**64):
        self.text = text
        self.size = size
        self.prime = prime
        self.modulo = modulo
        self.start = 0
        self.end = size
        self.hash = string_hash(self.text[:self.size], self.prime, self.modulo)

    def move_hash(self):
        if self.end <= len(self.text) - 1:
            self.hash = (self.hash - ord(self.text[self.start]) * pow(self.prime, self.size - 1, self.modulo)) % self.modulo
            self.hash = (self.hash * self.prime + ord(self.text[self.end])) % self.modulo
            self.start += 1
            self.end += 1

    def current_text(self):
        return self.text[self.start:self.end]


def string_hash(string, prime, modulo):
    hash_value = 0
    for character in string:
        hash_value = (hash_value * prime + ord(character)) % modulo
    return hash_value


def find_KR(string, text):
    position_list = []
    if not (string and text):
        return position_list
    if len(string) > len(text):
        return position_list
    if len(string) == len(text) and string != text:
        return position_list

    pattern_hash = string_hash(string, 101, 2**64)
    rolling_hash = RollingHash(text, len(string))

    for index in range(len(text) - len(string) + 1):
        if rolling_hash.hash == pattern_hash:
            if rolling_hash.current_text() == string:
                position_list.append(index)
        if index < len(text) - len(string):
            rolling_hash.move_hash()
    return position_list
