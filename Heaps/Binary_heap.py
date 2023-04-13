LIMIT = 100

class Binary_Heap:
    def __init__(self):
        self.heap_as_list = []
        self.current_parent_position = None

    def push(self, value):
        if not self.heap_as_list:
            self.heap_as_list.append(value)
            self.current_parent_position = 0
        elif value < self.heap_as_list[self.current_parent_position]:
            self.heap_as_list.append(value)
        else:
            pass

    def pop(self):
        pass

    def print_heap(self):
        pass


bh = Binary_Heap()
bh.push(8)
bh.push(7)
bh.push(6)
bh.push(6)
bh.push(4)
