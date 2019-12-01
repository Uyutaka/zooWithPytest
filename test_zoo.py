import sys
import pytest
import random


# https://raw.githubusercontent.com/sanikadongre/OOAD_F19_Homeworks_Projects/master/Project2/Q1a/zoo.py
from zoo import Animal
from zoo import Canine
from zoo import Feline
from zoo import Pachyderm
from zoo import Cat
from zoo import Elephant
from zoo import Hippo
from zoo import Lion
from zoo import Rhino
from zoo import Tiger
from zoo import Wolf
from zoo import Dog
from zoo import ZooKeeper

@pytest.fixture()
def getAnimal():
	animal = Animal("name")
	return animal

def test_animal_wakeUp(getAnimal, capsys):
	getAnimal.wakeUp()
	out, err = capsys.readouterr()
	assert out == "name The animal wakes up.\n"

def test_animal_sleep(getAnimal, capsys):
	getAnimal.sleep()
	out, err = capsys.readouterr()
	assert out == "name The animal sleeps.\n"

def test_animal_eat(getAnimal, capsys):
	getAnimal.eat()
	out, err = capsys.readouterr()
	assert out == "name The animal eats.\n"

def test_animal_roam(getAnimal, capsys):
	getAnimal.roam()
	out, err = capsys.readouterr()
	assert out == ""
def test_animal_makeNoise(getAnimal, capsys):
	getAnimal.makeNoise()
	out, err = capsys.readouterr()
	assert out == ""

@pytest.fixture()
def getCanine():
	canine = Canine("name")
	return canine

def test_canine_eat(getCanine, capsys):
	getCanine.eat()
	out, err = capsys.readouterr()
	assert out == "name The Canine animal eats meat.\n"

def test_canine_roam(getCanine, capsys):
	getCanine.roam()
	out, err = capsys.readouterr()
	assert out == "name The Canine animal roams in pack.\n"

@pytest.fixture()
def getFeline():
	feline = Feline("name")
	return feline

def test_feline_eat(getFeline, capsys):
	getFeline.eat()
	out, err = capsys.readouterr()
	assert out == "name The Feline animal eats raw meat.\n"

def test_feline_roam(getFeline, capsys):
	getFeline.roam()
	out, err = capsys.readouterr()
	assert out == "name The Feline animal roams individually/alone.\n"

@pytest.fixture()
def getPachyderm():
	pachyderm = Pachyderm("name")
	return pachyderm

def test_pachyderm_eat(getPachyderm, capsys):
	getPachyderm.eat()
	out, err = capsys.readouterr()
	assert out == "name The Pachyderm animal eats grass and/or some meat.\n"

def test_pachyderm_roam(getPachyderm, capsys):
	getPachyderm.roam()
	out, err = capsys.readouterr()
	assert out == "name The Pachyderm animal roams in herds or by itself.\n"

@pytest.fixture()
def getCat():
	cat = Cat("name")
	return cat

def test_cat_makeNoise(getCat, capsys):
	getCat.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Cat makes noise Meow.\n" or out == "name Cat makes noise Meowwww and Meowwww.\n"
def test_cat_roam(getCat, capsys):
	getCat.roam()
	out, err = capsys.readouterr()
	assert out == "name Cat exercises by stretching and licking itself.\n" or out == "name Cat exercises by playing with itself and purring.\n"

@pytest.fixture()
def getElephant():
	elephant = Elephant("name")
	return elephant
def test_elephant_makeNoise(getElephant, capsys):
	getElephant.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Elephant makes noise Mooooo.\n"
def test_elephant_roam(getElephant, capsys):
	getElephant.roam()
	out, err = capsys.readouterr()
	assert out == "name Elephant exercises by moving and bathing in the muddy water.\n"

@pytest.fixture()
def getHippo():
	hippo = Hippo("name")
	return hippo
def test_hippo_makeNoise(getHippo, capsys):
	getHippo.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Hippo makes noise Hipooo.\n"

def test_hippo_roam(getHippo, capsys):
	getHippo.roam()
	out, err = capsys.readouterr()
	assert out == "name Hippo exercises by jumping up and down in the water.\n"

@pytest.fixture()
def getLion():
	lion = Lion("name")
	return lion
def test_lion_makeNoise(getLion, capsys):
	getLion.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Lion makes noise LionGrrr.\n"
def test_lion_roam(getLion, capsys):
	getLion.roam()
	out, err = capsys.readouterr()
	assert out == "name Lion exercises by running quick and putting claws in trees.\n"

