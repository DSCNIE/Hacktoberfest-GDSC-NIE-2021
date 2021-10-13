#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
int stack[50],top=-1;
void push(int n)
{
    if(top==49)
    {
        printf("Overflow\n");
        return;
    }
    else
    {
        top++;
        stack[top]=n;
    }
}
int pop()
{
    int a;
    if(top==-1)
    {
        printf("Underflow\n");
    }
    else
    {
       a=stack[top];
       top--;
    }
    return a;
}
void eval(char s[],int size)
{
    int a,b;
    char c;
    for(int i=size;i>=0;i--)
    {
        c=s[i];
        if(isdigit(c))
        {
            push(c-'0');
        }
        else if(c=='^'||c=='-'||c=='+'||c=='/'||c=='*'||c=='%')
        {
            a=pop();
            b=pop();
            switch(c)
            {
                case '^':push(pow(a,b));
                         break;
                case '*':push(a*b);
                         break;
                case '/':push(a/b);
                         break;
                case '-':push(a-b);
                         break;
                case '+':push(a+b);
                         break; 
                case '%':push(a%b);
                         break;         
                         
            }
        }
    }
    printf("Value of Prefix Expression=%d",pop());
}
int main()
{
    char s[50];
    int len;
    printf("enter a Prefix expression for evaluation\n");
    scanf("%s",s);
    len=strlen(s);
    eval(s,len-1);
    return 0;
}
