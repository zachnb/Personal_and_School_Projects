#include "safety.h"
#include "train.h"
#include "config.h"
#include <assert.h>
static int abs_i(int x){return x<0?-x:x;}
int compute_authority(int self){int limit=TRACK_END; for(int i=0;i<MAX_TRAINS;i++){ if(i!=self && trains[i].position>trains[self].position){int c=trains[i].position-SAFE_DISTANCE; if(c<limit) limit=c;}} return limit;}
void enforce_invariants(void){ for(int i=0;i<MAX_TRAINS;i++) for(int j=i+1;j<MAX_TRAINS;j++) assert(abs_i(trains[i].position-trains[j].position)>=SAFE_DISTANCE); }
