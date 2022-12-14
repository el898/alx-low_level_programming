#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/**
 * main - assigns a random number to the variable n each time it is
 *
 * Return: Always O
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;

	if (n > 0)
		printf("%d is positive",n);
	if (n == 0)
		printf("%d is zero",n);
	if (n < 0)
		printf("%d is negative",n);
	return (0);
}
