import pygame
import pixelperfect


class BaseEntity(pygame.sprite.Sprite):
    """
    Base Entity Class. All Renderables should derive from this class.
    """
    position = (0, 0)  # Position in pixels
    velocity = (0, 0)  # Velocity in pixels/s
    accel    = (0, 0)  # Acceleration in pixels/s^2
    theta = 0  # Angle in degrees w.r.t. 0 degrees
    omega = 0  # Angular velocity in degrees/s
    alpha = 0  # Angular acceleration in degrees/s^2

    hitrect = None
    image = None
    blit_image = None
    hitmask = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def render(self, screen):
        """
        Render sprite to the screen. If own image is null, it errors.
        :param screen: pygame surface to blit to
        :return: void
        """
        if self.image is not None:
            screen.blit(self.blit_image, self.hitrect)
        else:
            raise Exception("Can't render with a null image")

    def setImage(self, newImage):
        """
        Sets own image to a surface, then uses PixelPerfect to calc hitmasks
        :param newImage:
        :return: void
        """
        try:
            self.image = pygame.image.load(newImage)
        except pygame.error, message:
            print "Couldn't load image:{0}, reverting to fallback".format(newImage)
            print message
            self.image = pygame.image.load("triangle.png")
        self.image = self.image.convert_alpha()
        self.blit_image = self.image
        self.hitrect = self.image.get_rect()
        self.hitrect.center = self.position
        self.hitmask = pixelperfect.get_alpha_hitmask(self.image, self.hitrect)

    def update(self, event=None):
        """Override this to process events. It should adjust it's own parameters here."""
        pass

    def tick(self, delta):
        """
        Physics tick
        :param delta: Delta time
        :return: void
        """
        addVectors = lambda p: p[0] + (p[1] * delta)
        self.position = map(addVectors, zip(self.position, self.velocity))
        self.velocity = map(addVectors, zip(self.velocity, self.accel))
        self.theta += self.omega * delta
        self.omega += self.alpha * delta

        self.blit_image = pygame.transform.rotate(self.image, self.theta)
        self.hitrect = self.blit_image.get_rect()
        self.hitrect.center = self.position
