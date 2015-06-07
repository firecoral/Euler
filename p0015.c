#include <stdio.h>
#include <stdlib.h>

int
node(int n, int x, int y) {
    int count = 0; 

    if (x == n && y == n)
	return 1;

    if (x < n)
	count += node(n, x+1, y);
    if (y < n)
	count += node(n, x, y+1);
    return count;
}

int
main(int argc, char *argv[]) {
    int n = 20;

    printf("%d: %d\n", n, node(n, 0, 0));
    exit(0);
}

