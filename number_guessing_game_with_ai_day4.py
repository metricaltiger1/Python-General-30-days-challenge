import random
user_feedback = ("higher", "lower", "correct")
is_guess_correct = True
continue_playing = True

print("Hello! Welcome to Number Guessing Game with AI")

def ai_gauss_to_user(response):
    if response == user_feedback[0]:
        return random.randint(comp_gauss + 1, 100)
    elif response == user_feedback[1]:
        return random.randint(1, comp_gauss - 1)
    else:
        return comp_gauss


def user_feedback_to_ai(response):
    if response == "1":
        return user_feedback[0]
    elif response == "2":
        return user_feedback[1]
    elif response == "3":
        return user_feedback[2]
    else:
        return "invalid input"


while continue_playing:
    print("Think of a number between 1 and 100. The computer will try to guess it.")

    comp_attempts = 1
    is_guess_correct = True
    comp_gauss = random.randint(1, 100) 

    while is_guess_correct:
        print(f"Computer's guess: {comp_gauss}")
        try:
            user_response = int(input("Is your number higher, lower, or correct (respond with 1, 2, or 3)? "))
            feedback = user_feedback_to_ai(str(user_response))
            if feedback == "invalid input":
                print("Invalid input, please respond with 1, 2, or 3.")
                continue

            if feedback == user_feedback[2]:  # Correct gauss
                is_guess_correct = False
                break

            comp_gauss = ai_gauss_to_user(feedback)
            comp_attempts += 1
        except ValueError:
            print("Invalid input, please enter integers only.")
            continue

    print(f"Hooray! The computer guessed your number in {comp_attempts} attempts.")

    while True:  
        user_continue_playing = input("Continue playing? (yes or no): ").strip().lower()
        if user_continue_playing == "yes":
            continue_playing = True
            print("New game started!")
            break 
        elif user_continue_playing == "no":
            continue_playing = False
            print("Goodbye! Thanks for playing!")
            break 
        else:
            print("Invalid input! Enter 'yes' or 'no' to continue.")
