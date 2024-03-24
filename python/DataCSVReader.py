from time import sleep
class DataCSVReader:
    def __init__(self, filename):
        self.filename = filename

    def _read_data(self) -> tuple:
        times = []
        voltages = []
        currents = []
        with open(self.filename, 'r') as file:
            for line in file:
                elements = line.split(',')
                times.append(int(elements[0]))
                voltages.append(float(elements[1]))
                currents.append(float(elements[2]))
        return times, voltages, currents

    def get_data(self):
        try:
            return self._read_data()
        except Exception as e:
            sleep(0.5)
            return self.get_data()

    def calculate_Ah(self, currents : list[float], times : list[int]) -> float:
        Ah = 0
        for i in range(1, len(currents)):
            Ah += currents[i] * (times[i] - times[i-1]) / 3600000
        return Ah