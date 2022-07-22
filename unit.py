from abc import ABC, abstractmethod
from classes import UnitClass
from equipment import Weapon, Armor


class BaseUnit(ABC):
	def __init__(self, name: str, unit_class: UnitClass):
		self._name = name
		self._unit_class = unit_class
		self._hp = unit_class.max_health
		self._stamina = unit_class.max_stamina
		self._weapon = None
		self._armor = None
		self._is_used_skill = False

	def get_weapon(self, weapon: Weapon):
		self._weapon = weapon

	def get_armor(self, armor: Armor):
		self._armor = armor

	def _get_damage(self):
		return self._weapon.get_damage()

	def get_self_damage(self):
		pass

	def get_skill_to_target(self):
		pass

	@abstractmethod
	def strike(self):
		pass
