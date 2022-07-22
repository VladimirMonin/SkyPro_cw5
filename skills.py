from avc import ABC, abstractmethod


class Skill(ABC):
	@abstractmethod
	def __init__(self, name: str, damage: float, need_stamina:float):
		self._name = name
		self._damage = damage
		self._need_stamina = float
		
	@abstractmethod
	def _skill_effect(self):
		pass

	def use(self, user, target):
		if user.stamina >= self._need_stamina:
			return self._skill_effect()
		else:
			return f'{user.name} попытался использовать {self.name}, но у него не хватило выносливости'

	




























input()