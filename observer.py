import pygame as pg
import numpy as np
from Space import Space, Cube, Wall
import math
from transformations import transform_into_view, screen_projection_matrix, multiply_vector_by_matrix


class Camera:
    def __init__(self):
        self.position = pg.Vector3(0, 0, -3)
        self.rotation = pg.Vector3(0, 0, 0)


print('siemka!')

# w1 = Wall(pg.Vector3(0, 0, 1), 2, 3, 4)
s = Space()
s.add_cube(1, 2, 3)

fNear = 0.1
fFar = 1000.0
fFov = 75.0
size = width, height = 1920, 1080

# transform_into_view(wall=s.walls[0], width=width, height=height)

s_p_m = screen_projection_matrix(fFov, fNear, fFar, width, height)
multiply_vector_by_matrix(vector=s.walls[1].vectors[1], matrix=s_p_m)



pg.init()
pg.display.set_caption('Observer')

black = 0, 0, 0
white = 255, 255, 255
center = 960, 540

screen = pg.display.set_mode(size)
clock = pg.time.Clock()
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(black)

    s_p_m = screen_projection_matrix(fFov, fNear, fFar, width, height)


    for wall in s.walls:
        transformed_wall = transform_into_view(wall=wall, width=width, height=height)

        v = transformed_wall.vectors


        pg.draw.line(screen, white, [transformed_wall.vectors[0].x, transformed_wall.vectors[0].y], [transformed_wall.vectors[1].x, transformed_wall.vectors[1].y], 2)
        pg.draw.line(screen, white, [transformed_wall.vectors[1].x, transformed_wall.vectors[1].y], [transformed_wall.vectors[2].x, transformed_wall.vectors[2].y], 2)
        pg.draw.line(screen, white, [transformed_wall.vectors[2].x, transformed_wall.vectors[2].y], [transformed_wall.vectors[3].x, transformed_wall.vectors[3].y], 2)
        pg.draw.line(screen, white, [transformed_wall.vectors[3].x, transformed_wall.vectors[3].y], [transformed_wall.vectors[0].x, transformed_wall.vectors[0].y], 2)

        # pg.draw.line(screen, white, transformed_wall[1], transformed_wall[2])
        # pg.draw.line(screen, white, transformed_wall[2], transformed_wall[3])
        # pg.draw.line(screen, white, transformed_wall[3], transformed_wall[0])
        # view = transform_to_viewport(point, d=50)
        # # print(view[0])
        # pygame.draw.circle(screen, white, [view[0], view[1]], 5)

    pg.display.flip()
    clock.tick(1)

pg.quit()
