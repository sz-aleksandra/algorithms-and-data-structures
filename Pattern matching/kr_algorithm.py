class RollingHash:
    def __init__(self, text, size):
        self.text = text
        self.size = size
        self.start = 0
        self.end = size
        self.hash = string_hash(self.text[:self.size])

    def move_hash(self):
        if self.end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.start]) - ord('a') + 1) * (26 ** (self.size - 1))
            self.hash *= 26
            self.hash += (ord(self.text[self.end]) - ord('a') + 1)
            self.start += 1
            self.end += 1

    def current_text(self):
        return self.text[self.start:self.end]


def string_hash(string):
    hash_value = 0
    for index in range(0, len(string)):
        hash_value += (ord(string[index]) - ord('a') + 1) * (26 ** (len(string) - index - 1))
    return hash_value


def find_KR(string, text):
    position_list = []
    if not (string and text):
        return position_list
    if len(string) > len(text):
        return position_list
    if len(string) == len(text) and string != text:
        return position_list

    pattern_hash = string_hash(string)
    rolling_hash = RollingHash(text, len(string))

    for index in range(len(text) - len(string) + 1):
        if rolling_hash.hash == pattern_hash:
            if rolling_hash.current_text() == string:
                position_list.append(index)
        if index < len(text) - len(string):
            rolling_hash.move_hash()
    return position_list
