from required_functions import get_all_airporft, find_haversine_distance


class All_Airports:
    def __init__(self) -> None:
        self.load_airports_data('./data/airports.csv')

    def load_airports_data(self, file_path):

        self.airports = get_all_airporft(file_path)
        # for airport in self.airports.items():
        #     print(airport)

    def distance_between_two_airports(self, start_airport_code, end_airport_code):
        origin_airport = self.airports[start_airport_code]
        destination_airport = self.airports[end_airport_code]
        distance = find_haversine_distance(
            origin_airport.lat, origin_airport.lon, destination_airport.lat, destination_airport.lon)
        return distance

    def get_ticket_price(self, start_airport_code, end_airport_code):
        distance = self.distance_between_two_airports(
            start_airport_code, end_airport_code)
        start_airport = self.airports[start_airport_code]
        fare = distance*1000*float(start_airport.usd_rate)
        return fare


# world_tour = All_Airports()
# print(world_tour.distance_between_two_airports('DAC', 'PRA'))
