cmake_minimum_required(VERSION 3.10)
project(monorail_cbtc C)
set(CMAKE_C_STANDARD 99)
include_directories(include)
add_executable(monorail
    src/main.c
    src/system_init.c
    src/sensor_task.c
    src/safety.c
    src/control_task.c
    src/motion_task.c
    src/telemetry.c
)
