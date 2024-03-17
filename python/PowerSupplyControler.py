
import random

class PowerSupplyControler:
    def __init__(self, output_log_file : str):
        log_file = open(output_log_file, "w")

        # long term memory
        self._long_term_time = []
        self._long_term_voltage = []
        self._long_term_current = []

        # short term memory
        self._short_term_time = []
        self._short_term_voltage = []
        self._short_term_current = []
        self._short_term_start_time = None

    def _get_voltage_and_current(self) -> tuple[float,float]:
        # mock
        return (random.random()*10, random.random()*10)