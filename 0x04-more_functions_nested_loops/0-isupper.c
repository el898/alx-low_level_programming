#include "main.h"
#include <stdio.h>
/**
 * _isupper - checks if the character is uppercase
 * Return: (1) if uppercase else (0)
 */
int _isupper(int c)
{
	  if (c >= 'A' || c <= 'Z')
		      return(1);
	    else  
		        return(0);
}
