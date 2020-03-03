secret_word = "University"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

#promt the user to input the secret word (catch: we want the user to enter the secret word, but if they don't guess
# it correctly we want to promt them to enter it again.)

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")
