import pygame
import math

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))

gameExit = False


x_coord = 300
y_coord = 300

joystick = pygame.joystick.Joystick(0)
joystick.init()

axes = joystick.get_numaxes()
## 0=Left_Stick X-axis, Left == Negative, Right == Positive
## 1=Left_Stick Y-axis, Up == Negative, Down == Positive
## 2=Triggers, Right == Negative, Left == Positive
## 3=Right_Stick Y-axis, Up == Negative, Down == Positive
## 4=Right_Stick X-axis, Left == Negative, Right == Positive

triangle = pygame.image.load("triangle.png")

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    def angle(x,y):
        if y <0 and x >0:
            y*=-1
            answer = math.atan(y/x)
            return 270+math.degrees(answer)
        elif y<0 and x<0:
            y*=-1
            x*=-1
            answer = 360 - math.atan(y/x)
            return math.degrees(answer)
        elif y>0 and x<0:
            x*=-1
            answer = 90+ math.atan(y/x)
            return math.degrees(answer)
        else:
            answer = 180 - math.atan(y/x)
            return math.degrees(answer)


    x_coord += joystick.get_axis(0)
    y_coord += joystick.get_axis(1)

    
    def rot_center(image, angle):

        loc = image.get_rect().center 
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite
    
    x_coordAngle = joystick.get_axis(4)+.0001
    y_coordAngle = joystick.get_axis(3)+.0001

    head = rot_center(triangle, angle(x_coordAngle, y_coordAngle))
        

    gameDisplay.fill((255,255,255))
    
    gameDisplay.blit(head,(x_coord,y_coord))
    pygame.display.update()
pygame.quit()
quit
