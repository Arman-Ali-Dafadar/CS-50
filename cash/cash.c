#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed(in cents)");
    }
    while (change <= 0);
    int no_of_quarters = (change / 25);
    change = change - (no_of_quarters * 25);
    int no_of_dimes = (change / 10);
    change = change - (no_of_dimes * 10);
    int no_of_nickels = (change / 5);
    change = change - (no_of_nickels * 5);
    int total_coins = (no_of_quarters + no_of_dimes + no_of_nickels + change);
    printf("%i\n", total_coins);
}
