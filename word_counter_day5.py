import re
def count_characters_with_spaces(word):
    return len(word)

def count_characters_without_spaces(word):
    return len(word.replace(' ', ''))

def count_words(word):
    words = word.split()
    return len(words)

def count_sentences(word):
    # Split by '.', '?', or '!'
    sentences = re.split(r'[.?!]', word)
    # Remove empty strings after splitting
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


is_done= True

while is_done:
    user_input= str(input("Enter your sentence: ")).strip()

    
    if user_input != '':

        print(f"Number of characters (excluding spaces): {count_characters_without_spaces(user_input)}")

        print(f"Number of characters (including spaces): {count_characters_with_spaces(user_input)}")

        print(f"Total words: {count_words(user_input)}")

        print(f"Total sentences: {count_sentences(user_input)}")
        
        while True:
            user_choice = str(input("Would you like to keep analysis of your words? (y/n): ")).lower()
            if user_choice=='y':
               break
            elif user_choice == 'n':
                is_done = False
                print("Thank you for using the word counter!")
                break
            else:
                print(" Please enter y or n.")
        
    else:
        print("Please enter a sentence.")
 

    