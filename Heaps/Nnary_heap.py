class Nnary_Heap:
    def __init__(self, n):
        self.arity = n
        self.heap_as_list = []
        self.current_position = None

    def push(self, value):
        if not self.heap_as_list:
            self.heap_as_list.append(value)
            self.current_position = 0
        else:
            self.heap_as_list.append(value)
            self.current_position += 1
            pos = self.current_position
            while pos > 0 and self.heap_as_list[pos] > self.heap_as_list[int((pos - 1) / self.arity)]:
                self.change_elements(pos, int((pos - 1) / self.arity))
                pos = int((pos - 1) / self.arity)

    def change_elements(self, position_1, position_2):
        temp = self.heap_as_list[position_1]
        self.heap_as_list[position_1] = self.heap_as_list[position_2]
        self.heap_as_list[position_2] = temp

    def pop_root(self):
        if self.heap_as_list:
            self.heap_as_list[0] = self.heap_as_list[self.current_position]
            self.heap_as_list.pop(self.current_position)
            if self.current_position != 0:
                self.current_position -= 1
                pos = 0
                i = self.find_max_child(pos)
                while i:
                    self.change_elements(pos, self.arity * pos + i)
                    pos = self.arity * pos + i
                    i = self.find_max_child(pos)
            else:
                self.current_position = None

    def find_max_child(self, pos):
        current_max = self.heap_as_list[pos]
        current_max_index = None
        for i in range(1, self.arity + 1):
            if self.arity * pos + i <= self.current_position:
                if self.heap_as_list[self.arity * pos + i] > current_max:
                    current_max = self.heap_as_list[self.arity * pos + i]
                    current_max_index = i
        return current_max_index

    def print_uni(self, position=0, level=0):
# prints root at the top and its children below (top is the most left one)
# same intendation equals same depth
        if self.heap_as_list:
            if position <= self.current_position:
                print('   ' * level, self.heap_as_list[position])
                for i in range(1, self.arity + 1):
                    self.print_uni(self.arity * position + i, level + 1)
