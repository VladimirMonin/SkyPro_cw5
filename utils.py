import json


def load_json(path: str) -> dict:
	"""Загружает данные из json-файла"""
	with open(path, 'r', encoding='utf-8') as file:
		return json.load(file)
