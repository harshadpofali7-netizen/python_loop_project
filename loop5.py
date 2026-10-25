#Mini project 5 : Number guessing game
SECRET_NUMBER = 37
max_attempts = 5
attempts_used = 0
has_won = False
print("=== Welcome to the number guessing game! ===")
print(f"I am thinking of a number. You have {max_attempts} attempts to guess it.")
while attempts_used < max_attempts:
    guess = int(input(f"\nAttempt {attempts_used + 1}/{max_attempts} - Enter your guess: "))
    attempts_used += 1
    if guess == SECRET_NUMBER:
        print("Correct! You found it!")
        has_won = True
        break
    elif guess < SECRET_NUMBER:
        print("Hint: Too low")
    else:
        print("Hint: Too high")
print("\n=======================================")
print("             GAME OVER                   ")
print("=========================================")
print(f"Win/lose message: {'Congratulations, you won!' if has_won else 'Sorry, you lost!'}")
print(f"attempts used  : {attempts_used}")
if not has_won:
    print(f"The secret number was: {SECRET_NUMBER}")
print("================================")
