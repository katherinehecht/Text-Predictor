#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>

int main()
{
	int * a = calloc(1, sizeof(int));
	*a = 5;
	fprintf(stdout, "%d\n", *a);
	return 0;
}
