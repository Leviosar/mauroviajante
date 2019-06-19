REGISTER_FLIGHT = 1
CANCEL_FLIGHT = 2
NEW_BOOKING = 3
SHOW_FLIGHTS = 4

COMMERCIAL_FLIGHT = 1
CHARTER_FLIGHT = 2
TRANSPORT_FLIGHT = 3

FIRST_CLASS = 1
ECONOMIC_CLASS = 2

NORMAL_MEAL = 1
GLUTEN_FREE = 2
VEGETARIAN = 3
KID_PORTION = 4

def empty(obj):
	if obj:
		return False

	return True


def showGeneralMenu():
	print('+====================================+')
	print('+ 1 - Cadastro de novo voo           +')
	print('+ 2 - Cancelamento de voo            +')
	print('+ 3 - Nova reserva                   +')
	print('+ 4 - Mostrar voos disponíveis       +')
	print('+ 5 - Sair                           +')
	print('+====================================+')

def showFlightsMenu():
	print('+====================================+')
	print('+ 1 - Voo Comercial                  +')
	print('+ 2 - Voo Fretado                    +')
	print('+ 3 - Voo de Transporte              +')
	print('+====================================+')

def showPassageMenu():
	print('+====================================+')
	print('+ 1 - Primeira Classe                +')
	print('+ 2 - Classe Econômica               +')
	print('+====================================+')

def showFoodMenu():
	print('+====================================+')
	print('+ 1 - Refeição normal                +')
	print('+ 2 - Sem glúten                     +')
	print('+ 3 - Vegetariana                    +')
	print('+ 4 - Porção infantil                +')
	print('+====================================+')

def validGeneralOption(generalOption):
	return 1 <= generalOption <= 5

def validFlightOption(flightOption):
	return 1 <= flightOption <= 3

def validPassageOption(passageOption):
	return 1 <= passageOption <= 2

def validFoodOption(foodOption):
	return 1 <= foodOption <= 4

def checkGeneralOption(generalOption):
	while not validGeneralOption(generalOption):
		print('Opção inválida, tente novamente')
		showGeneralMenu()
		generalOption = int(input())

	return generalOption

def checkFlightOption(flightOption):
	while not validFlightOption(flightOption):
		print('Opção de voo inválida, tente novamente')
		showFlightsMenu()
		flightOption = int(input())

	return flightOption

def checkPassageOption(passageOption):
	while not validPassageOption(passageOption):
		print('Opção de passagem inválida, tente novamente')
		showPassageMenu()
		passageOption = int(input())

	return passageOption

def checkFoodOption(foodOption):
	while not validFoodOption(foodOption):
		print('Opção de refeição inválida, tente novamente')
		showFoodMenu()
		foodOption = int(input())

	return foodOption