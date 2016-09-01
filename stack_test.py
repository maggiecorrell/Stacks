from stack import Stack, InvalidCapacity, StackOverflow, StackUnderflow
from nose.tools import *


def test_is_there_stack():
    stack = Stack()
    assert stack.peek() is None


def test_push():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == [5]


def test_push_multi():
    stack = Stack()
    stack.push(1, 2)
    assert stack.peek() == [1, 2]


def test_push_another_multi():
    stack = Stack()
    try:
        stack.push(1, 2, 3, 4)
    except:
        pass
    assert stack.len() <= stack.capacity


def test_push_yet_another_multi():
    stack = Stack()
    stack.push(1)
    try:
        stack.push(1, 2, 3)
    except:
        pass
    assert stack.len() <= stack.capacity


def test_capacity():
    stack = Stack()
    assert stack.capacity == 3


@raises(StackOverflow)
def test_past_capacity():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

@raises(InvalidCapacity)
def test_negative_capacity():
    stack = Stack(-2)


def test_len():
    stack = Stack()
    assert stack.len() == 0


def test_len_with_stuff():
    stack = Stack()
    stack.push(2)
    stack.push(3)
    assert stack.len() == 2


def test_empty():
    stack = Stack()
    assert stack.is_empty() is True


def test_not_empty():
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() is False


def test_pop():
    stack = Stack()
    stack.push(2)
    stack.push(6)
    assert stack.pop() == 6

@raises(StackUnderflow)
def test_pop_empty():
    stack = Stack()
    stack.pop()


def test_find():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    print(stack.find(5))
    assert stack.find(5) == 0


def test_find_returns_none():
    stack = Stack()
    stack.push(2)
    assert stack.find(5) is None


def test_find_value():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    assert stack.find_value(5) == 5
