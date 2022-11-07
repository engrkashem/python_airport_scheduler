
class Airport:
    def __init__(self, code, name, city, country, lat, long, usd_rate) -> None:
        self.code = code
        self.port_name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.long = long
        self.usd_rate = usd_rate

    def __repr__(self) -> str:
        return f'Airport {self.port_name} in {self.country}, Latitude: {self.lat}, Longitude: {self.long} and USD_Rate: {self.usd_rate}'
