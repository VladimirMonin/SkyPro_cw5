class Arena:
	def __init__(self, stamina: float, user, pc):
		self._stamina = stamina
		self._user = user
		self._pc = pc
		self._is_game = False

	def start_game(self):
		self._is_game = True
		pass

	def _next_step(self):
		pass

	def regeneration(self):
		pass

	def check_hp(self):
		if self._user.hp <= 0 or self._pc.hp <= 0:
			self._end_of_game()

	def _end_of_game(self):
		pass

	def users_hit(self):
		self._next_step()
		pass

	def used_skill(self):
		pass