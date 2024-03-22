from sys import path

path.append("bin/")

from PowerSupplyModule import PowerSupplyControlerWrapper
from time import sleep

ps = PowerSupplyControlerWrapper("log.txt")
ps.start_measurement(100,1000)

sleep(5)
ps.stop_measurement()
ps.start_measurement(100,1000)
sleep(5)

ps.freeze_data()
times = ps.get_times()
voltages = ps.get_voltages()
currents = ps.get_currents()

for i in range(len(times)):
    print(times[i], voltages[i], currents[i])
sleep(5)
print("10 seconds later")
ps.freeze_data()
times = ps.get_times()
voltages = ps.get_voltages()
currents = ps.get_currents()

for i in range(len(times)):
    print(times[i], voltages[i], currents[i])