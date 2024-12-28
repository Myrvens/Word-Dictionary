# Defining the main function
def main():
    # Creating a dictionary with words and their definitions
    word_dictionary = {
        'hi': 'a way of greeting',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in space',
    }

    # Starting an infinite loop for user input
    while True:
        # Prompting the user to enter a word
        word = input("Enter a word: ")
        
        # Breaking the loop if the input is empty
        if word == "":
            break

        # Checking if the word exists in the dictionary
        if word in word_dictionary:
            # Printing the word and its definition
            print(word, ":", word_dictionary[word])

# Calling the main function
main()
