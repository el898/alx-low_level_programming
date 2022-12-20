#include "main.h"
#include <stdio.h>
#include <string.h>
/**
 * rev_string - reverses a string
 * @s:  pointer to the string
 * Return: Always 0
 */
void rev_string(char *s)
{
	char *end = s + strlen(s) - 1;

	while (s < end)
	{
		char temp = *s;
		*s++ = *end;
		*end-- = temp;
	}
}
