from display import *
from matrix import *


def draw_lines(matrix, screen, color):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line(matrix[point][0],
                  matrix[point][1],
                  matrix[point + 1][0],
                  matrix[point + 1][1],
                  screen, color)
        point += 2


def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)


def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])


def draw_line(x0, y0, x1, y1, screen, color):  # this version uses error calculations
    dx = abs(x1 - x0)
    mx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    my = 1 if y0 < y1 else -1
    error = dx + dy
    while 1 == 1:  # for i in range(1000): <test code>
        plot(screen, color, x0, y0)
        if x0 == x1 and y0 == y1:
            break
        error_2 = 2 * error
        if error_2 >= dy:
            error += dy
            x0 += mx
        if error_2 <= dx:
            error += dx
            y0 += my
