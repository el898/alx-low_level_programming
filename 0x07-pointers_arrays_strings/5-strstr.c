#include <stdio.h>
#include <string.h>
#include "main.h"
/**
 * _strstr - function locate
 * @haystack: pointer to char
 * @needle: pointer to char
 * Return: NULL
 */
char *_strstr(char *haystack, char *needle)
{

	int i, j;

	for (i = 0; haystack[i]; i++)
	{
		for (j = 0; needle[j]; j++)
		{
			if (haystack[i + j] != needle[j])
			{
				break;
			}
		}
		if (!needle[j])
		{
			return (&haystack[i]);
		}
	}
	return (NULL);
}
