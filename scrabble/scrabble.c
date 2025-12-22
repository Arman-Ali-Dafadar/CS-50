#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int scrubble(string player);
int values[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");

    int player_1_score = scrubble(player_1);
    int player_2_score = scrubble(player_2);

    if (player_1_score > player_2_score)
    {
        printf("Player 1 win!\n");
    }
    else if (player_1_score < player_2_score)
    {
        printf("Player 2 win!\n");
    }
    else
    {
        printf("Tie\n");
    }
}

int scrubble(string player)
{
    int score = 0;

    for (int i = 0, len = strlen(player); i < len; i++)
    {
        if (isupper(player[i]))
        {
            score += values[player[i] - 'A'];
        }
        else if (islower(player[i]))
        {
            score += values[player[i] - 'a'];
        }
    }
    return score;
}
