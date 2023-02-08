#include <stddef.h>
#include "main.h"
/**
 * _strspn - gets the length of the prefix substring
 * @s: string where substring will look
 * @accept: substring of accepred chars
 * Return: length of occurance
 */
unsigned int _strspn(char *s, char *accept)
{
	unsigned int count = 0;

	for (; *s; ++s)
	{
		for (char *a = accept; *a; ++a)
		{
			if (*s == *a)
			{
				++count;
				break;
			}
		}
		if (*(s + count) != *s)
		{
			break;
		}
	}
	return (count);
}