@pytest.fixture()
def getRhino():
	rhino = Rhino("name")
	return rhino

def test_rhino_makeNoise(getRhino, capsys):
	getRhino.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Rhino makes noise Rhinooo.\n"
def test_rhino_roam(getRhino, capsys):
	getRhino.roam()
	out, err = capsys.readouterr()
	assert out == "name Rhino exercises by jumping up and down in the grass.\n"

@pytest.fixture()
def getTiger():
	tiger = Tiger("name")
	return tiger

def test_tiger_makeNoise(getTiger, capsys):
	getTiger.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Tiger makes noise Tigrrrrr.\n"
def test_tiger_roam(getTiger, capsys):
	getTiger.roam()
	out, err = capsys.readouterr()
	assert out == "name Tiger exercises by running quick and putting claws in trees.\n"

@pytest.fixture()
def getWolf():
	wolf = Wolf("name")
	return wolf

def test_wolf_makeNoise(getWolf, capsys):
	getWolf.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Wolf makes noise Grrrrr.\n"
def test_wolf_roam(getWolf, capsys):
	getWolf.roam()
	out, err = capsys.readouterr()
	assert out == "name Wolf exercises by stretching and licking itself.\n"

@pytest.fixture()
def getDog():
	dog = Dog("name")
	return dog
def test_dog_makeNoise(getDog, capsys):
	getDog.makeNoise()
	out, err = capsys.readouterr()
	assert out == "name Dog makes noise Woof.\n"
def test_dog_roam(getDog, capsys):
	getDog.roam()
	out, err = capsys.readouterr()
	assert out == "name Dog exercises by stretching and sprinting.\n"


