
class Airport:
    def __init__(self, name, country, lat, long, fare) -> None:
        self.port_name = name
        self.country = country
        self.lat = lat
        self.long = long
        self.fare = fare

    def __repr__(self) -> str:
        return f'Airport {self.port_name} in {self.country}, Latitude: {self.lat}, Longitude: {self.long} and fare: {self.fare}'
