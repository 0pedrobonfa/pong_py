# Example file showing a basic pygame "game loop"
import pygame

# CONSTANTS
WINDOW_width = 1280
WINDOW_height = 720


# pygame setup
pygame.init()

# Inicializa variaveis do game
screen = pygame.display.set_mode((WINDOW_width, WINDOW_height))
clock = pygame.time.Clock()
running_game = True

# Inicializa 'entidades'
field_limit = pygame.Rect(0,0,WINDOW_width,WINDOW_height)

ball = pygame.Rect(WINDOW_width/2,WINDOW_height/2,25,25)

p1 = pygame.Rect(1110,260,25,100)

p2 = pygame.Rect(110,260,25,100)

mid_line = pygame.Rect(WINDOW_width/2,0,1,720)




# PYSHICS
SPEED = 20
SPEED_y = 1

BALL_MOVE_X = SPEED
BALL_MOVE_Y = SPEED_y

PLAYER_X_SPEED = SPEED
PLAYER_Y_SPEED = SPEED_y

# PLAYER1 MOVEMENT
p1_moving_up = False
p1_moving_down = False

p2_moving_up = False
p2_moving_down = False

while running_game:

    delta = clock.tick(60) /1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

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

    if p1.top <= 5:
        p1.top = 5
    if p1.bottom >= WINDOW_height-5:
        p1.bottom = WINDOW_height-5

    if p2.top <= 0:
        p2.top = 0
    if p2.bottom >= WINDOW_height-5:
        p2.bottom = WINDOW_height-5

    if p1_moving_up:
        p1.move_ip(0, -PLAYER_X_SPEED)
    elif p1_moving_down:
        p1.move_ip(0, PLAYER_X_SPEED)

    if p2_moving_up:
        p2.move_ip(0, -PLAYER_X_SPEED)
    elif p2_moving_down:
        p2.move_ip(0, PLAYER_X_SPEED)


    # BALL PHYSICS
    ball.move_ip(BALL_MOVE_X, BALL_MOVE_Y)

    if ball.top < 0 or ball.bottom >= WINDOW_height:
        BALL_MOVE_Y = BALL_MOVE_Y * -1

    elif ball.left < 0 or ball.right>WINDOW_width:
        BALL_MOVE_X = BALL_MOVE_X * -1

    if p1.colliderect(ball):
        BALL_MOVE_X *= -1

    if p2.colliderect(ball):
        BALL_MOVE_X *= -1


    screen.fill("black")

    pygame.draw.rect(screen, "white", field_limit,3)

    pygame.draw.rect(screen, "white", mid_line)

    pygame.draw.rect(screen, "white", ball,0,50)
    pygame.draw.rect(screen, "green",p1)
    pygame.draw.rect(screen, "yellow",p2)

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()