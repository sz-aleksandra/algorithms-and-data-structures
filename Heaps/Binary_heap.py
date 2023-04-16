class Binary_Heap:
    def __init__(self):
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
            while pos > 0 and self.heap_as_list[pos] > self.heap_as_list[int((pos - 1) / 2)]:
                self.change_elements(pos, int((pos - 1) / 2))
                pos = int((pos - 1) / 2)

    def change_elements(self, position_1, position_2):
        temp = self.heap_as_list[position_1]
        self.heap_as_list[position_1] = self.heap_as_list[position_2]
        self.heap_as_list[position_2] = temp

    def pop_root(self):
        pos = 0
        while pos < self.current_position / 2:
            if self.heap_as_list[2 * pos + 2] >= self.heap_as_list[2 * pos + 1]:
                self.heap_as_list[pos] = self.heap_as_list[2 * pos + 2]
                pos = 2 * pos + 2
            else:
                self.heap_as_list[pos] = self.heap_as_list[2 * pos + 1]
                pos = 2 * pos + 1
        while pos < self.current_position:
            self.heap_as_list[pos] = self.heap_as_list[pos + 1]
            pos += 1
        self.heap_as_list.pop()

    def print_heap(self):
        pass
