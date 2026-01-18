#include "train.h"
#include "station.h"
#include "config.h"
Train trains[MAX_TRAINS]; Station stations[MAX_STATIONS]; int system_time=0;
void init_system(void){stations[0]=(Station){"Central",100,-1};stations[1]=(Station){"Junction",250,-1};stations[2]=(Station){"Airport",400,-1};stations[3]=(Station){"Harbor",550,-1};trains[0]=(Train){0,0,0,TRACK_END,0,1,STOPPED};trains[1]=(Train){1,120,0,TRACK_END,0,1,STOPPED};trains[2]=(Train){2,240,0,TRACK_END,0,1,STOPPED};}
