#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <ctype.h>
#include <string.h>

#define HANDLER "_handler.py"

#ifdef _WIN32
#define CMD "python.exe"
#elif __APPLE__
#define CMD "python"
#elif __linux__
#define CMD "python3"
#endif

void stradd(char* dest, const char* src) {
    strcat(dest, " ");
    strcat(dest, src);
}

int main(int argc, char *argv[]) {
    int opt;
    int flag_c = 0;
    char *ofile = NULL;

    while ((opt = getopt(argc, argv, "co:h")) != -1) {
        switch (opt) {
            case 'c':
                flag_c = 1;
                break;
            case 'o':
                ofile = optarg;
                break;
            case 'h':
                printf("Usage: %s <filename> [-c (compile only)][-o <output filename>\n", argv[0]);
                exit(0);
            case '?':
                if (optopt == 'o') {
                    fprintf(stderr, "Option -o requires an argument.\n");
                }
                else if (isprint(optopt)) {
                    fprintf(stderr, "Unknown option: -%c\n", optopt);
                }
                else {
                    fprintf(stderr, "Unknown option.\n");
                }
            default:
                exit(1);
        }
    }
    if (optind >= argc) {
        fprintf(stderr, "Usage: %s <filename> [-c (compile only)][-o <output filename>]\n", argv[0]);
        exit(1);
    }

    //format: "CMD HANDLER CMD ifile flag_c ofile"
    char command[100] = CMD;
    stradd(command, HANDLER);
    stradd(command, CMD);
    stradd(command, argv[optind]);
    stradd(command, flag_c ? "CMPLONLY" : "CMPLNRUN");
    stradd(command, ofile != NULL ? ofile : "");
    
    system(command);
    return 0;
}