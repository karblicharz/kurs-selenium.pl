class SearchHotelsData:

    def __init__(self, city, adult_travellers, child_travellers, hotel_1, price_1):
        self.city = city
        self.adult_travellers = adult_travellers
        self.child_travellers = child_travellers
        self.hotel_1 = hotel_1
        self.price_1 = price_1


class SearchFlightsData:

    def __init__(self, from_airport, to_airport):
        self.from_airport = from_airport
        self.to_airport = to_airport

