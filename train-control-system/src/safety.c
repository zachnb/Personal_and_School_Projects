#include "safety.h"
#include "train.h"
#include "config.h"

int compute_authority(int self) {
    int limit = TRACK_END;

    for (int i = 0; i < MAX_TRAINS; i++) {
        if (i == self) continue;

        if (trains[i].position > trains[self].position) {
            int candidate = trains[i].position - SAFE_DISTANCE;
            if (candidate < limit)
                limit = candidate;
        }
    }
    return limit;
}
