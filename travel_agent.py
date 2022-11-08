from all_airports import All_Airports
from air_lines import Air_lines
from trip import Trip


class Travel_agent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None
        self.all_airports = All_Airports()
        self.air_lines = Air_lines()

    # select air craft from air_lines
    def make_trip_one_city_one_way(self, start_port_code, end_port_code, journey_date):
        fare = self.all_airports.get_ticket_price(
            start_port_code, end_port_code)
        distance = self.all_airports.distance_between_two_airports(
            start_port_code, end_port_code)
        air_craft = self.air_lines.get_air_craft_by_distance(distance)
        trip = Trip([start_port_code, end_port_code], air_craft,
                    fare, journey_date, [start_port_code, end_port_code])
        return trip

    def make_trip_one_city_round_way(self, start_port_code, end_port_code, journey_date):
        trip1 = self.make_trip_one_city_one_way(
            start_port_code, end_port_code, journey_date[0])
        trip2 = self.make_trip_one_city_one_way(
            start_port_code, end_port_code, journey_date[1])
        return [trip1, trip2]

    """ 
        trip_info: [city1,city2,city3]
        journey_date: [date1, date2]
     """

    def make_trip_two_city_one_way(self, trip_cities, journey_date):
        trip1 = self.make_trip_one_city_one_way(
            trip_cities[0], trip_cities[1], journey_date[0])
        trip2 = self.make_trip_one_city_one_way(
            trip_cities[1], trip_cities[2], journey_date[1])
        return [trip1, trip2]

    '''
        trip_info: [city1,city2,city3, city4, city5, ....]
        journey_date: [date1, date2, date3, date4, ....]
    '''

    def make_trip_multi_city_one_way_fixed_route(self, trip_cities, journey_date):
        trips = []
        for i in range(0, len(trip_cities)-1):
            trip = self.make_trip_one_city_one_way(
                trip_cities[i], trip_cities[i+1], journey_date[i])
            trips.append(trip)
        return trips

    '''
        trip_info: [city1,city2,city3, city4, city5, ....]
        journey_date: [date1, date2, date3, date4, ....]
    '''

    def make_trip_multi_city_one_way_flexible_route(self, trip_cities, journey_date):
        pass

    def __repr__(self) -> str:
        return f'Travel Agent: {self.name}'
