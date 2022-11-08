
class Trip:
    def __init__(self, trip_cities, air_craft, fare, journey_date, route='') -> None:
        self.trip_cities = trip_cities
        self.air_craft = air_craft
        self.fare = fare
        self.journey_date = journey_date
        self.trip_route = route

    def __repr__(self) -> str:
        return f'Trip Started, Route: {self.trip_route}, Cost: {self.fare}'
