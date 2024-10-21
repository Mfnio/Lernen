#include <stdio.h> 

int main()
{
    int userInput  = 0;
    scanf("%d", &userInput);
    double toDay = (userInput / 60.0) / 24.0;
    double toYear = toDay / 365.0;
    

    printf("your minutes to dayes is %f\n", toDay);
    printf("your mintes in years are %f\n", toYear);
    return 0;
}