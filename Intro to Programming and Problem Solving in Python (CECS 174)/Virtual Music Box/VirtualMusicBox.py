#Musicbox module is imported so that the program may produce notes
import musicbox
#Four global lists are created that contain notes, their integer values, and how they scale up in a major or minor scale
NOTE_LETTERS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NOTE_NUMBERS = [60, 62, 64, 65, 67, 69, 71]
MAJOR_SCALE_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALE_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
#This statement calls the musicbox module and produces a piano sound
my_music = musicbox.MusicBox(0)

#The note_to_int function takes an argument, note, and determines its integer value
#Uses only 5 if/elif/else statements
#Uses .index and list indexing to obtain a result
def note_to_int(note):
    note_position = 0
    note_number = 0
    if note[0] in NOTE_LETTERS and (len(note) == 1):                                                  #1 if/elif/else
        note_position = NOTE_LETTERS.index(note)
        note_number = NOTE_NUMBERS[note_position]
        return note_number
    elif (note[0] in NOTE_LETTERS and (len(note) == 2)) and ((note[1] == '#') or (note[1] == 'b')):   #2 if/elif/else
        note_position = NOTE_LETTERS.index(note[0])
        note_number = NOTE_NUMBERS[note_position]
        if note[1] == '#':                                                                            #3 if/elif/else
            return (note_number + 1)
        elif note[1] == 'b':                                                                          #4 if/elif/else
            return (note_number - 1)
    else:                                                                                             #5 if/elif/else
        return -1

#The note_to_scale(note, type) function creates a list starting with the user inputted note at index 0, then 7 more values are appended
#to the list to create a major or minor scale, again based on the user's input
#Uses for loop and .appened to obtain result
def note_to_scale(note, type):
    scale = []
    if type == 'major':
        scale.append(note)
        for i in MAJOR_SCALE_INTERVALS:
            note += i
            scale.append(note)
        return scale
    elif type == 'minor':
        scale.append(note)
        for i in MINOR_SCALE_INTERVALS:
            note += i
            scale.append(note)
        return scale
    else:
        return False

#The print_menu() function prints the menu to the user
def print_menu():
    print("Main Menu:\n1. Play notes\n2. Play Scale\n3. Quit")

#The get_menu_choice() function obtains a user input and determines what function they'd like to use based on their input
#Uses .isdigit in case the user inputs a nonalphanumeric character
def get_menu_choice():
    menu_choice = int(input("Please enter a selection: "))
    while True:
        if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
            return menu_choice
        else:
            menu_choice = int(input("Please enter a selection from the menu using the numbers 1, 2, or 3: "))

#The get_notes() function will create a list based off the user's input using .split
#Only returns notes found in NOTE_LETTERS
def get_notes():
    notes = []
    note = 0
    user_notes = input('Please enter a sequence of notes separated by spaces: ')
    note_list = user_notes.split(" ")
    for note in note_list:
        note = note_to_int(note)
        if note != -1:
            notes.append(note)
    return notes

#The function play_notes(notes) will play notes if the user chooses to use function 1 of the program
def play_notes(notes):
    for i in notes:
        play_some_notes = my_music.play_note(i, 500)

#The function menu_play_notes() calls get_notes() to validate the user's notes and make sure they exist
#Also, it calls play_notes(notes) to play the user's notes
def menu_play_notes():
    notes = get_notes()
    if len(notes) == 0:
        print("I don't know any of those notes.")
    else:
        notes = play_notes(notes)

#The function get_scale() will validate the user's inputted scale and determine if it exists
#Uses len() and slicing to achieve its goal
def get_scale(): #length of string will always be either 7 "C major"(for no sharp/flat) or 8 "C# major"(for sharp/flat)
    while True:
        scale_name = input("Please enter a scale name (Ex. C major): ")
        if ((len(scale_name) == 7)) and ((scale_name[2:7] == 'major') or (scale_name[2:7] == 'minor')):
            note = scale_name[0]
            new_note = note_to_int(note)
            if new_note != -1:
                return scale_name
        elif ((len(scale_name) == 8)) and ((scale_name[3:8] == 'major') or (scale_name[3:8] == 'minor')):
            note = scale_name[0:2]
            new_note = note_to_int(note)
            if new_note != -1:
                return scale_name

#The function play_scale(scale) will pkay the notes in a user's scale
def play_scale(scale):
    for i in scale:
        play_a_scale = my_music.play_note(i, 500)

#The function menu_play_scale() calls multiple functions to create a list of notes based on the user's inputted scale
#Once the input is validated and constructed into a list, the play_scale(function) plays each note in the list
def menu_play_scale():
    new_scale = 0
    scale = get_scale()
    scale = scale.split(" ")
    note = scale[0]
    new_note = note_to_int(note)
    scale[0] = new_note
    new_scale = note_to_scale(scale[0], scale[1])
    scale = new_scale
    scale = play_scale(scale)

#A main() function is created to enable the program to run forever
#It implements all three functions of the program
def main():
    menu = print_menu()
    menu_choice = get_menu_choice()
    while True:
        if menu_choice == 1:
            play_the_notes = menu_play_notes()
            menu = print_menu()
            menu_choice = get_menu_choice()
        elif menu_choice == 2:
            play_the_scale = menu_play_scale()
            menu = print_menu()
            menu_choice = get_menu_choice()
        else:
            print("\nThank you for using this virtual music box.\nGoodbye!")
            break
main()
my_music.close()