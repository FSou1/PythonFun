from random import random
from time import sleep
import os

DEAD = 0
ALIVE = 1


def dead_state(width, height):
    return [[DEAD for x in range(width)] for y in range(height)]


def random_state(width, height):
    return [[random_cell() for x in range(width)] for y in range(height)]


def random_cell():
    return DEAD if random() < 0.5 else ALIVE


def render(state):
    display_as = {
        DEAD: ' ',
        ALIVE: u"\u2588"
    }
    lines = []
    for y in range(0, get_height(state)):
        line = ''
        for x in range(0, get_width(state)):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))


def get_width(state):
    return len(state[0])


def get_height(state):
    return len(state)


def get_cell(state, i, j):
    if i < 0 or j < 0:
        return DEAD
    try:
        return state[i][j]
    except IndexError:
        return DEAD


def next_alive_cell_state(alive_neighbors):
    if alive_neighbors < 2:
        return DEAD
    if 2 <= alive_neighbors <= 3:
        return ALIVE
    else:
        return DEAD


def next_dead_cell_state(alive_neighbors):
    if alive_neighbors == 3:
        return ALIVE
    else:
        return DEAD


def next_cell_state(cell, alive_neighbors):
    if cell == ALIVE:
        return next_alive_cell_state(alive_neighbors)
    else:
        return next_dead_cell_state(alive_neighbors)


def next_board_state(state):
    width = get_width(state)
    height = get_height(state)
    next_state = dead_state(width, height)
    for i in range(width):
        for j in range(height):
            current_cell = get_cell(state, i, j)
            alive_neighbors = get_cell(state, i-1, j-1) + get_cell(state, i, j-1) + get_cell(state, i+1, j-1) \
                              + get_cell(state, i-1, j) + get_cell(state, i+1, j) \
                              + get_cell(state, i-1, j+1) + get_cell(state, i, j+1) + get_cell(state, i+1, j+1)
            next_state[i][j] = next_cell_state(current_cell, alive_neighbors)
    return next_state


def cls():
    print ('\n' * 25)


clear = lambda: os.system('cls')


def start():
    state = random_state(50, 50)
    render(state)
    k = 0
    while True:
        sleep(0.1)
        clear()
        next_state = next_board_state(state)
        render(next_state)
        state = next_state
        k += 1


start()