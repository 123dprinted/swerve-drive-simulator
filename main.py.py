import pygame
import constants

from joystick_handler import JoystickHandler
from bot import Bot

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont('arial', constants.FONTSIZE)

        self.joystick_handler = JoystickHandler()


    def draw_text(self, t):
        self.font = pygame.font.SysFont('roboto', constants.FONTSIZE)

        self.text = self.font.render(t, True, (255, 255, 255))
        return self.text


    def new(self):
        self.playing = True

        self.robots = pygame.sprite.LayeredUpdates()

    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.JOYDEVICEADDED:
                self.joystick = pygame.joystick.Joystick(event.device_index)
                self.joystick_handler.add_joystick(self.joystick)

                self.bot = Bot(self, 300, 300, self.joystick_handler, event.device_index)

    
    def update(self):
        self.robots.update()

    def draw(self):
        self.screen.fill("purple")
        self.robots.draw(self.screen)

        self.controllers = self.draw_text(f"Controllers: {pygame.joystick.get_count()}")
        self.joystick1 = self.joystick_handler.get_joystick(0)

        for joystick in self.joystick_handler.get_joysticks():
            self.controller_type = self.draw_text(f"Controller Type: {joystick.get_name()}")
    
        self.controller_axis0 = self.draw_text(f"Left Axis 0: {self.joystick1.get_axis(0)}")
        self.controller_axis1 = self.draw_text(f"Left Axis 1: {self.joystick1.get_axis(1)}")

        self.controller_axis2 = self.draw_text(f"Right Axis 0: {self.joystick1.get_axis(2)}")
        self.controller_axis3 = self.draw_text(f"Right Axis 1: {self.joystick1.get_axis(3)}")

        self.screen.blit(self.controllers, (0,0))
        self.screen.blit(self.controller_type, (0, 20))

        self.screen.blit(self.controller_axis0, (0, 60))
        self.screen.blit(self.controller_axis1, (0, 80))

        self.screen.blit(self.controller_axis2, (0, 100))
        self.screen.blit(self.controller_axis3, (0, 120))

        self.clock.tick(60)
        pygame.display.update()

    '''
    GAME LOOP
    '''
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


game = Game()
game.new()

while game.running:
    game.main()

pygame.quit()
