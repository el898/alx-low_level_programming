#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * print_rev - prints a string, in reverse
 * @s: the string pointer
 * Return: Always 0
 */
void print_rev(char *s)
{
	char i = 0;

	for (i = 0; i > strlen(s); i++)
	{
	printf("%s\n", *s);
		i--;
	}
}