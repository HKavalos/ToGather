import os
from ctypes import *

INTERVAL_LENGTH = 2

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

def schedule_match(new_array, size, optimal_times):
    new_array = sorted(new_array)

    class IntervalArrayStruct(Structure):
        _fields_ = [("a", c_int),
                    ("array", (c_int * INTERVAL_LENGTH) * size),
                    ]

    # lib = CDLL("%s/test.so" % os.getcwd())
    # lib = CDLL("%s/emergency_test.so" % os.getcwd())
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

    # print("\n" + "Optimal Time: ")

    # if constraints.array[0][0] >= 12:
    #     if(constraints.array[0][0] == 12):
    #         print(constraints.array[0][0], "pm to")
    #     else:
    #         print(constraints.array[0][0] - 12, "pm to")
    # else:
    #     print(constraints.array[0][0], "am to")

    # if constraints.array[0][1] > 12:
    #     if(constraints.array[0][1] == 24):
    #         print(constraints.optimal_end, "am")
    #     else:
    #         print(constraints.array[0][1] - 12, "pm")
    # else:
    #     print(constraints.array[0][1], "am")

    optimal_times.append((constraints.array[0][0], constraints.array[0][1]))

    return optimal_times

def driver(users):
    optimal_times = []
    sun = []
    mon = []
    tues = []
    weds = []
    thurs = []
    fri = []
    sat = []

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][0])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][0][y][0]
            time2 = users[x][1][0][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            sun.append((int(time1), int(time2)))

    # print("Sunday")
    # print(sun)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][1])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][1][y][0]
            time2 = users[x][1][1][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            mon.append((int(time1), int(time2)))

    # print("Monday")
    # print(mon)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][2])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][2][y][0]
            time2 = users[x][1][2][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            tues.append((int(time1), int(time2)))
    
    # print("Tuesday")
    # print(tues)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][3])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][3][y][0]
            time2 = users[x][1][3][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            weds.append((int(time1), int(time2)))
    
    # print("Wednesday")
    # print(weds)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][4])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][4][y][0]
            time2 = users[x][1][4][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            thurs.append((int(time1), int(time2)))
    
    # print("Thursday")
    # print(thurs)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][5])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][5][y][0]
            time2 = users[x][1][5][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            fri.append((int(time1), int(time2)))
    
    # print("Friday")    
    # print(fri)

    for x in range(0, len(users)):
        # print(users[x][0])
        for y in range(0, len(users[x][1][6])):
            # print(users[x][1][0][y][0])
            # print(users[x][1][0][y][1])
            time1 = users[x][1][6][y][0]
            time2 = users[x][1][6][y][1]

            time1 = time_maker(time1)
            time2 = time_maker(time2)

            # print(time1 + " " + time2)

            sat.append((int(time1), int(time2)))
    
    # print("Saturday")
    # print(sat)

    optimal_times = schedule_match(tuple(sun), len(sun), optimal_times)
    optimal_times = schedule_match(tuple(mon), len(mon), optimal_times)
    optimal_times = schedule_match(tuple(tues), len(tues), optimal_times)
    optimal_times = schedule_match(tuple(weds), len(weds), optimal_times)
    optimal_times = schedule_match(tuple(thurs), len(thurs), optimal_times)
    optimal_times = schedule_match(tuple(fri), len(fri), optimal_times)
    optimal_times = schedule_match(tuple(sat), len(sat), optimal_times)

    return optimal_times