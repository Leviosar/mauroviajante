from util import *

from Classes.Person import Person
from Classes.Passenger import Passenger

from Classes.CommercialFlight import CommercialFlight
from Classes.CharterFlight import CharterFlight
from Classes.TransportFlight import TransportFlight

class Operator:

	def __init__(self, flights = [], passengers = []):
		self.flights = flights
		self.passengers = passengers

	def registerFlight(self, flightType):
		if self.maxiumFlightCapacity():
			print('Capacidade máxima de voos atingida, não será possível cadastrar um novo voo')
		else:
			origin = input('Insira a origem do seu voo: ')
			destiny = input('Insira o destino do seu voo: ')
			flightNumber = int(input('Insira o número do seu voo: '))

			if self.flightNumberResgitered(flightNumber):
				print('Número de voo já cadastrado')
				flightNumber = self.getUnregisteredFlightNumber()

			if flightType == COMMERCIAL_FLIGHT:
				flightCapacity = int(input('Insira a capacidade máxima do seu voo (Quantidade de pessoas): '))

				self.registerCommercialFlight(origin, destiny, flightNumber, flightCapacity)

			elif flightType == CHARTER_FLIGHT:
				flightCapacity = int(input('Insira a capacidade máxima do seu voo (Quantidade de pessoas): '))
				flightDistance = float(input('Insira a distância total do seu voo (km): '))

				self.registerCharterFlight(origin, destiny, flightNumber, flightCapacity, flightDistance)

			elif flightType == TRANSPORT_FLIGHT:
				flightWeightCapacity = int(input('Insira a capacidade máxima do seu voo (Peso máximo em kg): '))

				self.registerTransportFlight(origin, destiny, flightNumber, flightWeightCapacity)

	def cancelFlight(self):
		if empty(self.flights):
			print('Ainda não há voos cadastrados.')
			return

		flightNumber = int(input('Insira o número do voo que você deseja cancelar: '))
		flightNumber = self.checkRegisteredFlight(flightNumber)

		self.deleteFlight(flightNumber)
		print('Voo cancelado com sucesso.')

	def newBooking(self, flightNumber):
		flightNumber = self.checkRegisteredFlight(flightNumber)
		flight = self.getFlightByNumber(flightNumber)

		if isinstance(flight, (CommercialFlight, CharterFlight)):
			name = input('Insira o nome do passageiro: ')
			cpf = input('Insira o CPF do passageiro: ')
			person = Person(name, cpf)

			flight.bookPassage(person)

			passenger = Passenger(person, flight)

			self.passengers.append(passenger)
		
		elif isinstance(flight, TransportFlight):
			weight = float(input('Digite o peso da sua carga: '))

			flight.bookPassage(weight)

	def registerCommercialFlight(self, origin, destiny, flightNumber, flightCapacity):
		commercialFlight = CommercialFlight(origin, destiny, flightNumber, flightCapacity)
		self.flights.append(commercialFlight)

		print('\nNovo voo comercial cadastrado com sucesso.\n')

	def registerCharterFlight(self, origin, destiny, flightNumber, flightCapacity, flightDistance):
		charterFlight = CharterFlight(origin, destiny, flightNumber, flightCapacity, flightDistance)
		self.flights.append(charterFlight)

		print('\nNovo voo fretado cadastrado com sucesso.\n')

	def registerTransportFlight(self, origin, destiny, flightNumber, flightWeightCapacity):
		transportFlight = TransportFlight(origin, destiny, flightNumber, flightWeightCapacity)
		self.flights.append(transportFlight)

		print('\nNovo voo de transporte cadastrado com sucesso.\n')

	def deleteFlight(self, flightNumber):
		flight = self.getFlightByNumber(flightNumber)
		self.flights.remove(flight)

	def flightNumberResgitered(self, flightNumber):
		return self.getFlightByNumber(flightNumber) is not None

	def getFlightByNumber(self, flightNumber):
		for flight in self.flights:
			if flight.flightNumber == flightNumber:
				return flight

		return None

	def checkRegisteredFlight(self, flightNumber):
		if self.getFlightByNumber(flightNumber) is None:
			print('Voo não encontrado, digite um número de voo válido')
			flightNumber = self.getRegisteredFlightNumber()

		return flightNumber

	def getUnregisteredFlightNumber(self):
		flightNumber = int(input('Insira um número de voo válido, valores já cadastrados não serão aceitos: '))

		if self.getFlightByNumber(flightNumber) is not None:
			flightNumber = self.getUnregisteredFlightNumber()

		return flightNumber

	def getRegisteredFlightNumber(self):
		flightNumber = int(input('Insira um número de voo que exista: '))

		if self.getFlightByNumber(flightNumber) is None:
			flightNumber = self.getRegisteredFlightNumber()

		return flightNumber

	def showFlights(self):
		if empty(self.flights):
			print('Sem voos cadastrados até o momento.')
		else:
			print('\nVoos disponíveis:\n')
			for flight in self.flights:
				print(flight)
				print()

	def maxiumFlightCapacity(self):
		return len(self.flights) >= 3