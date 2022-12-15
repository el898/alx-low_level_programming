#include "main.h"

/**
 * _isalpha - checks if the letter is lower case
 * @e : character to check
 * Return:0 or 1
 */

int _isalpha(int e)

{

	return ((e >= 97 && e <= 122) || (e >= 65 && e <= 90));

}
