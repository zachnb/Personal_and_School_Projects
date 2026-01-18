#include "train.h"

void task_sensors(void) {
    for (int i = 0; i < 3; i++) {
        if (system_time == 20 && i == 1) {
            trains[i].telemetry_ok = false;
        }
    }
}
