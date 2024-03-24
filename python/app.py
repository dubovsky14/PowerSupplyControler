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

#from PowerSupplyModule import PowerSupplyControlerWrapper
from PowerSupplyControler import PowerSupplyControler
from DataCSVReader import DataCSVReader
from other_functions import resample_data, keep_only_data_in_interval, get_start_and_end_of_interval
import time, datetime


time_string = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d_%H:%M:%S')
log_address = "logs/log_" + time_string + ".txt"
power_supply = PowerSupplyControler(log_address)
power_supply.start_measurement(100,1000)

#log_address = "logs/log_test.txt"
app = Bottle()

@app.route('/')
@view('index')
def show_index():
    # uwsgi does something very weird with memory access in multi-threading code, reading it from a text file is the only way to get the data
    csv_reader = DataCSVReader(log_address)
    data_times, data_voltages, data_currents = csv_reader.get_data()
    current_voltage = data_voltages[-1] if len(data_voltages) > 0 else 0
    time0 = data_times[0] if len(data_times) > 0 else 0

    n_resapled_points = 100
    if request.query.n_points:
        n_resapled_points = int(request.query.n_points)

    interval_start = None
    if request.query.interval_start:
        interval_start = time0 + 1000*int(request.query.interval_start)

    interval_end = None
    if request.query.interval_end:
        interval_end = time0 + 1000*int(request.query.interval_end)

    interval_start, interval_end = get_start_and_end_of_interval(data_times, interval_start, interval_end)

    data_times, data_voltages, data_currents = keep_only_data_in_interval(interval_start, interval_end, data_times, data_voltages, data_currents)


    Ah = csv_reader.calculate_Ah(data_currents, data_times)
    Ah = round(Ah, 3)

    data_times, data_voltages, data_currents = resample_data(n_resapled_points, data_times, data_voltages, data_currents)
    times_s = [int((x - time0)/1000) for x in data_times]
    context =   {
                    "measurement_start" : datetime.datetime.fromtimestamp(int(time0/1000)).strftime('%Y-%m-%d %H:%M:%S'),
                    "times" : times_s,
                    "voltages" : data_voltages,
                    "currents" : data_currents,
                    "current_voltage": round(current_voltage,2),
                    "Ah" : Ah,
                    "time_start" : int((interval_start - time0)/1000),
                    "time_end" : int((interval_end - time0)/1000),
                    "sampling_n_points" : n_resapled_points,
                    "log_address" : log_address,
                }
    return context

@app.route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root=main_dir + '/js/')

@app.route('/logs/<filename>')
def serve_plugin_txt_file(filename):
    with open("logs/" + filename ) as f:
        stat_art = f.read()
    return stat_art