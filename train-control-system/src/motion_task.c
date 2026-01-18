#include <assert.h>
#include "motion.h"
#include "train.h"
#include "station.h"
#include "config.h"

static int abs_val(int x) {
    return x < 0 ? -x : x;
}

static int should_depart(int train_id) {
    return system_time % (5 + train_id * 2) == 0;
}

void task_motion(void) {
    for (int i = 0; i < MAX_TRAINS; i++) {
        Train* t = &trains[i];

        switch (t->state) {
        case STOPPED:
            if (should_depart(i)) {
                t->speed = MAX_SPEED;
                t->state = MOVING;
            }
            break;

        case MOVING:
            t->position += t->speed;

            for (int s = 0; s < MAX_STATIONS; s++) {
                if (t->position >= stations[s].position &&
                    stations[s].occupied_by == -1) {

                    stations[s].occupied_by = t->id;
                    t->state = DWELLING;
                    t->dwell = 0;
                }
            }
            break;

        case DWELLING:
            t->speed = 0;
            t->dwell++;

            if (t->dwell >= DWELL_TIME) {
                for (int s = 0; s < MAX_STATIONS; s++)
                    if (stations[s].occupied_by == t->id)
                        stations[s].occupied_by = -1;

                t->state = STOPPED;
            }
            break;

        case EMERGENCY_STOP:
            t->speed = 0;
            break;
        }

        assert(t->state != EMERGENCY_STOP || t->speed == 0);
        assert(t->position <= t->authority || t->state == EMERGENCY_STOP);
    }

    for (int i = 0; i < MAX_TRAINS; i++)
        for (int j = i + 1; j < MAX_TRAINS; j++)
            assert(abs_val(trains[i].position -
                           trains[j].position) >= SAFE_DISTANCE);
}
