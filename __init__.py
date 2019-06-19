from util import *

from Classes.Operator import Operator

operator = Operator()

while True:
    showGeneralMenu()
    generalOption = int(input())
    generalOption = checkGeneralOption(generalOption)

    if generalOption == REGISTER_FLIGHT:
        showFlightsMenu()
        flightOption = int(input())
        flightOption = checkFlightOption(flightOption)

        operator.registerFlight(flightOption)

    elif generalOption == CANCEL_FLIGHT:
        operator.showFlights()
        operator.cancelFlight()

    elif generalOption == NEW_BOOKING:
        operator.showFlights()

        number = int(input('Insira o número do voo no qual deseja fazer a reserva: '))

        operator.newBooking(number)
    
    elif generalOption == SHOW_FLIGHTS:
        operator.showFlights()
    
    else:
        break