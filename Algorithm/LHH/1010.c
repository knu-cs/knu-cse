#include<stdio.h>

int Combination(int n, int r);
int main()
{
    int num_right_site, num_left_site;
    int num_test_case;
    int i;
    scanf("%d", &num_test_case);

    for(i = 0; i<num_test_case; i++){
        scanf("%d %d", &num_left_site, &num_right_site);
        printf("%d\n", Combination(num_right_site, num_left_site));
    }
}

int Combination(int n, int r)
{
    if(r==0)
        return 1;
    else if(n == r)
        return 1;
    else
        return Combination(n-1, r-1)+Combination(n-1, r);
}