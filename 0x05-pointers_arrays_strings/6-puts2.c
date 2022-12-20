#include "main.h"
#include <stdio.h>

/**
 * puts2 - prints character of a string
 * @str: string pointer
 * Return: Always 0
 */
void puts2(char *str);
{

	putchar(str[0]);
	putchar('\n');

	for (int i = 2; str[i] != '\0'; i += 2)
	{
	putchar(str[i]);

	putchar('\n');
	}
}
