#include <stdio.h>

#include <stdlib.h>

#include <time.h>

#include <string.h>



#define PASSWORD_LENGTH 8

#define CHARACTER_SET "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"



char *generate_password() {

  static char password[PASSWORD_LENGTH + 1];



  srand(time(0));

  int i = 0;

  while (i < PASSWORD_LENGTH) {

    int index = rand() % (sizeof(CHARACTER_SET) - 1);

    password[i] = CHARACTER_SET[index];

    i++;

  }

  password[PASSWORD_LENGTH] = '\0';



  return password;

}



int main() {

  char *password = generate_password();

  printf("Generated password: %s\n", password);



  return 0;

}

