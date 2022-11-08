from travel_agent import Travel_agent


def main():
    sadat_tours = Travel_agent('GO with SADAT')
    argentina_trip_info = sadat_tours.make_trip_one_city_one_way(
        'DAC', 'PRA', '05/12/2022')
    print('Air Craft: ', argentina_trip_info[0])
    print('Ticket Cost: ', argentina_trip_info[1])


if __name__ == "__main__":
    main()
