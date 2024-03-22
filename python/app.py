# run as:
# uwsgi --http-socket :9090 --wsgi-file run_localhost.py --master
# access the gui in browser at address: localhost:9090

from bottle import Bottle, view, request, static_file, abort, route

import os
from sys import path

this_file_path = os.path.abspath(__file__)
main_dir = os.path.dirname(this_file_path)
main_dir = os.path.dirname(main_dir)
path.append(main_dir + "/bin/")

from PowerSupplyModule import PowerSupplyControlerWrapper
from DataCSVReader import DataCSVReader
import time, datetime

time_string = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d_%H:%M:%S')
log_address = "logs/log_" + time_string + ".txt"

power_supply = PowerSupplyControlerWrapper(log_address)
power_supply.start_measurement(100,1000)

app = Bottle()

@app.route('/')
@view('index')
def show_index():
    # uwsgi does something very weird with memory access in multi-threading code, reading it from a text file is the only way to get the data
    csv_reader = DataCSVReader(log_address)
    data_times, data_voltages, data_currents = csv_reader.get_data()

    print("data_times")
    for i in range(len(data_times)):
        print(data_times[i], data_voltages[i], data_currents[i])
    time0 = data_times[0] if len(data_times) > 0 else 0
    times_s = [int((x - time0)/1000) for x in data_times]
    Ah = csv_reader.calculate_Ah(data_currents, data_times)
    print("Time0: ", time0)
    context =   {
                    "measurement_start" : datetime.datetime.fromtimestamp(int(time0/1000)).strftime('%Y-%m-%d %H:%M:%S'),
                    "times" : times_s,
                    "voltages" : data_voltages,
                    "currents" : data_currents,
                    "Ah" : Ah
                }
    return context

@app.route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root=main_dir + '/js/')