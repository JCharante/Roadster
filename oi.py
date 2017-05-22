import wpilib
from utils.gamepad import Gamepad


class OI:
	def __init__(self):
		self.gamepad = Gamepad
		self.operator_console = wpilib.Joystick(1)


