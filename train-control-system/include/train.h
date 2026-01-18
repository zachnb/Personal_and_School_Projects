#pragma once
#include "types.h"
#include <stdbool.h>
typedef struct { int id, position, speed, authority, dwell; bool telemetry_ok; TrainState state; } Train;
extern Train trains[]; extern int system_time;
