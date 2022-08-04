from constants import STAMINA_PER_ROUND
from unit import BaseUnit
from typing import Optional


class BaseSingleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
	stamina_per_round = STAMINA_PER_ROUND
	user: BaseUnit
	pc: BaseUnit
	battle_result: str
	game_is_running = False

	def start_game(self, user: BaseUnit, pc: BaseUnit):
		self.game_is_running = True
		self.user = user
		self.pc = pc

	def next_turn(self) -> str:
		if self.check_hp():
			return self.check_hp()
		pc_hit = self.pc.hit(self.user)
		self.stamina_regeneration()
		return pc_hit

	def stamina_regeneration(self):
		self.user.stamina = round(self.user.stamina + self.stamina_per_round * self.user.stamina_modify, 1)
		if self.user.stamina > self.user.unit_class.max_stamina:
			self.user.stamina = self.user.unit_class.max_stamina

		self.pc.stamina = round(self.pc.stamina + self.stamina_per_round * self.pc.stamina_modify, 1)
		if self.pc.stamina > self.pc.unit_class.max_stamina:
			self.pc.stamina = self.pc.unit_class.max_stamina

	def check_hp(self) -> Optional[str]:
		if self.user.hp > 0 and self.pc.hp > 0:
			return None
		elif self.user.hp > 0:
			battle_result = 'Игрок победил!'
		elif self.pc.hp > 0:
			battle_result = 'Игрок проиграл!'
		else:
			battle_result = 'Ничья!'
		self.battle_result = battle_result
		return battle_result

	def game_over(self) -> str:
		self._instances = {}
		self.game_is_running = False
		return self.battle_result

	def users_hit(self) -> str:
		result = self.user.hit(self.pc)
		# self.next_turn()
		return result

	def used_skill(self) -> str:
		result = self.user.get_skill_to_target(self.pc)
		# self.next_turn()
		return result
