#include <stdio.h>
int main()
{
    int age = 0;
    printf("What's your age?\n");
    printf("type it here: ");
    scanf("%d", &age);
    if(age >= 18){
        printf("You can vote!\n");
    }
    
    else{printf("you can't vote!\n");}
    
    return 0;
}