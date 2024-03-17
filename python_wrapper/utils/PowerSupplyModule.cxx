#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <string>

#include "../headers/PowerSupplyControlerWrapper.h"


BOOST_PYTHON_MODULE(PowerSupplyModule) {
    // An established convention for using boost.python.
    using namespace boost::python;

    boost::python::class_<std::vector<double>>("DoubleVector")
    .def(boost::python::vector_indexing_suite<std::vector<double>>());

    boost::python::class_<std::vector<float>>("FloatVector")
    .def(boost::python::vector_indexing_suite<std::vector<float>>());

    boost::python::class_<std::vector<int>>("IntVector")
    .def(boost::python::vector_indexing_suite<std::vector<int>>());


    /**
     * @brief Python wrapper around FastFramesExecutor
     *
     */
    class_<PowerSupplyControlerWrapper>("PowerSupplyControlerWrapper", init<std::string>())
        .def("start_measurement", &PowerSupplyControlerWrapper::start_measurement)
        .def("stop_measurement", &PowerSupplyControlerWrapper::stop_measurement)
        .def("get_data", &PowerSupplyControlerWrapper::get_data)
        .def("freeze_data", &PowerSupplyControlerWrapper::freeze_data)
        .def("get_times", &PowerSupplyControlerWrapper::get_times)
        .def("get_voltages", &PowerSupplyControlerWrapper::get_voltages)
        .def("get_currents", &PowerSupplyControlerWrapper::get_currents)
    ;
}