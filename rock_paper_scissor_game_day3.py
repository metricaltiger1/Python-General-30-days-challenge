import random

# ASCII Art for the game
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Choices
game_choices = ("rock", "paper", "scissors")

# 5
# to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

# Main Game 
def play_game():
    print("Welcome to the Rock, Paper, Scissors game!")
    
    # Initialize scores
    player_score = 0
    computer_score = 0

    # Ask for the "best of" mode
    while True:
        try:
            best_of = int(input("\nEnter the number of rounds to win (best of 3 or 5): "))
            if best_of % 2 == 0 or best_of < 1:
                print("Please enter an odd number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    rounds_to_win = (best_of // 2) + 1

    # Main game loop
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        # Random computer choice
        computer_choice = random.choice(game_choices)

        # Get player's choice
        print("\nChoices: 1 - Rock, 2 - Paper, 3 - Scissors")
        player_input = input("Enter your choice (1/2/3 or 'quit' to exit): ").strip()
        
        if player_input.lower() == "quit":
            print("Thanks for playing!")
            break
        
        if player_input not in ("1", "2", "3"):
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue
        
        # Convert player input to choice
        player_choice = game_choices[int(player_input) - 1]

        # Display choices
        print("\nYou chose:")
        print(ascii_art[player_choice])
        print("\nComputer chose:")
        print(ascii_art[computer_choice])

        # Determine the winner
        result = determine_winner(player_choice, computer_choice)

        if result == "draw":
            print("It's a draw!")
        elif result == "player":
            print("You win this round! 🎉")
            player_score += 1
        else:
            print("Computer wins this round! 😢")
            computer_score += 1

        # Display scores
        print(f"Scores -> Player: {player_score}, Computer: {computer_score}")

    # Final results
    if player_score > computer_score:
        print("\n🎉 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("\n😢 Oh no! The computer won the game!")
    print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
    print("Thanks for playing!")

# Run the game
play_game()
