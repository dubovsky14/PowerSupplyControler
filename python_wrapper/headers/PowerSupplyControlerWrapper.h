#pragma once

#include "../../headers/PowerSupplyControler.h"

#include <memory>
#include <tuple>
#include <vector>


class PowerSupplyControlerWrapper {
    public:
        PowerSupplyControlerWrapper(const std::string &output_file) {
            m_power_supply_controler = std::make_shared<PowerSupplyControler>(output_file);
        };

        ~PowerSupplyControlerWrapper() = default;

        void start_measurement(int sampling_interval_ms, int recorded_interval_ms)   {
            m_power_supply_controler->start_measurement(sampling_interval_ms, recorded_interval_ms);
        };

        void stop_measurement()  {
            m_power_supply_controler->stop_measurement();
        };

        std::tuple<std::vector<int>, std::vector<float>, std::vector<float>> get_data() {
            return m_power_supply_controler->get_data();
        };

        void freeze_data() {
            m_frozen_data = m_power_supply_controler->get_data();
        };

        std::vector<int> get_times() {
            return std::get<0>(m_frozen_data);
        };

        std::vector<float> get_voltages() {
            return std::get<1>(m_frozen_data);
        };

        std::vector<float> get_currents() {
            return std::get<2>(m_frozen_data);
        };

    private:
        std::shared_ptr<PowerSupplyControler> m_power_supply_controler = nullptr;
        std::tuple<std::vector<int>, std::vector<float>, std::vector<float>> m_frozen_data;

};
