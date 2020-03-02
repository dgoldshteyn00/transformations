from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [0, 0, 0]
edges = new_matrix(0, 0)
transform = new_matrix()
ident(transform)

# import math

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


"""def parse_file(fname, points, transform, screen, color):
    clear_screen(screen)
    file = open(fname, 'r')
    lines = []
    for line in file:
        lines.append(line[:-1])
    counter = 0
    while counter < len(lines):
        if lines[counter] == "line":
            temp = lines[counter + 1].split()
            w = [int(num) for num in temp]
            add_edge(points, w[0], w[1], w[2], w[3], w[4], w[5])
            counter += 2
        elif lines[counter] == "display":
            draw_lines(points, screen, color)
            # display(screen)
            counter += 1
        elif lines[counter] == "ident":
            ident(transform)
            counter += 1
        elif lines[counter] == "scale":
            temp = lines[counter + 1].split()
            w = [int(num) for num in temp]
            transform_matrix = make_scale(w[0], w[1], w[2])
            matrix_mult(transform_matrix, transform)
            counter += 2
        elif lines[counter] == "move":
            temp = lines[counter + 1].split()
            w = [int(num) for num in temp]
            transform_matrix = make_translate(w[0], w[1], w[2])
            matrix_mult(transform_matrix, transform)
            counter += 2
        elif lines[counter] == "rotate":
            temp = lines[counter + 1].split()
            if temp[0] == "x":
                transform_matrix = make_rotX(int(temp[1]) * math.pi / 180)
            elif temp[0] == "y":
                transform_matrix = make_rotY(int(temp[1]) * math.pi / 180)
            else:
                transform_matrix = make_rotZ(int(temp[1]) * math.pi / 180)
            matrix_mult(transform_matrix, transform)
            counter += 2
        elif lines[counter] == "apply":
            matrix_mult(transform, points)
            counter += 1
        else:
            draw_lines(points, screen, color)
            # display(screen)
            save_ppm_ascii(screen, 'pic.ppm')
            counter += 2"""


f = open("script", "a")
f.write("\n")

"""for i in range(180):
    f.write("ident\n")
    f.write("rotate\n")
    f.write("z " + str(2) + "\n")
    f.write("rotate\n")
    f.write("x " + str(2) + "\n")
    f.write("rotate\n")
    f.write("y " + str(2) + "\n")
    f.write("apply\n")
    f.write("ident\n")
    f.write("apply\n")
    f.write("display\n")"""

f.write("save\n")

parse_file('script', edges, transform, screen, color)

"""f.close()

f = open("script", "w")
f.write("line\n")
f.write("0 0 25 100 0 25\n")
f.write("line\n")
f.write("100 0 25 100 100 75\n")
f.write("line\n")
f.write("100 100 75 0 100 75\n")
f.write("line\n")
f.write("0 100 75 0 0 25\n")
f.write("line\n")
f.write("0 0 125 100 0 125\n")
f.write("line\n")
f.write("100 0 125 100 100 175\n")
f.write("line\n")
f.write("100 100 175 0 100 175\n")
f.write("line\n")
f.write("0 100 175 0 0 125\n")
f.write("line\n")
f.write("0 0 25 0 0 125\n")
f.write("line\n")
f.write("0 100 75 0 100 175\n")
f.write("line\n")
f.write("100 100 75 100 100 175\n")
f.write("line\n")
f.write("100 0 25 100 0 125\n")
f.write("ident\n")
f.write("scale\n")
f.write("2 2 2\n")
f.write("apply\n")
f.write("ident\n")
f.write("move\n")
f.write("50 25 25\n")
f.write("apply")

f.close()"""
