#include<stdio.h>
#define MAX_NUM 50

int ftemp(int arr[], int size_of_array);

int main()
{
    int size_of_array;
    int A[MAX_NUM];
    int i = 0;
    scanf("%d", &size_of_array);

    
    for(i = 0; i< size_of_array; i++){
        scanf("%d", &A[i]);
    }


    ftemp(A, size_of_array);
    return 0;
}

int ftemp(int arr[], int size_of_array){
    int P[MAX_NUM] = {0,};
    int i, j;
    for(i=0; i<size_of_array; i++){
        for(j = 0; j<size_of_array; j++){
            if(i == j)
                continue;
            if(arr[i] > arr[j])
                P[i]++;
            if(arr[i] == arr[j] && i>j)
                P[i]++;
        }
    }
    
    for(i=0; i<size_of_array; i++){
        printf("%d", P[i]);
    }
}