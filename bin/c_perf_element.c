#include <stdio.h>
#include <stdlib.h>

// used for cmpfunc https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

struct vectord {
    short garbage; // "flexible array member in a struct with no named members"
    int arr[];
};

struct vector2d {
    short garbage;
    int arr[][2];
};

typedef struct IntervalArrayStruct {
    int a; /* Variable for first dimension of array? */
    int array[1][2]; /* An array that handles start/end intervals */
} IntervalArrayStruct; /* Initialize empty struct. */

extern void schedule_match(IntervalArrayStruct *schedule) {
    int i, j;
    int k = 0;

    // changed from * 1000 to * schedule->a, sizeof(schedule->a should be 4 bytes, int)
    // * 2 is for allocating enough memory for a 2D array
    struct vector2d *tester = malloc(sizeof(schedule->a) * schedule->a * 2);
    struct vectord *test = malloc(sizeof(schedule->a) * schedule->a);
    struct vectord *test2 = malloc(sizeof(schedule->a) * schedule->a);

    // Checks if there are any overlaps in times
    // printf("\nPrinting overlapping times: \n");
    for (j = 1; j < schedule->a; j++){
        if(schedule->array[j - 1][1] > schedule->array[j][0]){
            tester->arr[k][0] = schedule->array[j][0];
            test->arr[k] = schedule->array[j][0];
            tester->arr[k][1] = schedule->array[j - 1][1];
            test2->arr[k] = schedule->array[j - 1][1];
            k += 1;

        }

    }

    if(k == 0){
        schedule->array[0][0] = -1;
        schedule->array[0][1] = -1;
    } else {
        qsort(test->arr, k, sizeof(test->arr[0]), cmpfunc);
        qsort(test2->arr, k, sizeof(test2->arr[0]), cmpfunc);

        // referenced GeeksForGeeks implementation
        // had to make tweaks to look at the two arrays
        int max = 1;
        int current = 1;
        int common = test->arr[0];

        for(i = 1; i < k; i++){
            if(test->arr[i - 1] == test->arr[i]){
                current++;
            } else {
                if(max < current){
                    common = test->arr[i - 1];
                    max = current;
                }
                current = 1;
            }
        }

        if(max < current){
            common = test->arr[i - 1];
        }

        max = 1;
        current = 1;
        int common2 = test2->arr[0];

        for(i = 1; i < k; i++){
            if(test2->arr[i - 1] == test2->arr[i]){
                current++;
            } else {
                if(max < current){
                    common2 = test2->arr[i - 1];
                    max = current;
                }
                current = 1;
            }
        }

        if(max < current){
            common2 = test2->arr[i - 1];
        }

        schedule->array[0][0] = common;
        schedule->array[0][1] = common2;
    }

}