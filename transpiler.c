#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HANDLER "_handler.py"
#define NAME "mlpy"

#ifdef _WIN32
#define CMD "python.exe"
#elif __APPLE__
#define CMD "python"
#elif __linux__
#define CMD "python3"
#endif

int main(int argc, char *argv[]){
    if(argc != 2){
        printf("Usage: %s <filename>\n", NAME);
        return 1;
    }
    char command[100] = CMD;
    strcat(command, " ");
    strcat(command, HANDLER);
    strcat(command, " ");
    strcat(command, argv[1]);
    strcat(command, " ");
    strcat(command, CMD);
    system(command);
    return 0;
}