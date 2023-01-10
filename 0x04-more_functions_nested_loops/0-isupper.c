#include "main.h"
#include <stdio.h>
/**
 * _isupper - checks if the character is uppercase or not
 * @c: is the argument used for the function.
 * Return: (1) if uppercase else (0)
 */
int _isupper(int c)
{
	if (c >= 'A' || c <= 'Z')
		return (1);
	else
		return (0);
}
