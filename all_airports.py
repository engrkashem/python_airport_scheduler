from csv import reader
from airport import Airport


class All_Airports:
    def __init__(self) -> None:
        self.load_airports_data('./data/airports.csv')

    def load_airports_data(self, file_path):
        airports = {}
        with open(file_path, 'r', encoding='utf8') as file:
            lines = reader(file)
            for line in lines:
                airports[line[4]] = Airport(
                    line[0], line[1], line[2], line[3], line[6], line[7], 0)
            file.close()
        self.airports = airports
        for airport in self.airports.items():
            print(airport)


All_Airports()
