import pygame
import map_maker

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
game_over = False
clock = pygame.time.Clock()

_map = map_maker.get_map()

while not game_over:

    for event in pygame.event.get():

        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            
            game_over = True
    
    screen.fill((0,0,0))

    _map.draw_map(screen)
    


    pygame.display.flip()
    clock.tick(60)