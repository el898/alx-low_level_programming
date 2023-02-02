#include "main.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * clear_bit - sets the value of a bit to 0 at a given index
 * @n: parameter
 * @index: index
 * Return: 1 if works, -1 if error
 */
int clear_bit(unsigned long int *n, unsigned int index)
{
	if (n == NULL || index >= sizeof(unsigned long int) * 8)
	{
		return (-1);
	}
	*n &= ~(1UL << index);
	return (1);
}
