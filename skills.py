from abc import ABC, abstractmethod


class Skill(ABC):
	@abstractmethod
	def __init__(self, name: str, damage: float, need_stamina: float):
		self._name = name
		self._damage = damage
		self._need_stamina = need_stamina
		
	@abstractmethod
	def _skill_effect(self):
		pass

	def use(self, user, target):
		if user.stamina >= self._need_stamina:
			return self._skill_effect()
		else:
			return f'{user.name} попытался использовать {self._name}, но у него не хватило выносливости'
