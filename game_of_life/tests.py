from state import dead_state
from state import next_board_state


def test1():
    actual = dead_state(2, 2)
    expected = [[0, 0], [0, 0]]
    if actual == expected:
        print('test1: Passed')
    else:
        print('test1: Failed')


def test2():
    initial = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    actual = next_board_state(initial)
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if actual == expected:
        print('test2: Passed')
    else:
        print('test2: Failed')


def test3():
    initial = [
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
    ]
    actual = next_board_state(initial)
    expected = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
    ]
    if actual == expected:
        print('test3: Passed')
    else:
        print('test3: Failed')
        print('expected:')
        print_state(expected)
        print('initial:')
        print_state(initial)
        print('actual:')
        print_state(actual)


def test4():
    initial = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    actual = next_board_state(initial)
    expected = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    if actual == expected:
        print('test4: Passed')
    else:
        print('test4: Failed')
        print('expected:')
        print_state(expected)
        print('initial:')
        print_state(initial)
        print('actual:')
        print_state(actual)


def print_state(state):
    for row in state:
        print(row)


test1()
test2()
test3()
test4()