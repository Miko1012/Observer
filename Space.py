import pygame.math as pgm


class Wall:

    def __init__(self, v1, v2, v3, v4):
        self.vectors = [v1, v2, v3, v4]
        print('nowa ściana składa się z wektorów:')
        for v in self.vectors:
            print(v)


class Cube:
    def __init__(self, w, h, d):
        print(f'Tworzę kostkę o szerokości {w}, wysokości {h} i głębokości {d}')
        self.walls = []
        self.create_starting_cube()

    def create_starting_cube(self):
        w1 = Wall(pgm.Vector3(0, 0, 0), pgm.Vector3(1, 0, 0), pgm.Vector3(1, 0, 1), pgm.Vector3(0, 0, 1))
        w2 = Wall(pgm.Vector3(0, 1, 0), pgm.Vector3(1, 1, 0), pgm.Vector3(1, 1, 1), pgm.Vector3(0, 1, 1))
        w3 = Wall(pgm.Vector3(0, 0, 0), pgm.Vector3(0, 1, 0), pgm.Vector3(0, 1, 1), pgm.Vector3(0, 0, 1))
        w4 = Wall(pgm.Vector3(1, 0, 0), pgm.Vector3(1, 1, 0), pgm.Vector3(1, 1, 1), pgm.Vector3(1, 0, 1))
        w5 = Wall(pgm.Vector3(0, 1, 1), pgm.Vector3(1, 1, 1), pgm.Vector3(1, 0, 1), pgm.Vector3(0, 0, 1))
        w6 = Wall(pgm.Vector3(0, 1, 0), pgm.Vector3(1, 1, 0), pgm.Vector3(1, 0, 0), pgm.Vector3(0, 0, 0))
        self.walls = [w1, w2, w3, w4, w5, w6]
        print('Moje ściany:')
        for wall in self.walls:
            print(wall)

    def get_walls(self):
        return self.walls


class Space:
    def __init__(self):
        self.cubes = []
        self.walls = []

    def add_cube(self, w, h, d):
        cube = Cube(w, h, d)
        cube_walls = cube.get_walls()
        self.cubes.append(cube)
        for wall in cube_walls:
            self.walls.append(wall)
        print(cube_walls)


