import wpilib
import logging
from oi import OI

from utils.gamepad import Gamepad


class MyRobot(wpilib.IterativeRobot):
	logger = logging.getLogger("robot")

	def robotInit(self):
		# object that handles basic drive operations
		self.myRobot = wpilib.RobotDrive(0, 1)
		self.myRobot.setExpiration(0.1)

		self.oi = OI()

	def teleopInit(self):
		self.myRobot.setSafetyEnabled(True)
		self.logger.warning('You have warnings logs on')
		self.logger.info('You have info logs on')

	def teleopPeriodic(self):
		self.logger.info(f"Gamepad Left X: {self.oi.gamepad.getX('left', 2)}, Y: {self.oi.gamepad.getY('left', 2)} | Gamepad Right X: {self.oi.gamepad.getX('right', 2)}, Y: {self.oi.gamepad.getY('right', 2)}")
		# self.myRobot.tankDrive(self.leftStick, self.rightStick, True)


if __name__ == '__main__':
	wpilib.run(MyRobot)
