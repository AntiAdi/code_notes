//Aadityaraj Kaushal going God Mode here </>

#include <stdio.h>
#include <stdlib.h>

void clear_scr();



int main(){
    clear_scr();
    printf("Enter number of rows (Height) : ");
    int rows;
    scanf("%d", &rows);


    clear_scr();
    int max_width = 2*rows - 1 ;
    int mid_index = rows;

    for(int row=1 ; row<= rows ; row++){
        int row_width = 2*row - 1 ;
        
        for(int row_counter = 1 ; row_counter<=max_width ; row_counter++){
            if(row_counter >= (mid_index-row+1) && row_counter <= (mid_index+row-1)){
                printf("*");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }


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