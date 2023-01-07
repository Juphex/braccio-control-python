import braccio_adapter
from enum import Enum
from pynput import keyboard

class ServoMotor(Enum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6

class BraccioDebug(braccio_adapter.BraccioAdapter):
    def __init__(self, serial_port_robot_magnet="COM3"):
        super().__init__(serial_port_robot_magnet,)
        self.home_position()

    def move_single_joint(self, servo, degrees):
        # get currect vals
        s1 = self.s1
        s2 = self.s2 
        s3 = self.s3
        s4 = self.s4 
        s5 = self.s5
        s6 = self.s6

        if servo.value == 1:
            s1 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
        if servo.value == 2:
            s2 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
        if servo.value == 3:
            s3 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
        if servo.value == 4:
            s4 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
        if servo.value == 5:
            s5 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
        if servo.value == 6:
            s6 += degrees
            self.servo_movement(s1, s2, s3, s4, s5, s6)
    
    def up(self, servo : ServoMotor, degrees = 1):
        self.move_single_joint(servo, degrees)
        
    def down(self, servo: ServoMotor, degrees = -1):
        self.move_single_joint(servo, degrees)

if __name__ == "__main__":
    braccioDebug :BraccioDebug = BraccioDebug(serial_port_robot_magnet="COM3")
    braccioControlString = "Control the Braccio using: \n\
                            Servo 1 UP/DOWN Q/A\n\
                            Servo 2 UP/DOWN W/S\n\
                            Servo 3 UP/DOWN E/D\n\
                            Servo 4 UP/DOWN R/F\n\
                            Servo 5 UP/DOWN T/G\n\
                            Servo 6 UP/DOWN Z/H\n\
                            HOME C\
                            "
    print(braccioControlString)

    print("Control Positions Positions: \n")
    while True:
        with keyboard.Events() as events:
            # Block for as much as possible
            event = events.get(1e6)
            if event.key == keyboard.KeyCode.from_char('q'):
                braccioDebug.up(ServoMotor.S1)
            elif event.key == keyboard.KeyCode.from_char('w'):
                braccioDebug.up(ServoMotor.S2)
            elif event.key == keyboard.KeyCode.from_char('e'):
                braccioDebug.up(ServoMotor.S3)
            elif event.key == keyboard.KeyCode.from_char('r'):
                braccioDebug.up(ServoMotor.S4)
            elif event.key == keyboard.KeyCode.from_char('t'):
                braccioDebug.up(ServoMotor.S5)
            elif event.key == keyboard.KeyCode.from_char('z'):
                braccioDebug.up(ServoMotor.S6)
            elif event.key == keyboard.KeyCode.from_char('a'):
                braccioDebug.down(ServoMotor.S1)
            elif event.key == keyboard.KeyCode.from_char('s'):
                braccioDebug.down(ServoMotor.S2)
            elif event.key == keyboard.KeyCode.from_char('d'):
                braccioDebug.down(ServoMotor.S3)
            elif event.key == keyboard.KeyCode.from_char('f'):
                braccioDebug.down(ServoMotor.S4)
            elif event.key == keyboard.KeyCode.from_char('g'):
                braccioDebug.down(ServoMotor.S5)
            elif event.key == keyboard.KeyCode.from_char('h'):
                braccioDebug.down(ServoMotor.S6)
            elif event.key == keyboard.KeyCode.from_char('c'):
                braccioDebug.home_position()
        print(f"{braccioDebug.s1}, \
            {braccioDebug.s2}, {braccioDebug.s3}, \
                {braccioDebug.s4}, {braccioDebug.s5}, \
                    {braccioDebug.s6}", end="\r")
