#include <stdio.h>
#include <stdlib.h>

// struct for the array that will be sent back to python
typedef struct IntervalArrayStruct {
    int a; /* Variable for first dimension of array? */
    int array[1][2]; /* An array that handles start/end intervals */
} IntervalArrayStruct; /* Initialize empty struct. */


// maximum and minimum functions
int maximum(int temp, int temp2){
    if(temp > temp2){
        return temp;
    } else {
        return temp2;
    }

}

int minimum(int temp, int temp2){
    if(temp < temp2){
        return temp;
    } else {
        return temp2;
    }

}

extern void schedule_match(IntervalArrayStruct *schedule) {
    int test1 = schedule->array[0][0];
    int test2 = schedule->array[0][1];
    int success = 0;
    
    // intersection function
    for(int i = 0; i < schedule->a; i++){
        // referenced GeeksForGeeks for the if conditions and idea of introducing a min function
        if(schedule->array[i][1] < test1 || schedule->array[i][0] > test2){
            // schedule->array[0][0] = -1;
            // schedule->array[0][1] = -1;
            success = 0;
        } else {
            test1 = maximum(test1, schedule->array[i][0]);
            test2 = minimum(test2, schedule->array[i][1]);
        }
    }

    if(test1 == schedule->array[0][0] && schedule->array[0][0] != schedule->array[1][0]){
        schedule->array[0][0] = -1;
        schedule->array[0][1] = -1;
    } else if(success == 0){
        schedule->array[0][0] = test1;
        schedule->array[0][1] = test2;
    }

}