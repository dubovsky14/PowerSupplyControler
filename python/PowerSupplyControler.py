import time
import threading

class PowerSupplyControler:
    def __init__(self, output_log_file : str, a0_to_voltage_const : float = 7.60, a1_to_currenct_const : float = 4.22):
        self.log_file = open(output_log_file, "w")
        self.a0_to_voltage_const  = a0_to_voltage_const
        self.a1_to_currenct_const = a1_to_currenct_const

        self.sampling_interval_ms = 100
        self.recorded_interval_ms = 1000

        self.running_on_raspberry = False
        try:
            import board
            import busio
            import adafruit_ads1x15.ads1115 as ADS
            from adafruit_ads1x15.analog_in import AnalogIn

            i2c = busio.I2C(board.SCL, board.SDA)
            ads = ADS.ADS1115(i2c)
            self.channel_voltage = AnalogIn(ads, ADS.P0)
            self.channel_current = AnalogIn(ads, ADS.P1)
            self.running_on_raspberry = True
        except Exception as e:
            print("Failed to initialize measurement on Raspberry Pi. Maybe you are running on a different platform?")
            print(e)

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
                self.log_file.write(f"{int(current_time*1000)}, {voltage/n_values}, {current/n_values}\n")
                self.log_file.flush()
                n_values = 0
                voltage = 0.
                current = 0.
                next_record_time += self.recorded_interval_ms / 1000

    def measure(self) -> tuple[float,float]:
        if self.running_on_raspberry:
            a0 = self.channel_voltage.voltage
            a1 = self.channel_current.voltage
            return a0*self.a0_to_voltage_const, a1*self.a1_to_currenct_const
        else:
            return 0., 0.

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