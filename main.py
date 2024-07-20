import random
def number_guessing_game():
  """Plays a number guessing game with the user."""
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1, 100)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    attempts = 10
  else:
    attempts = 5
  print(f"You have {attempts} attempts to guess the number.")
  for attempt in range(attempts):
    print(f"You have {attempts - attempt} attempts remaining.")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
    elif guess < number:
      print("Too low.")
    else:
      print(f"You got it! The answer was {number}")
      return 
  print(f"You ran out of guesses. The answer was {number}")
number_guessing_game()