#!/usr/bin/python

import pygame, time
from entities import BaseEntity

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    exit = False
    lastTime = time.time()

    Player = BaseEntity.BaseEntity()
    Player.setImage("triangle.png")
    Player.velocity = [100, 100]
    Player.accel = [-10, -10]
    Player.alpha = 15
    Player.theta = -45

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            else:
                # In the future this will be replaced by an Active SpriteGroup
                Player.update(event)

        Player.tick(time.time() - lastTime)
        lastTime = time.time()
        screen.fill([255, 255, 255])
        Player.render(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()