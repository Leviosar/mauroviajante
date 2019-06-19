from Classes.Flight import Flight

'''
Tabela de preços:

Valor padrão:
	- Passagem: 0.5 R$/km
Acréscimos:
	- Número de passageiros: + 0.1%/passageiro
'''

class CharterFlight(Flight):
	def __init__(self, origin, destiny, flightNumber, flightCapacity, flightDistance, passengers = []):
		self.flightCapacity = flightCapacity
		self.flightDistance = flightDistance
		self.passengers = passengers

		super().__init__(origin, destiny, flightNumber)

	def bookPassage(self, person):
		if self.fullyBooked():
			print('Voo lotado, não será possível agendar.')
		else:
			self.buySit(person)

	def buySit(self, person):
		price = self.calculateFinalPrice()

		option = input('O preço final de sua passagem é de R${}. Gostaria de confirmar (s/n)? '.format(price))

		if option.lower() == 's':
			self.passengers.append(person)
			print('Passagem comprada com sucesso.')

	def calculateFinalPrice(self):
		price = 0.5 * self.flightDistance

		price += price * (0.001 * len(self.passengers))

		return price

	def fullyBooked(self):
		return len(self.passengers) >= self.flightCapacity

	def __repr__(self):
		return f'Tipo de voo: Voo Fretado ({self.__class__.__name__})\nOrigem: {self.origin}\nDestino: {self.destiny}\nNúmero do Voo: {self.flightNumber}\nLotação Máxima: {self.flightCapacity}\nAssentos Ocupados: {len(self.passengers)}'