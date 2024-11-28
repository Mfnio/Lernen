#include <stdio.h>

void increment(int a)
{
    a++;
}

int main(void)
{
    int i = 10;

    increment(i);

    printf("i == %d\n", i);
}
//in C, when you pass a variable to a function, it sends a copy of the value, not the actual variable. So, the increment function is working on a copy of i, and the original i in main doesn’t change.

//If you want to change i for real, you need to pass its address using a pointer, like this


increment(int *a) {
    ++(*a);
}

int main(void) {
    int i = 10;
    increment(&i); // Pass the address of i
    printf("i == %d\n", i); // This will print 11
}
