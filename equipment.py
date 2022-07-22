from dataclasses import dataclass
from typing import List
import random
import marshmallow_dataclass
import marshmallow
from utils import load_json


@dataclass
class Weapon:
	id: int
	name: str
	min_damage: float
	max_damage: float
	stamina_per_hit: float

	def get_damage(self) -> float:
		damage = random.uniform(self.min_damage, self.max_damage)
		return round(damage, 1)


@dataclass
class Armor:
	id: int
	name: str
	defence: float
	stamina_per_turn: float


@dataclass
class EquipmentData:
	weapons: List[Weapon]
	armors: List[Armor]


class Equipment:
	def __init__(self, data: dict):
		self._data = data
		self._equip = self._get_data()

	def _get_data(self):
		try:
			equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
			return equipment_schema().load(self._data)
		except marshmallow.exceptions.ValidationError:
			raise ValueError

	def get_weapon(self, weapon: str) -> Weapon:
		for item in self._equip.weapons:
			if weapon == item.name:
				return item

	def get_armor(self, armor: str) -> Armor:
		pass

	def get_weapon_names(self) -> List[str]:
		return [i.name for i in self._equip.weapons]

	def get_armor_names(self) -> List[str]:
		pass


equip_data = load_json('data/equipment.json')
eq_schemf = Equipment(equip_data)
print(eq_schemf.get_weapon_names())
# print(eq_schemf.get_weapon('ладошки'))
