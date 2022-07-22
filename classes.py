from dataclasses import dataclass


@dataclass
class UnitClass:
	name: str
	max_health: float
	max_stamina: float
	attack: float
	stamina: float
	armor: float
	skill: ConcreteSkill
