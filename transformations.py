import numpy as np
import math


def transform_into_view(wall, width, height):
    wall2 = wall
    for vector in wall2.vectors:
        print(vector)
        vector.x += 1
        vector.y += 1

        vector.x *= 0.5 * width
        vector.y *= 0.5 * height
    return wall2


def screen_projection_matrix(fov, near, far, w, h):
    ar = w / h
    f = math.tan(math.radians(fov) / 2)
    matrix = np.zeros([3, 3])
    matrix[0:0] = 1 / (ar * f)
    matrix[1:1] = 1 / f
    matrix[2:2] = (-near - far) / (near - far)
    matrix[2:3] = (2 * near * far) / (near - far)
    matrix[3:2] = 1
    return matrix


def multiply_vector_by_matrix(vector, matrix):
    return True
