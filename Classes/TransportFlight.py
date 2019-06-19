from Classes.Flight import Flight

'''
Tabela de preços:

Valor padrão:
	- Valor total: R$50.000
'''

class TransportFlight(Flight):
	def __init__(self, origin, destiny, flightNumber, flightWeightCapacity):
		self.flightWeightCapacity = flightWeightCapacity
		self.flightPrice = 50000
		self.totalWeight = 0

		super().__init__(origin, destiny, flightNumber)

	def bookPassage(self, weight):
		if self.exceedsMaxCapacity(weight):
			print('Sua carga ultrapassará o limite de carga do avião.')
			print('Espaço disponível: {}'.format(self.flightWeightCapacity - self.totalWeight))
		else:
			self.buySpace(weight)

	def buySpace(self, weight):
		price = self.calculateTotalPrice(weight)

		option = input('\nO preço final de sua passagem é de R${:.2f}. Gostaria de confirmar (s/n)? '.format(price))

		if option.lower() == 's':
			self.totalWeight += weight
			print('Passagem comprada com sucesso.')

	def calculateTotalPrice(self, weight):
		return weight/self.flightWeightCapacity * self.flightPrice

	def exceedsMaxCapacity(self, weight):
		return self.totalWeight + weight > self.flightWeightCapacity

	def __repr__(self):
		return f'Tipo de voo: Voo de Transporte ({self.__class__.__name__})\nOrigem: {self.origin}\nDestino: {self.destiny}\nNúmero: {self.flightNumber}\nCapacidade Máxima (kg): {self.flightWeightCapacity}\nCapacidade Ocupada (kg): {self.totalWeight}'