#include "motion.h"
#include "train.h"
#include "station.h"
#include "config.h"
#include "safety.h"
void task_motion(void){ for(int i=0;i<MAX_TRAINS;i++){ Train*t=&trains[i]; switch(t->state){ case STOPPED: t->speed=MAX_SPEED; t->state=MOVING; break; case MOVING: t->position+=t->speed; for(int s=0;s<MAX_STATIONS;s++) if(t->position>=stations[s].position && stations[s].occupied_by==-1){stations[s].occupied_by=t->id; t->state=DWELLING; t->dwell=0;} break; case DWELLING: t->speed=0; if(++t->dwell>=DWELL_TIME){ for(int s=0;s<MAX_STATIONS;s++) if(stations[s].occupied_by==t->id) stations[s].occupied_by=-1; t->state=STOPPED;} break; case EMERGENCY_STOP: t->speed=0; break;} } enforce_invariants(); }
