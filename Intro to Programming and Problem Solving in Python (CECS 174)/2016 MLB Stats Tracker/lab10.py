def read_players(file_name):  # Reads the player's data into a tuple
    result = []

    first_line = True

    for line in open(file_name):
        if first_line:
            first_line = False
            continue

        # read: Name=0, Team=1, AB=3, HR=9
        split_line = line.split(",")
        # strip('"')

        player = (split_line[0].strip('"'), split_line[1].strip('"'), \
                  int(split_line[3].strip('"')), int(split_line[9].strip('"')), float(split_line[21].strip('"')))
        result.append(player)

    return result

def main():  # Allows the program to run, user can enter their desired function
    all_players = read_players("baseball_players.csv")
    choice = 0
    while choice != 5:
        print("1. Search for player")
        print("2. Search for team")
        print("3. Find player with highest homeruns")
        print("4. Find player with highest batting average")
        print("5. Quit")

        choice = int(input("Enter a choice: "))
        if choice == 1:
            search_for_player(all_players)
        elif choice == 2:
            search_for_team(all_players)
        elif choice == 3:
            find_max_hrs(all_players)
        elif choice == 4:
            find_highest_avg(all_players)
        elif choice == 5:
            print("\nThank you for using this 2016 MLB Stats Tracker.\nGoodbye!")

def print_player(player):  # Prints the player's statistics
    (name, team, ab, hr, avg) = player
    print("{0} ({1}): {2} AB, {3} HR, {4} AVG".format(name, team, ab, hr, avg))


def find_max_hrs(
        all_players):  # Searches through the file of players, returns the player with the highest amount of home runs


    home_run = 0
    for player in all_players:
        (name, team, ab, hr, avg) = player
        if hr > home_run:
            home_run = hr
    for player in all_players:
        if player[3] == home_run:
            print_player(player)


def search_for_team(all_players):  # Searches for all players on the user's inputted team
    search_team = input("Please enter a team's name: ")

    for player in all_players:
        (name, team, ab, hr, avg) = player
        if team == search_team:
            print_player(player)


def search_for_player(all_players):  # Searches for a player in the list that the user inputted
    search_name = input("Please enter a player's name: ")

    for player in all_players:
        (name, team, ab, hr, avg) = player
        if name == search_name:
            print_player(player)
            break


def find_highest_avg(all_players):  # Searches for the player with the highest avg


    average = 0
    for player in all_players:
        (name, team, ab, hr, avg) = player
        if ab < 100:
            continue
        if avg > average:
            average = avg
    for player in all_players:
        if player[4] == average:
            print_player(player)
main()