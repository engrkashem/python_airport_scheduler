from csv import reader
from aircraft import Aircraft
from random import choice


class Air_lines:
    def __init__(self) -> None:
        self.air_crafts = None
        self.load_air_crafts('./data/aircrafts.csv')

    def load_air_crafts(self, csv_file):
        air_crafts = {}
        with open(csv_file, 'r') as file:
            lines = reader(file)
            next(lines)
            for line in lines:
                air_crafts[line[0]] = Aircraft(
                    line[3], line[0], line[1], line[4])
        file.close()
        self.air_crafts = air_crafts

        # for craft in self.air_crafts.items():
        #     print(craft)

    def get_air_craft(self, air_craft_code):
        return self.air_crafts.get(air_craft_code)

    def get_air_craft_by_distance(self, distance):
        air_crafts = []
        for air_craft in self.air_crafts.values():
            if air_craft.flight_range > distance/2:
                air_crafts.append(air_craft)
        return choice(air_crafts)


# Air_lines()
