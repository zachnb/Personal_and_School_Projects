#include <stdio.h>
#include "telemetry.h"
#include "train.h"

void task_telemetry(void) {
    printf("\n[TIME %d]\n", system_time);
    for (int i = 0; i < 3; i++) {
        printf("Train %d | Pos %3d | Speed %2d | State %d | Telemetry %s\n",
               trains[i].id,
               trains[i].position,
               trains[i].speed,
               trains[i].state,
               trains[i].telemetry_ok ? "OK" : "FAIL");
    }
}
