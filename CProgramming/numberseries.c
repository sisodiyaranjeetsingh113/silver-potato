#include<stdio.h>
#include<conio.h>

int main()
{
int i,number,number1;
printf("Enter a number :");
scanf("%d",&number);
for(i=1;i<=10;i++)
{
      number1=number*i;
      printf("%d\n",number1);
}
return 0;
}