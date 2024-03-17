#pragma once

#include <mutex>
#include <vector>
#include <string>
#include <memory>
#include <tuple>
#include <fstream>
#include <thread>


class PowerSupplyControler {
    public:
        PowerSupplyControler(const std::string &output_file);

        void start_measurement(int sampling_interval_ms, int recorded_interval_ms);

        void stop_measurement();

        /**
         * @brief Get the data from the power supply
         * returns: a tuple with the following elements:
         * - a vector with the time in ms
         * - a vector with the voltage in V
         * - a vector with the current in A
        */
        std::tuple<std::vector<int>, std::vector<float>, std::vector<float>> get_data();


    private:
        std::unique_ptr<std::ofstream> m_output_file = nullptr;
        std::mutex                      m_mutex;
        bool                            m_measuring = false;
        std::unique_ptr<std::thread>    m_measurement_thread = nullptr;
        std::vector<int>    m_time;
        std::vector<float>  m_voltage;
        std::vector<float>  m_current;

        void get_voltage_and_current(float *voltage, float *current);

};
