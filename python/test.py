from sys import path
import time
import datetime


from PowerSupplyControler import PowerSupplyControler

time_string = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d_%H:%M:%S')
log_address = "logs/log_" + time_string + ".txt"

power_supply = PowerSupplyControler(log_address)
power_supply.start_measurement(100,1000)

time.sleep(240)
power_supply.stop_measurement()