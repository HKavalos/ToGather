import os
from ctypes import *

# 2D array sample_array[][2]
INTERVAL_LENGTH = 2

# takes a string in the format ex. 05:00 am and changes it to 5 (depends on am/pm as well)
def time_maker(temp):
    test = temp
    test_int = ""

    for i in test:
        if(i == ':'):
            break
        test_int += i

    if(test[-2] + test[-1] == "PM" and int(test_int) < 12):
        test_int = str(int(test_int) + 12)

    elif(test[-2] + test[-1] == "AM" and int(test_int) == 12):
        test_int = str(int(test_int) + 12)

    return test_int

# takes an int (ex. 5) and formats it back into a string in the format ex. 05:00 am
def time_revert(temp):
    test = temp
    test_int = ""

    if(test == -1):
        return "-1"

    if(test == 0):
        test = 24

    if(test > 12):
        test_int = str(test - 12)
        if(int(test_int) < 10):
            test_int = "0" + test_int + ":00"
        else:
            test_int = test_int + ":00"
    else:
        test_int = str(test)

        if(test < 10):
            test_int = "0" + test_int + ":00"
        else:
            test_int = test_int + ":00"

    if(test >= 12 and test != 24):
        test_int = test_int + " PM"
    else:
        test_int = test_int + " AM"

    return test_int

# runs the schedule match function from the c library c_perf_element.so
def schedule_match(new_array, size, optimal_times):
    new_array = sorted(new_array)

    class IntervalArrayStruct(Structure):
        _fields_ = [("a", c_int),
                    ("array", (c_int * INTERVAL_LENGTH) * size),
                    ]

    lib = CDLL("%s/c_perf_element.so" % os.getcwd())
    lib.schedule_match.argtypes = [POINTER(IntervalArrayStruct)]
    lib.schedule_match.restype = None

    # Initialize struct ctype.
    constraints = IntervalArrayStruct()

    # Define struct with array values.
    for i in range(len(new_array)):
        for j in range(INTERVAL_LENGTH):
            constraints.array[i][j] = new_array[i][j]

    constraints.a = len(new_array)

    # Call schedule_match function from C lib.
    lib.schedule_match(byref(constraints))

    optimal_times.append((time_revert(constraints.array[0][0]), time_revert(constraints.array[0][1])))

    return optimal_times

# driver function that takes 5D array of schedules and translates it into 7 arrays
# each of the 7 arrays will have the time intervals of all users on a specific day
def driver(users):
    optimal_times = []
    sun = []
    mon = []
    tues = []
    weds = []
    thurs = []
    fri = []
    sat = []

    # Sunday
    for x in range(0, len(users)):
        if len(users[x][1][0]) == 0:
            time1 = 0
            time2 = 24

            sun.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][0])):
            time1 = users[x][1][0][y][0]
            time2 = users[x][1][0][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            sun.append((int(time1), int(time2)))
    
    # Monday
    for x in range(0, len(users)):
        if len(users[x][1][1]) == 0:
            time1 = 0
            time2 = 24

            mon.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][1])):
            time1 = users[x][1][1][y][0]
            time2 = users[x][1][1][y][1]

            time1 = time_maker(time1)

            if(time1 == 24):
                time1 = 0

            time2 = time_maker(time2)

            mon.append((int(time1), int(time2)))

    # Tuesday
    for x in range(0, len(users)):
        if len(users[x][1][2]) == 0:
            time1 = 0
            time2 = 24

            tues.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][2])):
            time1 = users[x][1][2][y][0]
            time2 = users[x][1][2][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            tues.append((int(time1), int(time2)))
    
    # Wednesday
    for x in range(0, len(users)):
        if len(users[x][1][3]) == 0:
            time1 = 0
            time2 = 24

            weds.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][3])):
            time1 = users[x][1][3][y][0]
            time2 = users[x][1][3][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            weds.append((int(time1), int(time2)))
    
    # Thursday
    for x in range(0, len(users)):
        if len(users[x][1][4]) == 0:
            time1 = 0
            time2 = 24

            thurs.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][4])):
            time1 = users[x][1][4][y][0]
            time2 = users[x][1][4][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            thurs.append((int(time1), int(time2)))
    
    # Friday
    for x in range(0, len(users)):
        if len(users[x][1][5]) == 0:
            time1 = 0
            time2 = 24

            fri.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][5])):
            time1 = users[x][1][5][y][0]
            time2 = users[x][1][5][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            fri.append((int(time1), int(time2)))
    
    # Saturday
    for x in range(0, len(users)):
        if len(users[x][1][6]) == 0:
            time1 = 0
            time2 = 24

            sat.append((int(time1), int(time2)))

            continue

        for y in range(0, len(users[x][1][6])):
            time1 = users[x][1][6][y][0]
            time2 = users[x][1][6][y][1]

            time1 = time_maker(time1)

            if(int(time1) == 24):
                time1 = 0

            time2 = time_maker(time2)

            sat.append((int(time1), int(time2)))
    
    if(len(sun) != 0):
        optimal_times = schedule_match(tuple(sun), len(sun), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(mon) != 0):
        optimal_times = schedule_match(tuple(mon), len(mon), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(tues) != 0):
        optimal_times = schedule_match(tuple(tues), len(tues), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(weds) != 0):
        optimal_times = schedule_match(tuple(weds), len(weds), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(thurs) != 0):
        optimal_times = schedule_match(tuple(thurs), len(thurs), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(fri) != 0):
        optimal_times = schedule_match(tuple(fri), len(fri), optimal_times)
    else:
        optimal_times.append((0,24))

    if(len(sat) != 0):
        optimal_times = schedule_match(tuple(sat), len(sat), optimal_times)
    else:
        optimal_times.append((0,24))

    return optimal_times
