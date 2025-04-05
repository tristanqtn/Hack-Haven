/*
Code written by TRISTAN QUERTON on 12/23/2020
All rights reserved
This code is able to genrate different type of password.
This code is only practice and is not intended for hacking purposes.
I will NOT be held responsible for anything silly you may do with this!
*/

#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <Windows.h>

void simplePWD();
void spePWD();
void numPWD();
void fullPWD();

int main()
{
    char lowKey[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char upKey[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char special[11] = {33, 35, 36, 37, 38, 40, 41, 42, 43, 45, 47};
    char number[10] = {48, 49, 50, 51, 52, 53, 54, 55, 56, 57};
    char *PWD;
    char generation[30];

    int verif = 1;

    int lenghtPWD;

    int autorSpe;
    int autorNum;

    srand(time(NULL));

    do
    {
        printf("How many characters do you want in your password : ");
        fflush(stdin);
        scanf("%d", &lenghtPWD);

        PWD = (char *)malloc(lenghtPWD * sizeof(char));

        printf("Do you want to include special character in your password ? enter 1 for yes / 0 for no : ");
        fflush(stdin);
        scanf("%d", &autorSpe);

        printf("Do you want to include numbers in your password ? enter 1 for yes / 0 for no : ");
        fflush(stdin);
        scanf("%d", &autorNum);

        for (int j = 0; j < 50; j++)
        {
            generation[j] = NULL;
        }

        if (autorNum != 1 && autorSpe != 1)
        {
            simplePWD(lenghtPWD, lowKey, upKey, generation);
        }
        if (autorSpe == 1 && autorNum != 1)
        {
            spePWD(lenghtPWD, lowKey, upKey, special, generation);
        }
        if (autorSpe != 1 && autorNum == 1)
        {
            numPWD(lenghtPWD, lowKey, upKey, number, generation);
        }
        if (autorSpe == 1 && autorNum == 1)
        {
            fullPWD(lenghtPWD, lowKey, upKey, number, special, generation);
        }

        strcpy(PWD, generation);
        printf("%s", PWD);
        free(PWD);

        printf("\nDo you want to generate another password ? enter 1 for yes / 0 for no : ");
        scanf("%d", &verif);

        Sleep(100);

    } while (verif == 1);

    return 0;
}

void simplePWD(int lenghtPWD, char lowKey[26], char upKey[26], char generation[50])
{
    int alea;

    for (int i = 0; i < lenghtPWD; i++)
    {
        alea = rand();
        if ((alea % 2) == 0)
        {
            generation[i] = lowKey[rand() % 25];
        }
        else
        {
            generation[i] = upKey[rand() % 25];
        }
    }
}

void spePWD(int lenghtPWD, char lowKey[26], char upKey[26], char spe[11], char generation[50])
{
    int alea;

    for (int i = 0; i < lenghtPWD; i++)
    {
        alea = rand();
        if ((alea % 2) == 0)
        {
            generation[i] = lowKey[rand() % 25];
        }
        else if ((alea % 3) == 0)
        {
            generation[i] = upKey[rand() % 25];
        }
        else
        {
            generation[i] = spe[rand() % 10];
        }
    }
}

void numPWD(int lenghtPWD, char lowKey[26], char upKey[26], char num[10], char generation[50])
{
    int alea;

    for (int i = 0; i < lenghtPWD; i++)
    {
        alea = rand();
        if ((alea % 2) == 0)
        {
            generation[i] = lowKey[rand() % 25];
        }
        else if ((alea % 3) == 0)
        {
            generation[i] = upKey[rand() % 25];
        }
        else
        {
            generation[i] = num[rand() % 9];
        }
    }
}

void fullPWD(int lenghtPWD, char lowKey[26], char upKey[26], char num[10], char spe[11], char generation[50])
{
    int alea;

    for (int i = 0; i < lenghtPWD; i++)
    {
        alea = rand();

        if ((alea % 2) == 0)
        {
            generation[i] = spe[rand() % 10];
            i++;
            generation[i] = lowKey[rand() % 25];
        }
        else if ((alea % 3) == 0)
        {
            generation[i] = num[rand() % 25];
            i++;
            generation[i] = lowKey[rand() % 25];
        }
        else if ((alea % 5) == 0)
        {
            generation[i] = spe[rand() % 10];
            i++;
            generation[i] = upKey[rand() % 25];
            i++;
            generation[i] = num[rand() % 9];
            i++;
            generation[i] = lowKey[rand() % 25];
        }
        else
        {
            generation[i] = upKey[rand() % 25];
        }
    }
}