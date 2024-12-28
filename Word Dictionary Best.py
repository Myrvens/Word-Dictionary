# Importing the PyDictionary class from the PyDictionary module
from PyDictionary import PyDictionary

# Creating an instance of the PyDictionary class
dictionary = PyDictionary()

# Starting an infinite loop for the word lookup functionality
while True:
    # Prompting the user to enter a word
    word = input("Enter your word: ")
    
    # Breaking the loop if the user input is empty
    if word == "":
        break

    # Fetching and printing the meaning of the entered word
    print(dictionary.meaning(word))
