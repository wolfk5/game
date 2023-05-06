import pygame 
import os
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)

FPS = 60
VEL = 5
bullet_vel =   7
max_bullets = 3
space_witdh, spaceship_height = 55, 40

yellow_hit = pygame.USEREVENT + 1 
red_hit = pygame.USEREVENT + 2

yellow_spaceship_image = pygame.image.load(os.path.join('Pygame', 'Assets', 'trandan.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (space_witdh, spaceship_height)),  90)
red_spaceship_image = pygame.image.load(os.path.join('Pygame', 'Assets', 'dan2.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (space_witdh, spaceship_height)),  270)
space = pygame.transform.scale(pygame.image.load(os.path.join('Pygame', 'Assets', 'rice-field-1.png')), (WIDTH, HEIGHT))

            

def main():
    red = pygame.Rect(700, 300, space_witdh, spaceship_height)
    yellow = pygame.Rect(100, 300, space_witdh, spaceship_height)
    
    red_bullets = []
    yellow_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
            
        draw_window(red, yellow, red_bullets, yellow_bullets)
            
    pygame.quit()
        
def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.blit(space, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER )
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet )
        
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet )
        
        
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
        yellow.x  -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
        yellow.x  += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y  -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y  += VEL       
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT
        red.x  -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x  += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y  -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y  += VEL
        
        
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        
if __name__  == "__main__":
    main()
