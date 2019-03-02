#The print_menu() function prints the menu for the palindrome program
def print_menu():
    print("1. Is it a Palindrome?\n2. Make a Palindrome!\n3. Quit")
#The get_menu_choice() function prompts the user to choose an option from the menu
#A while loop is used to validate that the user chooses 1, 2, or 3
def get_menu_choice():
    menu_choice = int(input("Choose an option from the menu: "))
    while True:
        if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
            return menu_choice
        else:
            menu_choice = int(input("Please select an option from our menu using the numbers 1, 2, or 3: "))
#The get_phrase() function confirms that the user enters a phrase with at least one character
#A while loop is used to validate that the phrase contains at least one character
def get_phrase():
    phrase = input("Please enter an English phrase: ")
    while True:
            if len(phrase) != 0:
                return phrase
            else:
                phrase = input("Please enter an English phrase: ")
#The is_palindrome(phrase) function contains a loop used for phrases that contain non-alphabetical characters
#The loop is made to essentially skip over any non-alphabetical characters, that way the phrase can be compared
#as if it contained only alphabetical characters
def is_palindrome(phrase):
    phrase = phrase.lower()
    i = 0
    j = len(phrase) - i - 1
    while i < len(phrase) // 2:
        if phrase[i].isalpha() == True:
            i += 0
        elif (phrase[i + 1]).isalpha() == False:
            i += 2
        elif phrase[i].isalpha() == False:
            i += 1
        if phrase[j].isalpha() == True:
            i -= 0
        elif (phrase[j - 1]).isalpha() == False:
            j -= 2
        elif phrase[j].isalpha() == False:
            j -= 1
        if phrase[i] != phrase[j]:
            return False
        i += 1
        j -= 1
    return True
#The check_menu_palindrome() function will notify the user if their phrase is a palindrome or not
#Uses boolean values to check whether their phrase is a palindrome or not
def check_menu_palindrome():
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
    if palindrome == True:
        print('"{}"'.format(phrase) , "is a palindrome!")
    elif palindrome == False:
        print('"{}"'.format(phrase) , "is not a palindrome.")
#The get_repeat_last() function asks the user if they would like to repeat the last letter of their phrase
#A while loop is used to validate that they entered yes or no
def get_repeat_last():
    skip_last = input("Should the last letter be repeated? y/n: ")
    while True:
        if skip_last == "y":
            return True
        elif skip_last == "n":
            return False
        else:
            skip_last = input("Should the last letter be repeated? y/n: ")
#The make_palindrome(phrase, skip_last) function creates a palindrome based off of the user's phrase
#Uses two loops that iterates through the phrase, appending the reversed phrase to the end of the original phrase
def make_palindrome(phrase, skip_last):
    if skip_last == True:
        rev = ""
        for i in range(len(phrase) - 1 , -1 , -1):
            rev = rev + phrase[i]
        phrase = phrase + rev
        return phrase
    elif skip_last == False:
        rev = ""
        for i in range(len(phrase) - 2 , -1 , -1):
            rev = rev + phrase[i]
        phrase = phrase + rev
        return phrase
#The menu_make_palindrome() function displays to the user what their new palindrome is
def menu_make_palindrome():
    phrase = get_phrase()
    skip_last = get_repeat_last()
    palindrome = make_palindrome(phrase, skip_last)
    print('"{}"'.format(phrase) , "made into a palindrome is" , '"{}"'.format(palindrome))
#The main() function executes the program
#A while loop enables the program to run until the user selects to quit
def main():
    menu = print_menu()
    menu_choice = get_menu_choice()
    while True:
        if menu_choice == 1:
            palindrome = check_menu_palindrome()
            menu = print_menu()
            menu_choice = get_menu_choice()
        elif menu_choice == 2:
            palindrome = menu_make_palindrome()
            menu = print_menu()
            menu_choice = get_menu_choice()
        else:
            print("Bye!")
            break

main()