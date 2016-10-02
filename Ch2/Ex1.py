lb = 0
hb = 100
guess = (hb + lb) // 2
msg1 = "Enter 'h' to indicate the guess is too high. "
msg2 = "Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
guessmsg = "Is your secret number "
err = "Sorry, I did not understand your input. "
victory = "Game over. Your secret number was:"
ans = ""

print("Please think of a number between 0 and 100!")
while abs(lb-hb) > 1:
    print(guessmsg+str(guess)+"?")
    ans = input(msg1 + msg2,)
    if ans == "l":
        lb = guess
        guess = (hb + lb) // 2
    elif ans == "h":
        hb = guess
        guess = (hb + lb) // 2
    elif ans == "c":
        print(victory, guess)
        break
    else:
        print(err)


