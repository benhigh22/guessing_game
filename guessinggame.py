

secret_num = 70
close_num_low = [65, 66, 67, 68, 69]
close_num_hi = [71, 72, 73, 74, 75]

for _ in range(5):
    print ("Attempt number " + str(_ + 1))

    try:
        guess = int(input("Guess the number between 1 and 99 "))

        if guess < 1:
            print ("Incorrect entry, number must be between 1 and 99")

        elif guess > 99:
            print ("Incorrect entry, number must be between 1 and 99")

        elif guess == secret_num:
            print ("You've got it! The number is 70!")
            break

        elif guess in close_num_low and _ == 3:
            print ("You're so close, a little higher, but only one more guess!")

        elif guess in close_num_hi and _ == 3:
            print ("You're so close, a little lower, but only one more guess!")

        elif guess in close_num_low and _ == 4:
            print ("You were so close, but you're out of guesses! The number was 70.")

        elif guess in close_num_hi and _ == 4:
            print ("You were so close, but you're out of guesses! The number was 70.")

        elif guess in close_num_low:
            print ("You're so close, a little higher!")

        elif guess in close_num_hi:
            print ("You're so close, a little lower!")

        elif _ == 3 and (guess > secret_num):
            print ("Too high, only one more chance")

        elif _ == 3 and (guess < secret_num):
            print ("Too low, only one more chance")

        elif _ == 4:
            print ("Sorry, out of guesses. The number was 70")

        elif guess > secret_num:
            print ("Too high, guess again")

        elif guess < secret_num:
            print ("Too low, guess again")


    except ValueError:
        print ("Incorrect entry, guess must be a number.")








