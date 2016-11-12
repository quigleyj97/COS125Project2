#!/usr/bin/python

import pygame, time
from entities import BaseEntity, SpaceJunk

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    exit = False
    lastTime = time.time()

    ActiveSpriteGroup = pygame.sprite.Group()

    Player = BaseEntity.BaseEntity()
    Player.setImage("triangle.png")
    Player.velocity = [100, 100]
    Player.accel = [-10, -10]
    Player.alpha = 15
    Player.theta = -45

    ActiveSpriteGroup.add(Player)

    for i in range(10):
        ActiveSpriteGroup.add(SpaceJunk.SpaceJunk())

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            else:
                ActiveSpriteGroup.update(event)

        screen.fill([255, 255, 255])

        for sprite in ActiveSpriteGroup:
            sprite.tick(time.time() - lastTime)
            sprite.render(screen)
        lastTime = time.time()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()