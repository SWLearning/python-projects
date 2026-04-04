import pygame
import random
import time
from enum import Enum

tile = 20
plane = (40, 40)

pygame.init()
screen = pygame.display.set_mode((tile*plane[0], tile*plane[1]))

running = True

walls = []
snake = [(2,2), (2,3), (2,4)]
food = None

def build_walls():
    global walls

    for x in range(plane[0]):
        for y in range(plane[1]):
            if x == 0 or x == plane[0] - 1:
                walls.append((x,y))
                continue
            
            if y == 0 or y == plane[1] - 1:
                walls.append((x,y))
                continue



def place_food():
    global food

    while True:
        food = (random.randint(0, plane[0]-1), random.randint(0, plane[1]-1))

        if food in snake:
            continue

        if food in walls:
            continue

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
    
    if head in walls:
        running = False
        return

    if food == head:
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

build_walls()
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
    
        for part in walls:
            x = tile * part[0]
            y = tile * part[1]

            pygame.draw.rect(
                screen,
                (0,255,0),
                (x, y, tile, tile),
            )

    
    pygame.draw.rect(
        screen,
        (0,255,0),
        (food[0]*tile, food[1]*tile, tile, tile),
    )

    pygame.display.update()
    time.sleep(0.05)

# TODO
#  - Remove time.sleep in favour of more responsive approach
#  - Generally improve code/refactor
#  - Add walls and/or teleporting
#  - Add scoring