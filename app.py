from flask import Flask, render_template, request, redirect
from classes import unit_classes
from equipment import Equipment

from arena import Arena
from unit import BaseUnit, UserUnit, PC_Unit

app = Flask(__name__)

heroes = {
	"player": BaseUnit,
	"enemy": BaseUnit
}

arena = Arena()
equipment = Equipment()


@app.route('/')
def index():
	return render_template('index.html')


@app.route("/choose-hero/", methods=['POST', 'GET'])
def choose_hero():
	if request.method == 'GET':
		result = {
			'classes': unit_classes.keys(),
			'weapons': equipment.get_weapon_names(),
			'armors': equipment.get_armor_names()
		}
		return render_template('hero_choosing.html', result=result)

	elif request.method == 'POST':
		result = dict(request.form)
		heroes['player'] = UserUnit(
			name=result.get('name'),
			unit_class=unit_classes[result.get('unit_class')]
		)
		weapon = equipment.get_weapon(result.get('weapon'))
		armor = equipment.get_armor(result.get('armor'))
		heroes['player'].equip_weapon(weapon)
		heroes['player'].equip_armor(armor)
		return redirect('/choose-enemy/')


@app.route("/choose-enemy/", methods=['POST', 'GET'])
def choose_enemy():
	if request.method == 'GET':
		result = {
			'classes': unit_classes.keys(),
			'weapons': equipment.get_weapon_names(),
			'armors': equipment.get_armor_names()
		}
		return render_template('hero_choosing.html', result=result)

	elif request.method == 'POST':
		result = dict(request.form)
		heroes['enemy'] = PC_Unit(
			name=result.get('name'),
			unit_class=unit_classes[result.get('unit_class')]
		)
		weapon = equipment.get_weapon(result.get('weapon'))
		armor = equipment.get_armor(result.get('armor'))
		heroes['enemy'].equip_weapon(weapon)
		heroes['enemy'].equip_armor(armor)
		return redirect('/fight/')


@app.route("/fight/")
def start_fight():
	arena.start_game(user=heroes.get('player'), pc=heroes.get('enemy'))
	return render_template('fight.html', heroes=heroes)


@app.route("/fight/hit")
def hit():
	result = ''
	if arena.game_is_running:
		result = arena.users_hit()
	result += arena.next_turn()
	return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
	result = arena.used_skill()
	if result:
		result += arena.next_turn()
	else:
		result = 'Навык уже использован'
	return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
	result = arena.next_turn()
	return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)


