class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        matching_flights = []
        for flight in self.flights:
            if flight.source == source:
                matching_flights.append(flight)
        return matching_flights

    def search_by_destination(self, destination):
        matching_flights = []
        for flight in self.flights:
            if flight.destination == destination:
                matching_flights.append(flight)
        return matching_flights

# Create flight objects and add them to the table
flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

# User input and search
user_input = input("Enter a Flight ID, source city, or destination city: ")

matching_flights = []
flight = flight_table.search_by_flight_id(user_input)
if flight:
    matching_flights.append(flight)
else:
    matching_flights.extend(flight_table.search_by_source(user_input))
    matching_flights.extend(flight_table.search_by_destination(user_input))

# Print search results
if matching_flights:
    print("Matching flights:")
    for flight in matching_flights:
        print(f"Flight ID: {flight.flight_id}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
else:
    print("No matching flights found.")
