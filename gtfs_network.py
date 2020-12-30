import csv
import matplotlib.pyplot as plt
import networkx as nx
from operator import itemgetter
from networkx.algorithms import community



stops_coordinates = {}
stops_name = {}

with open("berlin_gtfs/BVG_VBB_bereichsscharf/stops.txt") as csvstops:
    csv_reader_object = csv.reader(csvstops, delimiter = ",")
    for row in csv_reader_object:
        del row[6:11]
        del row[3]
        del row[1]
        coordinate_stops = [float(row[2]), float(row[3])]
        stops_coordinates[row[0]] = coordinate_stops
        stops_name[row[0]] = row[1]

print(stops_coordinates["000008012713"])
print(stops_name["000008012713"])

with open("berlin_gtfs/BVG_VBB_bereichsscharf/stops.txt") as nodecsv:
    nodereader = csv.reader(nodecsv, delimiter = ",")
    nodes = [n for n in nodereader][1:]

node_id = [n[0] for n in nodes]

edge_traveltime = {}
traveltime = []

with open("berlin_gtfs/BVG_VBB_bereichsscharf/transfers.txt") as csvtransfers:
    edgereader = csv.reader(csvtransfers, delimiter = ",")
    edges = [tuple(e) for e in edgereader][1:]


edge_ids = [e[0:2] for e in edges]


print(len(edge_ids))
print(edge_ids[0:3])

with open("berlin_gtfs/BVG_VBB_bereichsscharf/transfers.txt") as csvtransfers:
    edgereader = csv.reader(csvtransfers, delimiter = ",")
    for i in edgereader:
        traveltime.append(i[3])

del traveltime[0]

print(len(edge_ids))
print(len(traveltime))

edge_traveltime = dict(zip(edge_ids, traveltime))

print(len(edge_traveltime))



#print(traveltime)
'''
print(len(node_id))
print(len(edge_ids))
print(edge_ids[0])
#print(edge_ids[0])
'''

G = nx.Graph()
G.add_nodes_from(node_id)
G.add_edges_from(edge_ids)
print(nx.info(G))

nx.set_node_attributes(G, stops_name, 'stop_name')
nx.set_node_attributes(G, stops_coordinates, 'stop_location')

nx.set_edge_attributes(G, edge_traveltime, 'min. traveltime')

density = nx.density(G)
print("Network Density:", density)

def draw_network(G, edges, color='black', new_plot=True, title='Map of M', label=None):



#tryout_shortest_path = nx.shortest_path(G, source = '250000120002', target ='710009230001')
#print(tryout_shortest_path)



