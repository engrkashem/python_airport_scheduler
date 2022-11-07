from csv import reader
from airport import Airport


def get_all_airporft(file_path):
    airports = {}
    currency_rates = {}
    country_currency = {}

    # Get dictionary of {currency_code : currency_rates}
    with open('./data/currency_rates.csv', 'r') as file:
        lines = reader(file)
        for line in lines:
            currency_rates[line[1]] = line[2]
    file.close()

    # get dictionary of {couyntry_name:currency_code}
    with open('./data/currencies.csv', 'r') as file:
        lines = reader(file)
        header = next(lines)
        for line in lines:
            country_currency[line[0]] = line[1]
    file.close()

    # Create Airport(country_code, name, city, country, lat, longitude,rate)etc.
    with open(file_path, 'r', encoding='utf8') as file:
        lines = reader(file)
        try:
            for line in lines:
                currency_code = country_currency.get(line[3])
                rate = currency_rates.get(currency_code)
                airports[line[4]] = Airport(
                    line[4], line[1], line[2], line[3], line[6], line[7], rate)
        except KeyError as e:
            print(e)
            # Alternate way to eleminate keyError
            """ for line in lines:
                currency_code = country_currency.get(line[3])
                rate = currency_rates.get(currency_code)
                airports[line[4]] = Airport(
                    line[0], line[1], line[2], line[3], line[6], line[7], rate) """
        file.close()

    return airports
