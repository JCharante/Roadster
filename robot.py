import wpilib
import logging


class MyRobot(wpilib.IterativeRobot):
    logger = logging.getLogger("robot")

    def robotInit(self):
        # object that handles basic drive operations
        self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.gamepad = wpilib.Joystick(0, 6)

    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)
        self.logger.warning('You have warnings logs on')
        self.logger.info('You have info logs on')

    def teleopPeriodic(self):
        xbox_stick_left_x = round(self.gamepad.getRawAxis(0), 2)
        xbox_stick_left_y = round(self.gamepad.getRawAxis(1), 2)
        xbox_stick_right_x = round(self.gamepad.getRawAxis(4), 2)
        xbox_stick_right_y = round(self.gamepad.getRawAxis(5), 2)
        self.logger.info(f'Gamepad Left X: {xbox_stick_left_x}, Y: {xbox_stick_left_y} | Gamepad Right X: {xbox_stick_right_x}, Y: {xbox_stick_right_y}')
        #self.myRobot.tankDrive(self.leftStick, self.rightStick, True)


if __name__ == '__main__':
    wpilib.run(MyRobot)
