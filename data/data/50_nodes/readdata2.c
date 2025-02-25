#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include <sys/stat.h>

int data[700][3];

int main(int argc, char *argv[])
{

    char *filename = argv[1]; 
    char out_filename[200];
    FILE *in_file;
    FILE *out_file;

    strcpy(out_filename, filename);
    strcat(out_filename, "_1.txt");
    strcat(filename, ".txt");

    in_file = fopen(filename, "r");    
    if (in_file == NULL)
    {
      printf("can not open input file for reading\n");
      return 1;
    }
    
    
    out_file =  fopen(out_filename, "a+");  
    if (out_file == NULL)
    {
      printf("can not open output file for writing\n");
      return 1;
    }
    struct stat sb;
    stat(filename, &sb);

    char *file_contents = malloc(sb.st_size);
    char *token;

    int i=0, count;
    while(fscanf(in_file, "%[^\n] ", file_contents) != EOF) {
      //  printf("> %s\n", file_contents);
        token = strtok(file_contents, " ");
        data[i][0] = atoi(token);
        //printf("%s ", token);
        token = strtok(NULL, " ");
        data[i][1] = atoi(token);
    //printf("%s ", token);

        token = strtok(NULL, " ");
        data[i][2] = atoi(token);
        
        if(data[i][1]<=50)
        {
          fprintf(out_file, "%d	%d	%d\n", data[i][0], data[i][1], data[i][2]);
        }
    //printf("%s ", token);

        /*count = 0;
        while(token != NULL)
        {
          //printf("%s ", token);
          tasks[i].pred[count] = atoi(token);
          token = strtok(NULL, " ");
          count++;
        }*/
        i++;
    }
    
    fclose(in_file);
    fclose(out_file);
    exit(EXIT_SUCCESS);
}
