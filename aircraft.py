
class Aircraft:
    def __init__(self, manufacturer, code, typ, flight_range) -> None:
        self.manufacturer = manufacturer
        self.code = code
        self.typ = typ
        self.flight_range = flight_range

    def get_manufacturer_info(self):
        return self.manufacturer

    def __repr__(self) -> str:
        return f'Aircraft Produced by {self.manufacturer}, code: {self.code}, Type: {self.typ} and flight-range: {self.flight_range}'
