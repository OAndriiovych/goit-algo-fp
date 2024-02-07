class MyNode:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous

    def __str__(self) -> str:
        return self.value


class MyList:
    def __init__(self):
        self.last = None
        self.size = 0

    def add(self, value):
        self.last = MyNode(value, self.last)
        self.size += 1

    def __str__(self) -> str:
        current = self.last
        to_str = " "
        for i in range(self.size):
            to_str = to_str + str(current.value) + " "
            current = current.previous
        return "[" + to_str + "]"

    def sort(self):
        for i in range(self.size):
            current = self.last
            for j in range(self.size - 1):
                previous = current.previous
                if (current.value > previous.value):
                    previous_value = previous.value
                    previous.value = current.value
                    current.value = previous_value
                current = current.previous

    def revers(self):
        current = self.last
        new_last = None
        for i in range(self.size):
            new_last = MyNode(current.value, new_last)
            current = current.previous
        self.last = new_last

    def merge(self, new_list: 'MyList'):
        new_list.sort()
        self.sort()
        new_last = None
        self_last = self.last
        new_list_last = new_list.last
        for i in range(self.size + new_list.size):
            if self_last and new_list_last:
                if self_last.value < new_list_last.value:
                    new_last = MyNode(self_last.value, new_last)
                    self_last = self_last.previous
                else:
                    new_last = MyNode(new_list_last.value, new_last)
                    new_list_last = new_list_last.previous
            elif self_last:
                new_last = MyNode(self_last.value, new_last)
                self_last = self_last.previous
            elif new_list_last:
                new_last = MyNode(new_list_last.value, new_last)
                new_list_last = new_list_last.previous
        self.last = new_last
        self.size += new_list.size


if __name__ == '__main__':
    list = MyList()
    list.add(10)
    list.add(1)
    list.add(5)
    list.add(3)
    list.add(4)
    list.add(-1)
    print(list)

    # 1
    list.sort()
    print(list)

    # 2
    list.revers()
    print(list)

    # 3
    list2 = MyList()
    list2.add(111)
    list2.add(110)
    list2.add(7)
    list2.add(-11)
    list.merge(list2)
    print(list)
