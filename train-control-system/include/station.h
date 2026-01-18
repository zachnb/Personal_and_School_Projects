#pragma once

typedef struct {
    const char* name;
    int position;
    int occupied_by;
} Station;

extern Station stations[];
