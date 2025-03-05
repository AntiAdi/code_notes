//Aadityaraj Kaushal going God Mode here </>

#include <stdio.h>
#include <stdlib.h>

void clear_scr();
void print_matrix(int rows, int columns, int** pointer);
void matrix_multiplication(int rows1, int columns1, int rows2, int columns2, int** M1, int** M2, int** MR);


int main(){

    /*
        taking input for Matrix 1
    */
    clear_scr();
    int rows1, columns1;
    printf("Number of Rows for Matrix 1: ");
    scanf("%d", &rows1);
    printf("\nNumber of Columns for Matrix 1 : ");
    scanf("%d", &columns1);

    //dynamically allocating matrices as 2D matrices.
    int** matrix1 = (int**) malloc (sizeof(int*)*rows1);
    //taking input for matrix values.
    for(int i=0 ; i<rows1 ; i++){
        matrix1[i] = (int*) malloc (sizeof(int)*columns1);
        
        printf("\nEnter values for Row %d , Seperated by Blank Spaces : ", i+1);
        for(int j=0 ; j<columns1 ; j++){
            scanf("%d", &matrix1[i][j]);
        }
    }

    /*
        taking input for Matrix 2
    */
    clear_scr();
    int rows2, columns2;
    printf("Number of Rows for Matrix 2: ");
    scanf("%d", &rows2);
    printf("\nNumber of Columns for Matrix  : ");
    scanf("%d", &columns2);

    //dynamically allocating matrices as 2D matrices.
    int** matrix2 = (int**) malloc (sizeof(int*)*rows2);
    //taking input for matrix values.
    for(int i=0 ; i<rows2 ; i++){
        matrix2[i] = (int*) malloc (sizeof(int)*columns2);
        
        printf("\nEnter values for Row %d , Seperated by Blank Spaces : ", i+1);
        for(int j=0 ; j<columns2 ; j++){
            scanf("%d", &matrix2[i][j]);
        }
    }



    //printing the two matrices.
    clear_scr();
    printf("MATRIX 1 :\n\n");
    print_matrix(rows1, columns1, matrix1);
    printf("\n\nMATRIX 2 :\n\n");
    print_matrix(rows2, columns2, matrix2);


    //warning , if the matrices can't be multiplied.
    //declaring two matrices for Matrix1 X 2 and 2 X 1, if possible.
    //printing the resultant matrices as well.
    int flag_M1xM2_exists=0;
    int flag_M2xM1_exists=0;

    if(columns1 != rows2){
        printf("\nMatrix1  X  Matrix2 is NOT possilbe.\n");
    }
    else{
        int** M1xM2 = (int**) malloc (sizeof(int*) * rows1);
        for(int i=0 ; i<rows1 ; i++){
            M1xM2[i] = (int*) malloc (sizeof(int)*columns2);
        }
        flag_M1xM2_exists = 1;

        printf("\nMATRIX 1 X MATRIX 2 :\n");
        matrix_multiplication( rows1,  columns1,  rows2,  columns2, matrix1, matrix2, M1xM2);
        print_matrix(rows1, columns2, M1xM2);
    }

    if(columns2 != rows1){
        printf("\nMatrix2  X  Matrix1 is NOT possilbe.\n");
    }
    else{
        int** M2xM1 = (int**) malloc (sizeof(int*) * rows2);
        for(int i=0 ; i<rows2 ; i++){
            M2xM1[i] = (int*) malloc (sizeof(int)*columns1);
        }
        flag_M2xM1_exists = 1;

        printf("\nMATRIX 2 X MATRIX 1 :\n");
        matrix_multiplication( rows2,  columns2,  rows1,  columns1, matrix2, matrix1, M2xM1);
        print_matrix(rows1, columns2, M2xM1);
    }

    printf("\n");

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

void print_matrix(int rows, int columns, int** pointer){
    for(int i=0 ; i<rows ; i++){
        for(int j=0 ; j<columns ; j++){
            printf("%-4d", pointer[i][j]);
        }
        printf("\n");
    }
}


void matrix_multiplication(int rows1, int columns1, int rows2, int columns2, int** M1, int** M2, int** MR){

    for(int i=0 ; i<rows1 ; i++){
        for(int j=0 ; j<columns2 ; j++){
            for(int k=0 ; k<columns1 ; k++){
                MR[i][j] += M1[i][k] * M2[k][j];
            }
        }
    }

}