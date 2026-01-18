#include "control.h"
#include "motion.h"
#include "telemetry.h"
void init_system(void); void task_sensors(void); extern int system_time;
int main(void){init_system(); while(system_time<40){system_time++; task_sensors(); task_control(); task_motion(); task_telemetry();} return 0;}
