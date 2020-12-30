import csv
import networkx as nx


class Station:

    def __init__(self, stop_id, stop_code,stop_name,
                 stop_desc,stop_lat,stop_lon,location_type,parent_station,
                 wheelchair_boarding,platform_code,zone_id):
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.stop_desc = stop_desc
        self.stop_lat = float(stop_lat)
        self.stop_lon = float(stop_lon)
        self.location_type = location_type
        self.parent_station = parent_station
        self.wheelchair_boarding = wheelchair_boarding
        self.platform_code = platform_code
        self.zone_id = zone_id


    def __str__(self):
        if self.parent_station == '':
            string = 'Name: ' + self.stop_name + '\nStop ID: ' + self.stop_id + \
                     '\nCoordinates: ' + '(' + str(self.stop_lat) + ',' + str(self.stop_lon) + ')'
        else:
            string = 'Name: ' + self.stop_name + '\nParent Station: ' + self.parent_station + \
                     '\nCoordinates: ' + '(' + str(self.stop_lat) + ',' + str(self.stop_lon) + ')'
        return string

    def get_name(self):
        return self.stop_name

    def get_id(self):
        return self.stop_id

    def get_parent_station(self):
        return self.parent_station

    def get_coordinates(self):
        return (self.stop_lon, self.stop_lat)



def create_stations(filename ='stops.txt'):

    with open('stops.txt') as stops:
        station_info = csv.reader(stops)
        next(station_info)
        stations = []

        for row in station_info:
            (stop_id, stop_code, stop_name,
             stop_desc, stop_lat, stop_lon, location_type, parent_station,
             wheelchair_boarding, platform_code, zone_id) = tuple(row)

            stations.append(Station(stop_id, stop_code, stop_name,
                                    stop_desc, stop_lat, stop_lon, location_type, parent_station,
                                    wheelchair_boarding, platform_code, zone_id))

    return stations


create_stations('stops.txt')

