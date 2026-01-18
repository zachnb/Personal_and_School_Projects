#include "control.h"
#include "train.h"
#include "safety.h"

void task_control(void) {
    for (int i = 0; i < 3; i++) {
        Train* t = &trains[i];

        if (!t->telemetry_ok) {
            t->state = EMERGENCY_STOP;
            continue;
        }

        t->authority = compute_authority(i);

        if (t->position >= t->authority) {
            t->state = EMERGENCY_STOP;
        }
    }
}
