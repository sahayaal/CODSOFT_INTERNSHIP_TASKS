import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Main game function
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock-Paper-Scissors ---")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Type 'exit' to quit the game.")
        
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice == 'exit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Display the current scores
        print(f"Current Scores -> You: {user_score} | Computer: {computer_score}")
        
        # Ask the user if they want to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing! Final Scores -> You: {} | Computer: {}".format(user_score, computer_score))

# Run the game
if __name__ == "__main__":
    play_game()
