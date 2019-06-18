from Classes.Route import Route

class Airport:
    def __init__(self, name, code, lat, lon, routes = []):
        self.name = name
        self.code = code
        self.lat = lat
        self.lon = lon
        self.routes = routes

    # def addRoutes(self, routes):

    def __repr__(self):
        return "{}: {}".format(
            self.__class__.__name__,
            { attr: value for attr, value in self.__dict__.items() }
        )
