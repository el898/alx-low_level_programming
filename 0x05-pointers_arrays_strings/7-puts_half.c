#include "main.h"
#include <stdio.h>
#include <string.h>

/**
 * puts_half - reverses a string
 * @str:  pointer to the string
 * Return: Always 0
 */
void puts_half(char *str)
{

	int length = strlen(str);

	if (length % 2 == 0)
	{
	printf("%.*s\n", length / 2, str + length / 2);
	}
	else
	{
	printf("%.*s\n", (length - 1) / 2, str + (length + 1) / 2);
	}
}
