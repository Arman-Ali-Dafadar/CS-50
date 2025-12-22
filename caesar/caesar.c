#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc==2)
    {
        int key= atoi(argv[1]);
        string plain_text = get_string("plaintext:  ");
        printf("ciphertext: ");
        int n = strlen(plain_text);
        for (int i=0;i<n;i++)
        {
            char c = plain_text[i];
            if (isupper(c))
            {
                c = (c - 'A' + key) % 26 + 'A';
                printf("%c",c);
            }
            else if (islower(c))
            {
                c = (c - 'a' + key) % 26 + 'a';
                printf("%c",c);
            }
            else
            {
                printf("%c",c);
            }
        }
        printf("\n");
    }
    else
    {
        printf("usage: ./caesar key\n");
        return 1;
    }
}
