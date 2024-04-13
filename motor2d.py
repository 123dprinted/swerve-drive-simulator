class Motor2D:
    def __init__(self, pos):
        self.pos = pos

        self.vel = 0
        self.angle = 0

    def set_vel(self, vel):
        self.vel = vel

    def set_angle(self, ang):
        self.angle = ang

class Module:
    def __init__(self, fl, fr, bl, br):
        self.module = [fl, fr, bl, br]

    def set_module_state(self, vel, angle):
        for motor in self.module:
            motor.set_vel(vel)
            motor.set_angle(angle)  