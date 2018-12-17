import csv
import time
import influxdb

csv_path = "<>insert path here!>\\CSV_Name.csv"
# influx config information
# information below should be filled in to match your information
influx = influxdb.InfluxDBClient(host='<host name>', 
                                 port=<port name>,
                                 database='DB name')

# opens the csv, skips the first two garbage lines, and appends to list
output = []
with open(csv_path, "r", encoding ="utf-16") as f:
	reader = csv.reader(f, skipinitialspace=True, delimiter=",")
	next(reader)
	next(reader)
	for row in reader:
		output.append(row)	

field_vals = {}
time_values = {}
main_dict = {}


# Get all field values into a dictionary
# loops through 24 times to reflect the 24 time entries
for r in range(25):
	list = []
	main_dict["measurement"] = "Test_02"
	main_dict["time"] = output[r][1]
	main_dict["fields"] = field_vals
	field_vals["msg_vals"] = int((output[r][2]))
	data = [main_dict]
	print(data)
	# gotta write 'em all'
	influx.write_points(data)
	time.sleep(1)
