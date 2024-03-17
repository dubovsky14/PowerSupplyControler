#include "../headers/PowerSupplyControler.h"

#include <iostream>

using namespace std;

int main(int argc, const char **argv) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <output_file>" << endl;
        return 1;
    }

    PowerSupplyControler psu(argv[1]);
    psu.start_measurement(100, 1000);
    this_thread::sleep_for(chrono::seconds(10));
    psu.stop_measurement();
    auto [time, voltage, current] = psu.get_data();
    for (size_t i = 0; i < time.size(); i++) {
        cout << time[i] << ", " << voltage[i] << ", " << current[i] << endl;
    }
    return 0;
}