import constants

class JoystickHandler:
    def __init__(self):
        self.joysticks = []
    
    def add_joystick(self, joystick):
        self.joysticks.append(joystick)

    def get_joysticks(self):
        return self.joysticks
    
    def get_joystick(self, index):
        return self.joysticks[index]
    
    def get_ajusted_axis(self, joystick, axis):
        if abs(joystick.get_axis(axis)) > constants.DEADBAND:
            return round(joystick.get_axis(axis) * 10)
        else:
            return 0



