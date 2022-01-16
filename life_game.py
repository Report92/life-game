import pygame
import classes


width, height = 960, 900
size = (width, height)

pygame.init()
pygame.display.set_caption("Alex's game")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 100

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = classes.Grid(width, height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.Conway(off_color=white, on_color=blue, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)


    pygame.display.update()

pygame.quit()
