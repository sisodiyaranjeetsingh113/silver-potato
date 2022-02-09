#include<stdio.h>
#include<conio.h>
int fact1=1;
int main()
{
int number;
printf("Enter a number :");
scanf("%d",&number);
int i=number;
while(i!=1)
{
fact1=fact1*i;
i--;
}
printf("%d",fact1);
return 0;
}