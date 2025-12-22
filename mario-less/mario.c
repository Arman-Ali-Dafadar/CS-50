#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Enter the height? :");
    }
    while (height <= 0);
    for (int j = 1; j <= height; j++)
    {
        for (int s = 0; s < height - j; s++)
        {
            printf(" ");
        }
        for (int i = 0; i < j; i++)
        {
            printf("#");
        }
        printf("\n");
    }
}
