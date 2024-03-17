#include "../headers/PowerSupplyControler.h"

#include <iostream>

using namespace std;

PowerSupplyControler::PowerSupplyControler(const string &output_file) {
    m_output_file = make_unique<ofstream>(output_file);
    const int reserved_size = 24*3600; // 24 hours of data
    m_time.reserve(reserved_size);
    m_voltage.reserve(reserved_size);
    m_current.reserve(reserved_size);
};

PowerSupplyControler::~PowerSupplyControler() {
    stop_measurement();
    m_output_file->close();
};

void PowerSupplyControler::start_measurement(int sampling_interval_ms, int recorded_interval_ms) {
    if (m_measurement_thread != nullptr) {
        return;
    }

    auto measurement_loop = [this, sampling_interval_ms, recorded_interval_ms]() {
        int n_values = 0;
        double voltage = 0.0;
        double current = 0.0;
        m_measuring = true;
        long long int end_of_next_interval = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count() + recorded_interval_ms;
        while (m_measuring) {
            this_thread::sleep_for(chrono::milliseconds(sampling_interval_ms));

            float current_voltage, current_current;
            get_voltage_and_current(&current_voltage, &current_current);

            voltage += current_voltage;
            current += current_current;
            n_values++;

            const long long int current_time = chrono::duration_cast<chrono::milliseconds>(chrono::system_clock::now().time_since_epoch()).count();
            if (current_time > end_of_next_interval) {
                end_of_next_interval += recorded_interval_ms;
                if (n_values == 0) {
                    continue;
                }
                scoped_lock lock(m_mutex);
                m_time.push_back(current_time);
                m_voltage.push_back(voltage / n_values);
                m_current.push_back(current / n_values);
                *m_output_file << current_time << ", " << voltage / n_values << ", " << current / n_values << endl;
                voltage = 0.0;
                current = 0.0;
                n_values = 0;
            }
        }
    };

    m_measurement_thread = make_unique<thread>(measurement_loop);
};

void PowerSupplyControler::stop_measurement() {
    m_measuring = false;
    if (m_measurement_thread != nullptr) {
        m_measurement_thread->join();
        m_measurement_thread = nullptr;
    }
};

tuple<vector<long long int>, vector<float>, vector<float>> PowerSupplyControler::get_data() {
    scoped_lock lock(m_mutex);
    return make_tuple(m_time, m_voltage, m_current);
};

void PowerSupplyControler::get_voltage_and_current(float *voltage, float *current)    {
    *voltage = 0.0; // TODO: add reasonable values here
    *current = 0.0; // TODO: add reasonable values here
};