import wpilib


class GamepadAxis:
	def __init__(self, gamepad: 'Gamepad', axis: int, invert=False):
		self.gamepad = gamepad
		self.axis = axis
		self.invert = invert

	def val(self, decimal_places=None):
		if self.invert:
			return self.gamepad.getRawAxis(self.axis) * -1 if round is None else round(self.gamepad.getRawAxis(self.axis) * -1, decimal_places)
		else:
			return self.gamepad.getRawAxis(self.axis) if round is None else round(self.gamepad.getRawAxis(self.axis), decimal_places)


class GamepadButton:
	def __init__(self, gamepad: 'Gamepad', button_number: int):
		self.gamepad = gamepad
		self.button_number = button_number

	def isPressed(self):
		return self.gamepad.getRawButton(self.button_number)


class Gamepad(wpilib.Joystick):
	def __init__(self, port: int):
		super().__init__(port)
		self.LEFT_X = GamepadAxis(self, 0)
		self.LEFT_Y = GamepadAxis(self, 1, True)
		self.LEFT_TRIGGER = GamepadAxis(self, 2)
		self.RIGHT_TRIGGER = GamepadAxis(self, 3)
		self.RIGHT_X = GamepadAxis(self, 4)
		self.RIGHT_Y = GamepadAxis(self, 5, True)
		self.D_PAD_HORIZONTAL = GamepadAxis(self, 6)
		self.D_PAD_VERTICAL = GamepadAxis(self, 7)
