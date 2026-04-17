import pygame
import random
import time
from enum import Enum

tile = 20
plane = (40, 40)

pygame.init()
screen = pygame.display.set_mode((tile*plane[0], tile*plane[1]))

running = True

class Tile(Enum):
    WALL = 1
    FOOD = 2

world = []

snake = [(2,2), (2,3), (2,4)]
food = None

def build_world():
    for x in range(plane[0]):
        world.append([])

        for y in range(plane[1]):
            if x == 0 or x == plane[0] - 1:
                world[x].append(Tile.WALL)
                continue
            
            if y == 0 or y == plane[1] - 1:
                world[x].append(Tile.WALL)
                continue

            world[x].append(None)


def place_food():
    global world

    while True:
        x, y = random.randint(0, plane[0]-1), random.randint(0, plane[1]-1)

        if world[x][y] == Tile.WALL:
            continue

        if (x,y) in snake:
            continue

        world[x][y] = Tile.FOOD
        break

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

direction = Direction.DOWN

def update_snake():
    global snake
    global running

    head = snake[len(snake)-1]

    match direction:
        case Direction.UP:
            head = (head[0], head[1]-1)
        case Direction.DOWN:
            head = (head[0], head[1]+1)
        case Direction.LEFT:
            head = (head[0]-1, head[1])
        case Direction.RIGHT:
            head = (head[0]+1, head[1])

    if head in snake:
        running = False
        return
    
    if world[head[0]][head[1]] == Tile.WALL:
        running = False
        return
    
    if world[head[0]][head[1]] == Tile.FOOD:
        world[head[0]][head[1]] = None
        place_food()
    else:
        snake = snake[1:]

    snake.append(head)

def handle_inputs():
    global running
    global direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                continue
            
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    direction = Direction.UP

                case pygame.K_DOWN:
                    direction = Direction.DOWN

                case pygame.K_LEFT:
                    direction = Direction.LEFT

                case pygame.K_RIGHT:
                    direction = Direction.RIGHT

build_world()
place_food()

while running:
    screen.fill((0, 0, 0))

    handle_inputs()
    update_snake()

    for part in snake:
        x = tile * part[0]
        y = tile * part[1]

        pygame.draw.rect(
            screen,
            (0,255,0),
            (x, y, tile, tile),
        )
    
        for x in range(plane[0]):
            for y in range(plane[1]):
                if world[x][y] is None:
                    continue

                sx = tile * x
                sy = tile * y

                pygame.draw.rect(
                    screen,
                    (0,255,0),
                    (sx, sy, tile, tile),
                )

    pygame.display.update()
    time.sleep(0.05)

# TODO
#  - Generally improve code/refactor
#  - Remove time.sleep in favour of more responsive approach
#  - Add walls and/or teleporting
#  - Add scoring
#  - Do diff-based rendering (only render updated squares rather than all)