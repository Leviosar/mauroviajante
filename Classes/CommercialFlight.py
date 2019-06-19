from util import *

from Classes.Flight import Flight

'''
Tabela de preços:

Valores padrão:
	- Primeira classe: R$2.500
	- Classe econômica: R$1.000
Acréscimos:
	- Sem glúten: +R$10
	- Vegetariana: +R$15
	- Sem glúten: +R$5
'''

class CommercialFlight(Flight):
	def __init__(self, origin, destiny, flightNumber, flightCapacity, passengers = []):
		self.flightCapacity = flightCapacity
		self.passengers = passengers

		self.firstClassSits = int(flightCapacity * 0.2)
		self.economicClassSits = int(flightCapacity * 0.8)

		self.sitPrice = {
			FIRST_CLASS: 2500,
			ECONOMIC_CLASS: 1000
		}

		self.foodPrice = {
			NORMAL_MEAL: 0,
			GLUTEN_FREE: 10,
			VEGETARIAN: 15,
			KID_PORTION: 5
		}

		super().__init__(origin, destiny, flightNumber)

	def bookPassage(self, person):
		if self.fullyBooked():
			print('Voo lotado, não será possível agendar.')
		else:
			showPassageMenu()
			passageOption = int(input())
			passageOption = checkPassageOption(passageOption)

			if passageOption == FIRST_CLASS:
				self.checkFirstClass(person)

			elif passageOption == ECONOMIC_CLASS:
				self.checkEconomicClass(person)


	def checkFirstClass(self, person):
		if self.firstClassFullyBooked():
			self.offerEconomicClass()
		else:
			self.buySit(person, FIRST_CLASS)

	def checkEconomicClass(self, person):
		if self.economicClassFullyBooked():
			self.offerFirstClass()
		else:
			self.buySit(person, ECONOMIC_CLASS)



	def offerFirstClass(self, person):
		print('As passagens da classe econômica estão todas compradas, gostaria de comprar da primeira classe (s/n)?')
		option = input()

		if option.lower() == 's':
			self.buySit(person, FIRST_CLASS)

	def offerEconomicClass(self, person):
		print('As passagens da primeira classe estão todas compradas, gostaria de comprar da classe econômica (s/n)?')
		option = input()

		if option.lower() == 's':
			self.buySit(person, ECONOMIC_CLASS)

	def buySit(self, person, sitType):
		flightTime = input('Digite o horário do voo (hh:mm): ')
		flightHour = int(flightTime.split(':')[0])

		print('Escolha a opção de refeição: ')
		showFoodMenu()
		foodOption = int(input())
		foodOption = checkFoodOption(foodOption)

		finalPrice = self.calculateFinalPrice(sitType, flightHour, foodOption)

		option = input('O preço final de sua passagem é de R${}. Gostaria de confirmar (s/n)? '.format(finalPrice))

		if option.lower() == 's':
			if sitType == FIRST_CLASS:
				self.buyFirstClass(person)
			elif sitType == ECONOMIC_CLASS:
				self.buyEconomicClass(person)

	def buyFirstClass(self, person):
		self.firstClassSits -= 1
		self.passengers.append(person)
		print('Passagem comprada com sucesso.')

	def buyEconomicClass(self, person):
		self.economicClassSits -= 1
		self.passengers.append(person)
		print('Passagem comprada com sucesso.')

	def calculateFinalPrice(self, sitType, flightHour, foodOption):
		price = self.sitPrice[sitType]

		if self.flightCapacity > 100:
			price *= 0.85

		if flightHour >= 22 or flightHour <= 5:
			price *= 0.75

		price += self.foodPrice[foodOption]

		return price

	def firstClassFullyBooked(self):
		return self.firstClassSits <= 0

	def economicClassFullyBooked(self):
		return self.economicClassSits <= 0

	def fullyBooked(self):
		return len(self.passengers) >= self.flightCapacity

	def __repr__(self):		 
		return f'Tipo de voo: Voo Comercial ({self.__class__.__name__})\nOrigem: {self.origin}\nDestino: {self.destiny}\nNúmero do Voo: {self.flightNumber}\nLotação Máxima: {self.flightCapacity}\nAssentos Ocupados: {len(self.passengers)}'
