import math

stations = [[0, 0, 10],
            [20, 20, 5],
            [10, 0, 12]]

# Here I'm only gettin x and y as parameters, but I think the station list
# should also be passed, so we can avoid global variables
def get_link_station(x, y):
    possible_stations=[]
    # Iterate trough all the stations
    for station in stations:
        # Get distance using formula for distance between two points
        distance = math.sqrt(((x-station[0])**2)+((y-station[1])**2))
        if distance < station[2]:
            # If the reach is big enough add the station to the list
            # of aviable ones
            power = (station[2] - distance)**2
            possible_stations.append([station, power])
    # If empty no station can deliver power to the point
    if possible_stations == []:
        print(f"No link station within reach for point {x},{y}")
    else:
        # Get the station that can deliver the biggest output
        print(possible_stations)
        powers = [power[1] for power in possible_stations]
        best_power = max(powers)
        best_station = possible_stations[powers.index(best_power)]
        # We only have the max value of the power, we get the 
        print(f"Best link station for point {x},{y} is {best_station[0][0]},{best_station[0][1]} with power {best_power}")
    
get_link_station(0,0)
get_link_station(100,100)
get_link_station(15,10)
get_link_station(18,18)