#pragma once
#include <stdbool.h>
#include "types.h"

typedef struct {
    int id;
    int position;
    int speed;
    int authority;
    int dwell;
    bool telemetry_ok;
    TrainState state;
} Train;

extern Train trains[];
extern int system_time;
