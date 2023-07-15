import pygame

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0

TEAL = (0, 128, 128)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# set up the player
player_color = TEAL
player_width = 100
player_height = 10
player_x = (width - player_width) // 2
player_y = screen.get_height() / 1.2
player_speed = 2

# set up bricks
brick_color = ORANGE
brick_width = 100
brick_height = 30
brick_rows = 5
brick_cols = width // (brick_width + 5)
padding = 5
bricks = []  # contains the undestroyed bricks

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + padding) + 10
        brick_y = row * (brick_height + padding) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# game loop
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    # draw player (paddle)
    pygame.draw.rect(screen, TEAL, (player_x, player_y,
                     player_width, player_height))

    # draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)
        pygame.draw.rect(screen, BLACK, brick, 1)  # brick outlines for padding

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 300 * dt * player_speed
    if keys[pygame.K_RIGHT]:
        player_x += 300 * dt * player_speed

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()