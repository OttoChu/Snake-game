import pygame
from random import choice

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 200, 255)
GREEN1 = (0, 225, 0)
GREEN2 = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 215, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)

pygame.init()
screen = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Snakes")
clock = pygame.time.Clock()
    
def draw_board():
    pygame.draw.rect(screen, BLACK, (49, 49, 451, 451), 2)
    flag = True
    for y in range(15):
        for x in range(15):
            if flag:
                colour = GREEN1
                flag = not(flag)
            else:
                colour = GREEN2
                flag = not(flag)
            pygame.draw.rect(screen, colour, (x * 30 + 50, y * 30 + 50, 30, 30))

def draw_score(length):
    font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 50)
    text_surf = font.render(f'Your score: {str(length - 1)}', True, RED)
    text_rect = text_surf.get_rect(topleft = (10, 10))
    screen.blit(text_surf, text_rect)

def draw_snake(snake_pos):
    for i, each_coor in enumerate(snake_pos):
        if i == len(snake_pos) - 1:
            pygame.draw.rect(screen, PINK, (each_coor[1] * 30 + 50, each_coor[0] * 30 + 50, 30, 30))
        else:
            pygame.draw.rect(screen, YELLOW, (each_coor[1] * 30 + 50, each_coor[0] * 30 + 50, 30, 30))

def draw_apple(apple_coor):
    pygame.draw.rect(screen, RED, (apple_coor[1] * 30 + 60, apple_coor[0] * 30 + 60, 10, 10))

def add_apple():
    empty = []
    for y in range(15):
        for x in range(15):
            empty.append([y,x])
    for each in snake_pos:
        empty.remove(each)
    if not(empty):
        return True
    new_apple_coor = choice(empty) 
    return new_apple_coor

def move_snake(key, old_key):
# Stoping the snake from doing ilgeal moves
    if key == 'W' and old_key == 'S':
         key = 'S'
    elif key == 'S' and old_key == 'W':
        key = 'W'
    elif key == 'A' and old_key == 'D':
        key = 'D'
    elif key == 'D' and old_key == 'A':
        key = 'A'
# Adding a new block
    if key == 'W':
        new_pos = [snake_pos[-1][0] - 1, snake_pos[-1][1]]
    elif key == 'A':
        new_pos = [snake_pos[-1][0], snake_pos[-1][1] - 1]
    elif key == 'S':
        new_pos = [snake_pos[-1][0] + 1, snake_pos[-1][1]]
    elif key == 'D':
        new_pos = [snake_pos[-1][0], snake_pos[-1][1] + 1]
    if key != None:
# End the game if the snake collides with itself
        for each_coor in snake_pos:
            if new_pos == each_coor:
                return key, True, False
# End the game if the snake is out of the box
        if new_pos[0] < 0 or new_pos[0] > 14 or new_pos[1] < 0 or new_pos[1] > 14:
            return key, True, False
        snake_pos.append(new_pos)
# Add a new block if the snake ate an apple
        if new_pos != apple_coor:
            snake_pos.pop(0)
            return key, False, False
        return key, False, True
    return key, False, False

snake_pos = [[7, 7]]
key = None
old_key = None
new_apple = True
lost = False
win = False
update_counter = 0
speed = 8

while True:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode.upper() == 'W' or event.unicode.upper() == 'A' or event.unicode.upper() == 'S' or event.unicode.upper() == 'D':
                key = event.unicode.upper()
            if event.key == pygame.K_UP:
                key = 'W'
            if event.key == pygame.K_LEFT:
                key = 'A'
            if event.key == pygame.K_DOWN:
                key = 'S'
            if event.key == pygame.K_RIGHT:
                key = 'D'
        try:
            if new_game_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                snake_pos = [[7, 7]]
                key = None
                old_key = None
                new_apple = True
                lost = False
                win = False
        except:
            pass
    if lost:
        font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 100)
        text_surf = font.render('You lost!', True, RED)
        text_rect = text_surf.get_rect(center = (275, 250))
        font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 50)
        score_surf = font.render(f'Score: {str(len(snake_pos) - 1)}', True, RED)
        score_rect = score_surf.get_rect(center = (275, 300))
        screen.blit(text_surf, text_rect)
        screen.blit(score_surf, score_rect)
        font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 50)
        new_game_text_surf = font.render('New game', True, BLACK)
        new_game_text_rect = new_game_text_surf.get_rect(center = (275, 380))
        new_game_rect = pygame.Rect((175, 350, 200, 50))
        pygame.draw.rect(screen, WHITE, new_game_rect)
        pygame.draw.rect(screen, BLACK, new_game_rect, 2)
        screen.blit(new_game_text_surf,new_game_text_rect)
    elif win:
        font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 200)
        text_surf = font.render('You WIN!', True, RED)
        text_rect = text_surf.get_rect(center = (275, 250))
        screen.blit(text_surf, text_rect)
        font = pygame.font.Font("D:\_Work\_Computer Science\A Level\_random code\Snake\Pixeltype.ttf", 50)
        new_game_text_surf = font.render('New game', True, BLACK)
        new_game_text_rect = new_game_text_surf.get_rect(center = (275, 380))
        new_game_rect = pygame.Rect((175, 350, 200, 50))
        pygame.draw.rect(screen, WHITE, new_game_rect)
        pygame.draw.rect(screen, BLACK, new_game_rect, 2)
        screen.blit(new_game_text_surf,new_game_text_rect)
    else:
        draw_board()
        draw_score((len(snake_pos)))
        draw_snake(snake_pos)
        if new_apple:
            apple_coor = add_apple()
            new_apple = False
        if apple_coor == True:
            win = True
        else:
            draw_apple(apple_coor)
        update_counter += 1
        if update_counter == speed:
            old_key, end, new_apple = move_snake(key, old_key)
            if end:
                lost = True
            update_counter = 0

    pygame.display.update()
    clock.tick(60)