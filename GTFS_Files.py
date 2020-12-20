import csv

'''
stops_location = {}
with open("stops_all.csv") as csvstops:
    csv_reader_object = csv.reader(csvstops, delimiter = ";")
    for row in csv_reader_object:
        del row[4:8]
        del row[1]
        coordinates_stops = [row[3], row[4]]
        stops_location[row[1]] = coordinates_stops

print(stops_location['Solln'])


with open("routes.csv") as csvroutes:
    csv_reader_object1 = csv.reader(csvroutes, delimiter =",")
   # for row in csv_reader_object1:
       # print(row[2:5])
'''

stops_berlin = {}
with open("berlin_gtfs/BVG_VBB_bereichsscharf/stops.txt") as csvstops:
    csv_reader_object = csv.reader(csvstops, delimiter = ",")
    for row in csv_reader_object:
        del row[6:11]
        del row[3]
        del row[1]
        coordinates_stops = [row[2], row[3]]
        stops_berlin[row[0]] = coordinates_stops

print(stops_berlin["000008012713"])

#with open("berlin_gtfs/BVG_VBB_bereichsscharf/transfers.txt") as csvtransfers:
    #csv_reader_object1 = csv.reader(csvtransfers, delimiter = ",")
    #for row_transfers in csv_reader_object1:




