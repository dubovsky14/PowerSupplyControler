from copy import deepcopy

def get_start_and_end_of_interval(times : list[int], limit_start : int, limit_end : int) -> tuple[int,int]:
    """
    Get the start and end of the interval.
    """
    if len(times) == 0:
        return 0, 0
    result_start = times[0]
    if limit_start != None:
        if not limit_start < times[0]:
            result_start = limit_start

    result_end = times[-1]
    if limit_end != None:
        if not limit_end > times[-1]:
            result_end = limit_end

    return result_start, result_end

def keep_only_data_in_interval(interval_start : int, interval_end : int, times : list[int], voltages : list[float], currents : list[float]) -> tuple[list,list,list]:
    """
    Keep only the data in the interval [interval_start, interval_end].
    """
    result_times = []
    result_currents = []
    result_voltages = []
    if len(times) != len(currents) or len(times) != len(voltages):
        raise ValueError("The lengths of the input lists must be equal.")
    if len(times) == 0:
        return result_times, result_voltages, result_currents

    if interval_start == None:
        interval_start = times[0]
    if interval_end == None:
        interval_end = times[-1]

    for index in range(len(times)):
        if times[index] >= interval_start and times[index] <= interval_end:
            result_times.append(times[index])
            result_currents.append(currents[index])
            result_voltages.append(voltages[index])
    return result_times, result_voltages, result_currents

def resample_data(n_points_resampled : int, times : list[int], voltages : list[float], currents : list[float]) -> tuple[list,list,list]:
    """
    Resample data to a new sample rate.
    """
    result_times = []
    result_currents = []
    result_voltages = []
    if len(times) != len(currents) or len(times) != len(voltages):
        raise ValueError("The lengths of the input lists must be equal.")
    if n_points_resampled > len(times):
        return deepcopy(times), deepcopy(currents), deepcopy(voltages)

    n_oldpoints_in_one_newpoint = len(times) / n_points_resampled
    time_average = 0
    current_average = 0
    voltage_average = 0
    time_interval = 0
    next_point = n_oldpoints_in_one_newpoint
    for index_old in range(1,len(times)):
        dt = times[index_old] - times[index_old-1]
        time_interval   += dt
        time_average    += times[index_old]*dt
        current_average += currents[index_old]*dt
        voltage_average += voltages[index_old]*dt
        if index_old >= next_point:
            result_times.append(time_average/time_interval)
            result_currents.append(current_average/time_interval)
            result_voltages.append(voltage_average/time_interval)
            time_average = 0
            current_average = 0
            voltage_average = 0
            time_interval = 0
            next_point += n_oldpoints_in_one_newpoint
    return result_times, result_voltages, result_currents
