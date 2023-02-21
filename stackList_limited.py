class Stacks:
    def __init__(self, Maxsize):
        self.maxsize = Maxsize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "the stack is full."
        else:
            self.list.append(value)
            return " the max size is created."

    def pop(self):
        if self.isEmpty():
            return "no list in here"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return " no stack list in here."
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


custom = Stacks(5)
print(custom.isFull())
print(custom.isEmpty())
custom.push(2)
custom.push(3)
custom.push(4)
custom.push(5)
print(custom)
