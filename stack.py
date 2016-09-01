class Stack:

    def __init__(self, capacity=3):
        self.stack = []
        self.capacity = capacity
        if capacity < 0:
            raise InvalidCapacity

    def peek(self):
        if self.stack:
            return self.stack
        else:
            return None

    def push(self, *values):
        if len(values) + self.len() > self.capacity:
            raise StackOverflow
        for value in values:
            self.stack.append(value)

    def len(self):
        return len(self.stack)

    def is_empty(self):
        if self.len() == 0:
            return True
        else:
            return False

    def pop(self):
        if self.len() > 0:
            return self.stack.pop()
        else:
            raise StackUnderflow

    def find(self, value):
        for index, item in enumerate(self.stack):
            if item == value:
                return index
            else:
                return None

    def find_value(self, value):
        for item in self.stack:
            if item == value:
                return item
            else:
                return None


class InvalidCapacity(Exception):
    pass


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass
