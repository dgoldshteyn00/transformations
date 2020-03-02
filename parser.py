from display import *
from matrix import *
from draw import *

import math

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""


def parse_file(fname, points, transform, screen, color):
    file = open(fname, 'r')
    commands = []
    for line in file:
        commands.append(line[:-1])
    # print(commands)
    i = 0
    while i < len(commands):
        if commands[i] == "line":
            alist = commands[i + 1].split()
            a = [int(num) for num in alist]
            add_edge(points, a[0], a[1], a[2], a[3], a[4], a[5])
            i += 2
        elif commands[i] == "display":
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)
            i += 1
        elif commands[i] == "ident":
            ident(transform)
            i += 1
        elif commands[i] == "scale":
            alist = commands[i + 1].split()
            a = [int(num) for num in alist]
            newmat = make_scale(a[0], a[1], a[2])
            matrix_mult(newmat, transform)
            i += 2
        elif commands[i] == "move":
            alist = commands[i + 1].split()
            a = [int(num) for num in alist]
            newmat = make_translate(a[0], a[1], a[2])
            matrix_mult(newmat, transform)
            i += 2
        elif commands[i] == "rotate":
            alist = commands[i + 1].split()
            if alist[0] == "x":
                newmat = make_rotX(int(alist[1]) * math.pi / 180)
            elif alist[0] == "y":
                newmat = make_rotY(int(alist[1]) * math.pi / 180)
            else:
                newmat = make_rotZ(int(alist[1]) * math.pi / 180)
            matrix_mult(newmat, transform)
            i += 2
        elif commands[i] == "apply":
            matrix_mult(transform, points)
            i += 1
        else:
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)
            save_ppm_ascii(screen, 'pic.ppm')
            i += 2
