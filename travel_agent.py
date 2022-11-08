from all_airports import All_Airports
from air_lines import Air_lines


class Travel_agent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None
        self.all_airports = All_Airports()
        self.air_lines = Air_lines()

    # select air craft fron air_lines
    def make_trip_one_city_one_way(self, start_port_code, end_port_code, journey_date):
        price = self.all_airports.get_ticket_price(
            start_port_code, end_port_code)
        distance = self.all_airports.distance_between_two_airports(
            start_port_code, end_port_code)
        air_craft = self.air_lines.get_air_craft_by_distance(distance)
        # print('distance: ', distance)
        return [air_craft, price]

    def make_trip_multi_city_one_way(self):
        pass

    def make_trip_one_city_round_way(self):
        pass

    def make_trip_multi_city_round_way(self):
        pass

    def __repr__(self) -> str:
        return f'Travel Agent: {self.name}'
