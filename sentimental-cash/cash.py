from cs50 import get_float

while True:
    change = get_float("Change: ")
    if change > 0:
        break
change = int(change * 100)
no_of_quarters = change // 25
change = change - (25 * no_of_quarters)
no_of_dimes = change // 10
change = change - (10 * no_of_dimes)
no_of_nickels = change // 5
change = change - (5 * no_of_nickels)
no_of_pennies = change // 1
total_coins = no_of_quarters + no_of_dimes + no_of_nickels + no_of_pennies
print(total_coins)
