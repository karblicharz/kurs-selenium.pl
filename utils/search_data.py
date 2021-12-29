class SearchHotelsData:

    def __init__(self, city, check_in, check_out, adult_travellers, child_travellers, hotel_1, price_1):
        self.check_in = check_in
        self.check_out = check_out
        self.city = city
        self.adult_travellers = adult_travellers
        self.child_travellers = child_travellers
        self.hotel_1 = hotel_1
        self.price_1 = price_1


class SearchFlightsData:

    def __init__(self, from_airport, to_airport, departure_date, arrival_date):
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.departure = departure_date
        self.arrival = arrival_date
