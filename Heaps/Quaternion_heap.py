class Quaternion_Heap:
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
            while pos > 0 and self.heap_as_list[pos] > self.heap_as_list[int((pos - 1) / 4)]:
                self.change_elements(pos, int((pos - 1) / 4))
                pos = int((pos - 1) / 4)

    def change_elements(self, position_1, position_2):
        temp = self.heap_as_list[position_1]
        self.heap_as_list[position_1] = self.heap_as_list[position_2]
        self.heap_as_list[position_2] = temp

    def pop_root(self):
        pos = 0
        while pos < (self.current_position - 3) / 4:
            if self.heap_as_list[4 * pos + 2] >= self.heap_as_list[4 * pos + 1] and self.heap_as_list[4 * pos + 2] >= self.heap_as_list[4 * pos + 3] and self.heap_as_list[4 * pos + 2] >= self.heap_as_list[4 * pos + 4]:
                self.heap_as_list[pos] = self.heap_as_list[4 * pos + 2]
                pos = 4 * pos + 2
            elif self.heap_as_list[4 * pos + 1] >= self.heap_as_list[4 * pos + 2] and self.heap_as_list[4 * pos + 1] >= self.heap_as_list[4 * pos + 3] and self.heap_as_list[4 * pos + 1] >= self.heap_as_list[4 * pos + 4]:
                self.heap_as_list[pos] = self.heap_as_list[4 * pos + 1]
                pos = 4 * pos + 1
            elif self.heap_as_list[4 * pos + 3] >= self.heap_as_list[4 * pos + 2] and self.heap_as_list[4 * pos + 3] >= self.heap_as_list[4 * pos + 1] and self.heap_as_list[4 * pos + 3] >= self.heap_as_list[4 * pos + 4]:
                self.heap_as_list[pos] = self.heap_as_list[4 * pos + 3]
                pos = 4 * pos + 3
            else:
                self.heap_as_list[pos] = self.heap_as_list[4 * pos + 4]
                pos = 4 * pos + 4
        while pos < self.current_position:
            self.heap_as_list[pos] = self.heap_as_list[pos + 1]
            pos += 1
        self.heap_as_list.pop()

    def print_heap(self):
        pass


bh = Quaternion_Heap()
bh.push(11)
bh.push(7)
bh.push(6)
bh.push(10)
bh.push(4)
bh.push(6)
bh.push(5)
bh.push(2)
bh.push(9)
bh.push(4)
bh.push(3)
bh.push(6)
bh.push(2)
bh.push(9)
bh.pop_root()