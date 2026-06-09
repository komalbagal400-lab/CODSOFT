import random

user_score = 0
computer_score = 0

while True:
    print("\n--- ROCK PAPER SCISSORS GAME ---")
    print("Choose: rock, paper, or scissors")

    user = input("Your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    elif user in choices:
        print("Computer Wins!")
        computer_score += 1

    else:
        print("Invalid Choice!")
        continue

    print("\nScore:")
    print("You =", user_score)
    print("Computer =", computer_score)

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score:")
        print("You =", user_score)
        print("Computer =", computer_score)
        print("Thanks for playing!")
        break