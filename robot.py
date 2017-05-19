import wpilib
import logging

from utils.gamepad import Gamepad


class MyRobot(wpilib.IterativeRobot):
	logger = logging.getLogger("robot")

	def robotInit(self):
		# object that handles basic drive operations
		self.myRobot = wpilib.RobotDrive(0, 1)
		self.myRobot.setExpiration(0.1)

		# joysticks 1 & 2 on the driver station
		self.gamepad = Gamepad(0)
		# self.operatorConsole = wpilib.Joystick(1)

	def teleopInit(self):
		self.myRobot.setSafetyEnabled(True)
		self.logger.warning('You have warnings logs on')
		self.logger.info('You have info logs on')

	def teleopPeriodic(self):
		self.logger.info(f'Gamepad Left X: {self.gamepad.LEFT_X.val(2)}, Y: {self.gamepad.LEFT_Y.val(2)} | Gamepad Right X: {self.gamepad.RIGHT_X.val(2)}, Y: {self.gamepad.RIGHT_Y.val(2)}')
		# self.myRobot.tankDrive(self.leftStick, self.rightStick, True)


if __name__ == '__main__':
	wpilib.run(MyRobot)
