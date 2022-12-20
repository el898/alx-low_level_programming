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
	int length = strlen(s);

	for (int i = 0; i < length / 2; i++);
	{
		char temp = s[i];

		s[i] = s[length - i - 1];
		s[length - i - 1] = temp;

	}
}
