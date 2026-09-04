# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

# Inicializa variaveis do game
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Inicializa 'entidades'
#field_limit = pygame.Rect(0,720,5,0)

ball = pygame.Rect(1280/2,720/2,16,16)

p1 = pygame.Rect(1110,260,25,100)

p2 = pygame.Rect(110,260,25,100)

mid_line = pygame.Rect(1280/2,0,1,720)




# PYSHICS
SPEED = 5
SPEED_y = 0

# PLAYER MOVEMENT
p1_moving_up = False
p1_moving_down = False

p2_moving_up = False
p2_moving_down = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # p1 MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1_moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1_moving_up = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p1_moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p1_moving_down = False

        # p2 MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p2_moving_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p2_moving_up = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                p2_moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                p2_moving_down = False

    # PLAYER MOVEMENT CHECK
    if p1_moving_up:
        p1.move_ip(0, -SPEED)
        print("UP")
    elif p1_moving_down:
        p1.move_ip(0, SPEED)
        print("DOWN")

    if p2_moving_up:
        p2.move_ip(0, -SPEED)
        print("UP")
    elif p2_moving_down:
        p2.move_ip(0, SPEED)
        print("DOWN")



    # BALL PHYSICS

    ball.move_ip(SPEED,SPEED_y)

    if ball.x == p1.x or ball.x == p2.x:
        SPEED = SPEED*-1
        SPEED_y = SPEED_y * -1
        if SPEED_y > 0:
            SPEED_y += 1
        else:
            SPEED_y -= 1


    screen.fill("black")

    #pygame.draw.rect(screen, "white", field_limit)

    pygame.draw.rect(screen, "white", mid_line)

    pygame.draw.rect(screen, "white", ball)
    pygame.draw.rect(screen, "green",p1)
    pygame.draw.rect(screen, "yellow",p2)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()