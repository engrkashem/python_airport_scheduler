
class Trip:
    def __init__(self, trip_cities, journey_date) -> None:
        self.trip_cities = trip_cities
        self.journey_date = journey_date
        self.air_craft = None
        self.trip_route = None
        self.cost = None

    def __repr__(self) -> str:
        return f'Trip Started from {self.trip_cities}, Air_Craft: {self.air_craft}, Route: {self.trip_route}, Cost: {self.cost}'
