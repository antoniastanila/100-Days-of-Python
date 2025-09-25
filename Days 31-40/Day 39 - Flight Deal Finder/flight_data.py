def find_cheapest_flight(data):
    if not data or len(data) == 0:
        print("No flight data")
        return None

    cheapest_flight = data[0]
    smallest_price = float(data[0]["price"]["total"])
    for index in range(1, len(data)):
        curent = float(data[index]["price"]["total"])
        if curent < smallest_price:
            cheapest_flight = data[index]
            smallest_price = curent
    return cheapest_flight
