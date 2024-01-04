
def count_words(text):
    """Counts the number of words in a given text."""

    word_count = len(text.split())
    return word_count

# Get user input
while True:
    try:
        user_input = input("Enter a sentence or paragraph: ")

        # Handling empty and non-string input
        if not user_input:
            print("Please enter some text.")
            continue
        elif not isinstance(user_input, str):
            print("Invalid input type. Please enter text only.")
            continue

        # Count words
        word_count = count_words(user_input)

        # Print word count
        print("Word count:", word_count)

        # Ask if the user wants to continue
        choice = input("Do you want to count words in another text? (y/n): ")
        if choice.lower() != 'y':
            break

    except Exception as e:
        print("An error occurred: {}".format(e))
        