def test_zookeeper_init(capsys):
	ZooKeeper()
	out, err = capsys.readouterr()
	assert out == """----- Day At the Zoo: Output -----
Zoo Opened.

----------- wakeUpAnimals --------------
Cheshire The animal wakes up.
Cuddles The animal wakes up.
Leo The animal wakes up.
Lewis The animal wakes up.
Tigran The animal wakes up.
Tigru The animal wakes up.
Ellen The animal wakes up.
Elson The animal wakes up.
Deo The animal wakes up.
Dawn The animal wakes up.
Hank The animal wakes up.
Hustler The animal wakes up.
Rincon The animal wakes up.
Ruben The animal wakes up.
Ruben The animal wakes up.
Will The animal wakes up.
Wiz The animal wakes up.
----------- rollCallAnimals --------------
Cheshire Cat makes noise Meow.
Cuddles Cat makes noise Meow.
Leo Lion makes noise LionGrrr.
Lewis Lion makes noise LionGrrr.
Tigran Tiger makes noise Tigrrrrr.
Tigru Tiger makes noise Tigrrrrr.
Ellen Elephant makes noise Mooooo.
Elson Elephant makes noise Mooooo.
Deo Dog makes noise Woof.
Dawn Dog makes noise Woof.
Hank Hippo makes noise Hipooo.
Hustler Hippo makes noise Hipooo.
Rincon Rhino makes noise Rhinooo.
Ruben Rhino makes noise Rhinooo.
Ruben Tiger makes noise Tigrrrrr.
Will Wolf makes noise Grrrrr.
Wiz Wolf makes noise Grrrrr.
----------- feedAnimals --------------
Cheshire The Feline animal eats raw meat.
Cuddles The Feline animal eats raw meat.
Leo The Feline animal eats raw meat.
Lewis The Feline animal eats raw meat.
Tigran The Feline animal eats raw meat.
Tigru The Feline animal eats raw meat.
Ellen The Pachyderm animal eats grass and/or some meat.
Elson The Pachyderm animal eats grass and/or some meat.
Deo The Canine animal eats meat.
Dawn The Canine animal eats meat.
Hank The Pachyderm animal eats grass and/or some meat.
Hustler The Pachyderm animal eats grass and/or some meat.
Rincon The Pachyderm animal eats grass and/or some meat.
Ruben The Pachyderm animal eats grass and/or some meat.
Ruben The Feline animal eats raw meat.
Will The Canine animal eats meat.
Wiz The Canine animal eats meat.
------------ exerciseAnimals -------------
Cheshire Cat exercises by playing with itself and purring.
Cuddles Cat exercises by playing with itself and purring.
Leo Lion exercises by running quick and putting claws in trees.
Lewis Lion exercises by running quick and putting claws in trees.
Tigran Tiger exercises by running quick and putting claws in trees.
Tigru Tiger exercises by running quick and putting claws in trees.
Ellen Elephant exercises by moving and bathing in the muddy water.
Elson Elephant exercises by moving and bathing in the muddy water.
Deo Dog exercises by stretching and sprinting.
Dawn Dog exercises by stretching and sprinting.
Hank Hippo exercises by jumping up and down in the water.
Hustler Hippo exercises by jumping up and down in the water.
Rincon Rhino exercises by jumping up and down in the grass.
Ruben Rhino exercises by jumping up and down in the grass.
Ruben Tiger exercises by running quick and putting claws in trees.
Will Wolf exercises by stretching and licking itself.
Wiz Wolf exercises by stretching and licking itself.
------------ shutDownZoo -------------
Cheshire The animal sleeps.
Cuddles The animal sleeps.
Leo The animal sleeps.
Lewis The animal sleeps.
Tigran The animal sleeps.
Tigru The animal sleeps.
Ellen The animal sleeps.
Elson The animal sleeps.
Deo The animal sleeps.
Dawn The animal sleeps.
Hank The animal sleeps.
Hustler The animal sleeps.
Rincon The animal sleeps.
Ruben The animal sleeps.
Ruben The animal sleeps.
Will The animal sleeps.
Wiz The animal sleeps.

Zoo Closed
""" or out == """----- Day At the Zoo: Output -----
Zoo Opened.

----------- wakeUpAnimals --------------
Cheshire The animal wakes up.
Cuddles The animal wakes up.
Leo The animal wakes up.
Lewis The animal wakes up.
Tigran The animal wakes up.
Tigru The animal wakes up.
Ellen The animal wakes up.
Elson The animal wakes up.
Deo The animal wakes up.
Dawn The animal wakes up.
Hank The animal wakes up.
Hustler The animal wakes up.
Rincon The animal wakes up.
Ruben The animal wakes up.
Ruben The animal wakes up.
Will The animal wakes up.
Wiz The animal wakes up.
----------- rollCallAnimals --------------
Cheshire Cat makes noise Meow.
Cuddles Cat makes noise Meow.
Leo Lion makes noise LionGrrr.
Lewis Lion makes noise LionGrrr.
Tigran Tiger makes noise Tigrrrrr.
Tigru Tiger makes noise Tigrrrrr.
Ellen Elephant makes noise Mooooo.
Elson Elephant makes noise Mooooo.
Deo Dog makes noise Woof.
Dawn Dog makes noise Woof.
Hank Hippo makes noise Hipooo.
Hustler Hippo makes noise Hipooo.
Rincon Rhino makes noise Rhinooo.
Ruben Rhino makes noise Rhinooo.
Ruben Tiger makes noise Tigrrrrr.
Will Wolf makes noise Grrrrr.
Wiz Wolf makes noise Grrrrr.
----------- feedAnimals --------------
Cheshire The Feline animal eats raw meat.
Cuddles The Feline animal eats raw meat.
Leo The Feline animal eats raw meat.
Lewis The Feline animal eats raw meat.
Tigran The Feline animal eats raw meat.
Tigru The Feline animal eats raw meat.
Ellen The Pachyderm animal eats grass and/or some meat.
Elson The Pachyderm animal eats grass and/or some meat.
Deo The Canine animal eats meat.
Dawn The Canine animal eats meat.
Hank The Pachyderm animal eats grass and/or some meat.
Hustler The Pachyderm animal eats grass and/or some meat.
Rincon The Pachyderm animal eats grass and/or some meat.
Ruben The Pachyderm animal eats grass and/or some meat.
Ruben The Feline animal eats raw meat.
Will The Canine animal eats meat.
Wiz The Canine animal eats meat.
------------ exerciseAnimals -------------
Cheshire Cat exercises by stretching and licking itself.
Cuddles Cat exercises by stretching and licking itself.
Leo Lion exercises by running quick and putting claws in trees.
Lewis Lion exercises by running quick and putting claws in trees.
Tigran Tiger exercises by running quick and putting claws in trees.
Tigru Tiger exercises by running quick and putting claws in trees.
Ellen Elephant exercises by moving and bathing in the muddy water.
Elson Elephant exercises by moving and bathing in the muddy water.
Deo Dog exercises by stretching and sprinting.
Dawn Dog exercises by stretching and sprinting.
Hank Hippo exercises by jumping up and down in the water.
Hustler Hippo exercises by jumping up and down in the water.
Rincon Rhino exercises by jumping up and down in the grass.
Ruben Rhino exercises by jumping up and down in the grass.
Ruben Tiger exercises by running quick and putting claws in trees.
Will Wolf exercises by stretching and licking itself.
Wiz Wolf exercises by stretching and licking itself.
------------ shutDownZoo -------------
Cheshire The animal sleeps.
Cuddles The animal sleeps.
Leo The animal sleeps.
Lewis The animal sleeps.
Tigran The animal sleeps.
Tigru The animal sleeps.
Ellen The animal sleeps.
Elson The animal sleeps.
Deo The animal sleeps.
Dawn The animal sleeps.
Hank The animal sleeps.
Hustler The animal sleeps.
Rincon The animal sleeps.
Ruben The animal sleeps.
Ruben The animal sleeps.
Will The animal sleeps.
Wiz The animal sleeps.

Zoo Closed
""" or out == """----- Day At the Zoo: Output -----
Zoo Opened.

----------- wakeUpAnimals --------------
Cheshire The animal wakes up.
Cuddles The animal wakes up.
Leo The animal wakes up.
Lewis The animal wakes up.
Tigran The animal wakes up.
Tigru The animal wakes up.
Ellen The animal wakes up.
Elson The animal wakes up.
Deo The animal wakes up.
Dawn The animal wakes up.
Hank The animal wakes up.
Hustler The animal wakes up.
Rincon The animal wakes up.
Ruben The animal wakes up.
Ruben The animal wakes up.
Will The animal wakes up.
Wiz The animal wakes up.
----------- rollCallAnimals --------------
Cheshire Cat makes noise Meow.
Cuddles Cat makes noise Meow.
Leo Lion makes noise LionGrrr.
Lewis Lion makes noise LionGrrr.
Tigran Tiger makes noise Tigrrrrr.
Tigru Tiger makes noise Tigrrrrr.
Ellen Elephant makes noise Mooooo.
Elson Elephant makes noise Mooooo.
Deo Dog makes noise Woof.
Dawn Dog makes noise Woof.
Hank Hippo makes noise Hipooo.
Hustler Hippo makes noise Hipooo.
Rincon Rhino makes noise Rhinooo.
Ruben Rhino makes noise Rhinooo.
Ruben Tiger makes noise Tigrrrrr.
Will Wolf makes noise Grrrrr.
Wiz Wolf makes noise Grrrrr.
----------- feedAnimals --------------
Cheshire The Feline animal eats raw meat.
Cuddles The Feline animal eats raw meat.
Leo The Feline animal eats raw meat.
Lewis The Feline animal eats raw meat.
Tigran The Feline animal eats raw meat.
Tigru The Feline animal eats raw meat.
Ellen The Pachyderm animal eats grass and/or some meat.
Elson The Pachyderm animal eats grass and/or some meat.
Deo The Canine animal eats meat.
Dawn The Canine animal eats meat.
Hank The Pachyderm animal eats grass and/or some meat.
Hustler The Pachyderm animal eats grass and/or some meat.
Rincon The Pachyderm animal eats grass and/or some meat.
Ruben The Pachyderm animal eats grass and/or some meat.
Ruben The Feline animal eats raw meat.
Will The Canine animal eats meat.
Wiz The Canine animal eats meat.
------------ exerciseAnimals -------------
Cheshire Cat exercises by playing with itself and purring.
Cuddles Cat exercises by stretching and licking itself.
Leo Lion exercises by running quick and putting claws in trees.
Lewis Lion exercises by running quick and putting claws in trees.
Tigran Tiger exercises by running quick and putting claws in trees.
Tigru Tiger exercises by running quick and putting claws in trees.
Ellen Elephant exercises by moving and bathing in the muddy water.
Elson Elephant exercises by moving and bathing in the muddy water.
Deo Dog exercises by stretching and sprinting.
Dawn Dog exercises by stretching and sprinting.
Hank Hippo exercises by jumping up and down in the water.
Hustler Hippo exercises by jumping up and down in the water.
Rincon Rhino exercises by jumping up and down in the grass.
Ruben Rhino exercises by jumping up and down in the grass.
Ruben Tiger exercises by running quick and putting claws in trees.
Will Wolf exercises by stretching and licking itself.
Wiz Wolf exercises by stretching and licking itself.
------------ shutDownZoo -------------
Cheshire The animal sleeps.
Cuddles The animal sleeps.
Leo The animal sleeps.
Lewis The animal sleeps.
Tigran The animal sleeps.
Tigru The animal sleeps.
Ellen The animal sleeps.
Elson The animal sleeps.
Deo The animal sleeps.
Dawn The animal sleeps.
Hank The animal sleeps.
Hustler The animal sleeps.
Rincon The animal sleeps.
Ruben The animal sleeps.
Ruben The animal sleeps.
Will The animal sleeps.
Wiz The animal sleeps.

Zoo Closed
""" or out == """----- Day At the Zoo: Output -----
Zoo Opened.

----------- wakeUpAnimals --------------
Cheshire The animal wakes up.
Cuddles The animal wakes up.
Leo The animal wakes up.
Lewis The animal wakes up.
Tigran The animal wakes up.
Tigru The animal wakes up.
Ellen The animal wakes up.
Elson The animal wakes up.
Deo The animal wakes up.
Dawn The animal wakes up.
Hank The animal wakes up.
Hustler The animal wakes up.
Rincon The animal wakes up.
Ruben The animal wakes up.
Ruben The animal wakes up.
Will The animal wakes up.
Wiz The animal wakes up.
----------- rollCallAnimals --------------
Cheshire Cat makes noise Meow.
Cuddles Cat makes noise Meow.
Leo Lion makes noise LionGrrr.
Lewis Lion makes noise LionGrrr.
Tigran Tiger makes noise Tigrrrrr.
Tigru Tiger makes noise Tigrrrrr.
Ellen Elephant makes noise Mooooo.
Elson Elephant makes noise Mooooo.
Deo Dog makes noise Woof.
Dawn Dog makes noise Woof.
Hank Hippo makes noise Hipooo.
Hustler Hippo makes noise Hipooo.
Rincon Rhino makes noise Rhinooo.
Ruben Rhino makes noise Rhinooo.
Ruben Tiger makes noise Tigrrrrr.
Will Wolf makes noise Grrrrr.
Wiz Wolf makes noise Grrrrr.
----------- feedAnimals --------------
Cheshire The Feline animal eats raw meat.
Cuddles The Feline animal eats raw meat.
Leo The Feline animal eats raw meat.
Lewis The Feline animal eats raw meat.
Tigran The Feline animal eats raw meat.
Tigru The Feline animal eats raw meat.
Ellen The Pachyderm animal eats grass and/or some meat.
Elson The Pachyderm animal eats grass and/or some meat.
Deo The Canine animal eats meat.
Dawn The Canine animal eats meat.
Hank The Pachyderm animal eats grass and/or some meat.
Hustler The Pachyderm animal eats grass and/or some meat.
Rincon The Pachyderm animal eats grass and/or some meat.
Ruben The Pachyderm animal eats grass and/or some meat.
Ruben The Feline animal eats raw meat.
Will The Canine animal eats meat.
Wiz The Canine animal eats meat.
------------ exerciseAnimals -------------
Cheshire Cat exercises by stretching and licking itself.
Cuddles Cat exercises by playing with itself and purring.
Leo Lion exercises by running quick and putting claws in trees.
Lewis Lion exercises by running quick and putting claws in trees.
Tigran Tiger exercises by running quick and putting claws in trees.
Tigru Tiger exercises by running quick and putting claws in trees.
Ellen Elephant exercises by moving and bathing in the muddy water.
Elson Elephant exercises by moving and bathing in the muddy water.
Deo Dog exercises by stretching and sprinting.
Dawn Dog exercises by stretching and sprinting.
Hank Hippo exercises by jumping up and down in the water.
Hustler Hippo exercises by jumping up and down in the water.
Rincon Rhino exercises by jumping up and down in the grass.
Ruben Rhino exercises by jumping up and down in the grass.
Ruben Tiger exercises by running quick and putting claws in trees.
Will Wolf exercises by stretching and licking itself.
Wiz Wolf exercises by stretching and licking itself.
------------ shutDownZoo -------------
Cheshire The animal sleeps.
Cuddles The animal sleeps.
Leo The animal sleeps.
Lewis The animal sleeps.
Tigran The animal sleeps.
Tigru The animal sleeps.
Ellen The animal sleeps.
Elson The animal sleeps.
Deo The animal sleeps.
Dawn The animal sleeps.
Hank The animal sleeps.
Hustler The animal sleeps.
Rincon The animal sleeps.
Ruben The animal sleeps.
Ruben The animal sleeps.
Will The animal sleeps.
Wiz The animal sleeps.

Zoo Closed
"""