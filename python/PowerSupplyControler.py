import time
import threading

class PowerSupplyControler:
    def __init__(self, output_log_file : str, a0_to_voltage_const : float = 1, a1_to_currenct_const : float = 1.):
        self.log_file = open(output_log_file, "w")
        self.a0_to_voltage_const  = a0_to_voltage_const
        self.a1_to_currenct_const = a1_to_currenct_const

        self.sampling_interval_ms = 100
        self.recorded_interval_ms = 1000

    def _measure_and_save_to_file(self):
        n_values = 0
        voltage = 0.
        current = 0.
        next_record_time = time.time() + self.recorded_interval_ms / 1000
        while not self.stop_flag:
            time.sleep(self.sampling_interval_ms / 1000)
            voltage_now, current_now = self.measure()
            current_time = time.time()
            n_values += 1
            voltage += voltage_now
            current += current_now
            if current_time > next_record_time:
                self.log_file.write(f"{current_time}, {voltage/n_values}, {current/n_values}\n")
                self.log_file.flush()
                n_values = 0
                voltage = 0.
                current = 0.
                next_record_time += self.recorded_interval_ms / 1000

    def measure(self) -> tuple[float,float]:
        a0 = 0
        a1 = 0
        return a0*self.a0_to_voltage_const, a1*self.a1_to_currenct_const

    def start_measurement(self, sampling_interval_ms : int = None, recorded_interval_ms : int = None) -> None:
        if sampling_interval_ms is not None:
            self.sampling_interval_s = sampling_interval_ms
        if recorded_interval_ms is not None:
            self.recorded_interval_s = recorded_interval_ms

        self.stop_flag = False
        self.thread = threading.Thread(target=self._measure_and_save_to_file)
        self.thread.start()

    def stop_measurement(self) -> None:
        self.stop_flag = True
        self.thread.join()