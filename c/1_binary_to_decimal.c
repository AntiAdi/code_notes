//Aadityaraj Kaushal going God Mode here </>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void clear_scr();



int main(){
    clear_scr();
    int size;
    printf("Enter the length of your binary number  :  ");
    scanf("%d", &size);

    char* binary_number = (char*) calloc (size+1, sizeof(char));

    printf("Enter your binary number without spaces :\n");
    scanf(" %s", binary_number);

    int decimal=0;
    int counter= strlen(binary_number) - 1;
    int multiplier=1;

    while(binary_number[counter] != '\0'){
        decimal += (binary_number[counter] - '0') * multiplier;
        multiplier *= 2;
        counter--;
    }

    printf("\nDecimal Number = %d\n",decimal);


    return 0;
}





#ifdef _WIN32
    #define clear "cls" 
#else
    #define clear "clear" 
#endif


void clear_scr() {
    system(clear);
}