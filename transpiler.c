#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
    if(argc != 2){
        printf("Usage: mlpy <filename>");
    }
    else{
        char command[100] = "python _handler.py ";
        strcat(command, argv[1]);
        system(command);
    }
    return 0;
}