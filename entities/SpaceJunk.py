import BaseEntity
import pygame
import random


class SpaceJunk(BaseEntity.BaseEntity):

    def __init__(self):
        BaseEntity.BaseEntity.__init__(self)
        self.setImage("triangle.png")
        self.position = (random.randint(10, 500), random.randint(10, 500))
        self.velocity = (random.randint(-50, 50), random.randint(-50, 50))
        self.accel = (random.randint(-5, 5), random.randint(-5, 5))
        self.theta = random.randint(-180, 180)
        self.omega = random.randint(-25, 25)
        self.alpha = random.randint(-10, 10)

    # This is just a really contrived example to demo how subclassing works. Press 'p' to arrest acceleration.
    # In the full game SpaceJunk shouldn't respond to events like this.
    def update(self, event):
        super(BaseEntity.BaseEntity, self).update(event)
        if event.type == pygame.KEYDOWN and event.key == ord('p'):
            self.velocity = (0, 0)
            self.omega = 0
