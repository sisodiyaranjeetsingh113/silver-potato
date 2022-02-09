#include<stdio.h>
#include<conio.h>
int main()
{
int a,b,c,d;

a=300;
b=100;
c=50;
d=400;

if(a>b)
{
   if(a>c)
  {
       if(a>d)
       {
        printf("Greatest number is%d",a);    
        }
         else
        {
          printf("Greatest number is %d",d);    
         }
  }
  else
  {
       if(c>d)
        {
         printf(" Greatest number is %d",c);          
         }
        else
        {
          printf("Greatest number is %d",d);    
         }
   }

}
else{
   if(b>c)
   { 
           if(b>d)
           {
	printf("Greatest number is %d",b);   
            }
             else
            { 
             printf("Greatest number is %d",d);   
             }
    } else
    {
            if(c>d)
             {
              printf("Greatest number is %d",c);    
               }
              else{
               printf("Greatest number is %d",d);    
               }

      }
}

return 0;
}