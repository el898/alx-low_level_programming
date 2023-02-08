#include <stdio.h>
#include <string.h>
#include "main.h"
/**
 * _strpbrk - bytes
 * @s: char pointer
 * @accept: char pointer
 * Return: Null
 */
char *_strpbrk(char *s, char *accept)
{

	int i, j;

	for (i = 0; s[i]; i++)
	{
	for (j = 0; accept[j]; j++)
	{
		if (s[i] == accept[j])
		{
			return (&s[i]);
		}
	}
	}

	return (NULL);

}
