from travel_agent import Travel_agent


def main():
    sadat_tours = Travel_agent('GO with SADAT')
    """ argentina_trip_info = sadat_tours.make_trip_one_city_one_way(
        'DAC', 'PRA', '05/12/2022')
    print('Air Craft: ', argentina_trip_info.air_craft)
    print('Ticket Fare: ', argentina_trip_info.fare)
    print('Journey Date: ', argentina_trip_info.journey_date)
    print('\n\n')

    # two city
    trip_info_two = ['DAC', 'ANK', 'MUC']
    trip_journey_two = ['10/11/2022', '18/11/2022']
    turky_german_trip_info = sadat_tours.make_trip_two_city_one_way(
        trip_info_two, trip_journey_two)
    for trip in turky_german_trip_info:
        print('Air Craft: ', trip.air_craft)
        print('Ticket Fare: ', trip.fare)
        print('Journey Date: ', trip.journey_date, end='\n\n')

    print('\n')
    # multi city fixed route
    trip_info_multi = ['DAC', 'ANK', 'MUC', 'LTQ', 'VCE']
    trip_journey_milti = ['10/11/2022',
                          '18/11/2022', '28/11/2022', '08/12/2022']
    turky_german_france_italy_trip_info = sadat_tours.make_trip_multi_city_one_way_fixed_route(
        trip_info_multi, trip_journey_milti)
    for trip in turky_german_france_italy_trip_info:
        print('Air Craft: ', trip.air_craft)
        print('Ticket Fare: ', trip.fare)
        print('Journey Date: ', trip.journey_date, end='\n\n') """

    # trip_cities_flex_route = ['DAC', 'DXB', 'MUC', 'LTQ', 'VCE', 'MTL', 'NYC']
    trip_cities_flex_route = ['DUB', 'LHR', 'SYD', 'JFK', 'ORD', 'DAC']
    journey_dates = ['10/11/2022', '18/11/2022', '28/11/2022',
                     '08/12/2022', '18/12/2022', '28/12/2022', '1/1/2023']
    trips_info = sadat_tours.make_trip_multi_city_one_way_flexible_route(
        trip_cities_flex_route, journey_dates)

    for trip in trips_info[0]:
        print(trip)
        print('Air Craft: ', trip.air_craft)
        print('Ticket Fare: $', trip.fare)
        print('Journey Date: ', trip.journey_date, end='\n\n')
    print('Total Cost: $', round(trips_info[1]))


if __name__ == "__main__":
    main()
