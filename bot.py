import pygame
from joystick_handler import JoystickHandler
from motor2d import Motor2D, Module

class Bot(pygame.sprite.Sprite):
    def __init__(self, game, x, y, joystick_handler, id):
        self.game = game
        self.groups = self.game.robots

        pygame.sprite.Sprite.__init__(self, self.groups)

        
        self.original_image = pygame.image.load("bot.png").convert()
        self.original_image.set_colorkey("white")
        self.image = self.original_image.copy()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0

        self.x_change = 0
        self.y_change = 0

        self.FL_Motor = Motor2D((0, 1))
        self.FR_Motor = Motor2D((1, 1))
        self.BL_Motor = Motor2D((0, 0))
        self.BR_Motor = Motor2D((1, 0))

        self.module = Module(self.FL_Motor, self.FR_Motor, self.BL_Motor, self.BR_Motor)

        self.joystick_handler = joystick_handler
        
        self.joystick = self.joystick_handler.get_joystick(id)

    def update(self):
         self.movement()
         self.rotate()

         self.rect.x += self.x_change
         self.rect.y += self.y_change

         self.x_change = 0
         self.y_change = 0

    def movement(self):
        self.x_change += self.joystick_handler.get_ajusted_axis(self.joystick, 0)
        self.y_change += self.joystick_handler.get_ajusted_axis(self.joystick, 1)

        self.module.set_module_state()
    
    
    def rotate(self):
        # Get the current joystick angle
        self.angle += -self.joystick_handler.get_ajusted_axis(self.joystick, 2) * .35

        # Rotate the image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # Get the rect of the rotated image and update its position
        self.rect = self.image.get_rect(center=self.rect.center)

        self.angle %= 360
