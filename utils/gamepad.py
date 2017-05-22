import wpilib


class Gamepad(wpilib.XboxController):
	def __init__(self, port: int):
		super().__init__(port)

	def getX(self, hand, decimal_places=None):
		return super().getX(hand) * -1 if decimal_places is None else round(super().getX(hand) * -1, decimal_places)

	def getY(self, hand, decimal_places=None):
		return super().getY(hand) * -1 if decimal_places is None else round(super().getY(hand) * -1, decimal_places)
