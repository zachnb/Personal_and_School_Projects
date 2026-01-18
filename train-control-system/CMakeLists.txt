cmake_minimum_required(VERSION 3.10)
project(train_control_system C)

set(CMAKE_C_STANDARD 99)

include_directories(include)

add_executable(train_control_system
    src/main.c
    src/system_init.c
    src/sensor_task.c
    src/motion_task.c
    src/control_task.c
    src/telemetry.c
    src/safety.c
)
