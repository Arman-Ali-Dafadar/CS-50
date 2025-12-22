#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    uint8_t buffer[512];
    int counter = 0;
    FILE *current_img = NULL;
    char filename[8];

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 &&
            buffer[3] <= 0xef)
        {
            if (current_img != NULL)
            {
                fclose(current_img);
            }

            sprintf(filename, "%03i.jpg", counter);
            current_img = fopen(filename, "w");
            if (current_img == NULL)
            {
                printf("Could not create %s.\n", filename);
                fclose(card);
                return 3;
            }
            counter++;
        }

        if (current_img != NULL)
        {
            fwrite(buffer, 1, 512, current_img);
        }
    }
    if (current_img != NULL)
    {
        fclose(current_img);
    }
    fclose(card);

    return 0;
}
