import random
money = 100
wins = 0
losses = 0
while money > 0:
    print("Computer thinks a number from 1 to 100")
    comp_number = random.randint(1, 100)
    level = int(input("choose level [1,2,3]? "))
    times = 10 if level == 1 else 5 if level == 2 else 3
    is_win = False
    money -= 5
    for time in range(times):
        your_num = int(input("Enter your guessing number #" + str(time + 1) + ": "))
        if your_num == comp_number:
            is_win = True
            break
        else:
            if your_num < comp_number:
                print("too low!")
            else:
                print("too high!")
    if is_win:
        print("You are Genius!!!!")
        wins += 1
        money += 10
    else:
        print("-------------------------")
        print("Game over! The number was:", comp_number)
        losses += 1
    print("-------------------------")
    print(f"Money left: ${money}")
    print(f"Wins: {wins}, Losses: {losses}")
    print("-------------------------")
    if money <= 0:
        print("You lost all your money! Game Over")
        break
    cont = input("Dare you to play [y/n]: ")
    if cont.lower() == 'n':
        break
print(f"Money left: ${money}")
print(f"Total Wins: {wins}")
print(f"Total Losses: {losses}")

