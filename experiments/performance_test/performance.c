#include <stdio.h>
#include <stdlib.h>

int counter() {  // this will print stuff
    int a = 0;
    for (int i = 0; i < 100000; i++) {
        a++;
    }
    return a;
}