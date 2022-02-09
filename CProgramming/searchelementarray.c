#include<stdio.h>
#include<conio.h>
int main()
{
int i,number,lookout;
printf("Enter a number tobe find :");
scanf("%d",&number);
int array[10]={10,40,25,32,12,54,65,13,90,75};
for(i=0;i<10;i++)
{
   if(number ==array[i])
    {
     lookout=1;
     break;
     }
     else
    {
      lookout=0;   
     }
}
if(lookout ==1)
{
printf("%d is found",number);
}
else
{
printf("%d is not found",number);
}
return 0;
}