#include<stdio.h>
#include<conio.h>

int main()
{ 
/*int i;
printf("Enter a number: ");
scanf("%d",&i);
printf("number : %d",i);
*/
int number,remainder;
int reversenumber=0;
printf("Enter a number: ");
scanf("%d",&number);
while(number>0)
{
    remainder=number%10;
    reversenumber=reversenumber*10+remainder;
    number=number/10;
}
printf("%d",reversenumber);

 return 0;
}
