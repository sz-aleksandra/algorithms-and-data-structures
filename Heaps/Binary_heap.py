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

    def pop(self):
        pass

    def print_heap(self):
        pass


bh = Binary_Heap()
bh.push(8)
bh.push(7)
bh.push(6)
bh.push(9)
bh.push(4)
