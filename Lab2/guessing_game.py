import random

def number_guessing_game():
    target = random.randint(1, 100)
    max_attempts = 7
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")
    
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
        
        if guess == target:
            print(f"Congratulations! You guessed the number correctly in {attempt} attempts.")
            return
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")
            
    print(f"Game Over! You ran out of attempts. The correct number was {target}.")

if __name__ == "__main__":
    number_guessing_game()