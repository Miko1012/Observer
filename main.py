import pygame
import numpy as np


# rzutowanie perspektywiczne punktu we współrzędnych jednorodnych
def transform_to_viewport(point, d):
    mat = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1 / d, 1]])
    # print(str(mat))
    # print(point.dot(mat))
    # print(int(point.dot(mat)[:, 0]), int(point.dot(mat)[:, 1]), int(point.dot(mat)[:, 2]))
    return int(point.dot(mat)[:, 0]), int(point.dot(mat)[:, 1]), int(point.dot(mat)[:, 2])


pygame.init()
pygame.display.set_caption('Observer')

size = width, height = 1920, 1080
black = 0, 0, 0
white = 255, 255, 255
center = 960, 540

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# if __name__ == '__main__':
done = False

camera_pos = 0, 0, 500
point = 0, 0, 0
# point_1 = np.array([-20, 20, 0, 1])
# point_2 = np.array([-20, -20, 0, 1])
# point_3 = np.array([20, 20, 0, 1])
# point_4 = np.array([20, 20, 0, 1])
point_1 = np.array([920, 500, 0, 1])
point_2 = np.array([920, 580, 0, 1])
point_3 = np.array([1000, 500, 0, 1])
point_4 = np.array([1000, 580, 0, 1])
point_5 = np.array([920, 500, 100, 1])
point_6 = np.array([920, 580, 100, 1])
point_7 = np.array([1000, 500, 100, 1])
point_8 = np.array([1000, 580, 100, 1])
points = [point_1, point_2, point_3, point_4, point_5, point_6, point_7, point_8]

screen_point = 960, 540
screen_point_1 = 920, 500
screen_point_2 = 920, 580
screen_point_3 = 1000, 580
screen_point_4 = 1000, 500

screen_points = [screen_point, screen_point_1, screen_point_2, screen_point_3, screen_point_4]

# print(transform_to_viewport(point_1, d=50))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)

    for point in points:
        view = transform_to_viewport(point, d=50)
        # print(view[0])
        pygame.draw.circle(screen, white, [view[0], view[1]], 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
