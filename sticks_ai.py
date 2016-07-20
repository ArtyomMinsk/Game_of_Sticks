from random import randrange

def valid_sticks_check(original_number_sticks):
    if original_number_sticks < 10 or original_number_sticks > 100:
        print("Out of range! Please enter a number between 10 and 100.")
        return False
    else:
        #print("in range")
        return True

def amount_of_sticks_input():
    while True:
        original_number_sticks = int(input("Please input the number of sticks within the range of (10 - 100): "))

        if valid_sticks_check(original_number_sticks):
            #print(original_number_sticks)
            return original_number_sticks

def valid_input_from_player(player_input):
    if player_input < 1 or player_input > 3:
        print("Out of range! Please enter a number between 1 and 3.")
        return False
    else:
        #print("in range")
        return True

def player_takes_out_sticks(player):
    while True:
        player_input = int(input("Player {}: How many sticks do you take (1-3)? ".format(player)))

        if valid_input_from_player(player_input):
            #print(player_input)
            return player_input

def update_num_sticks(sticks_left, player_sticks):
    while True:
        if valid_input_from_player(player_sticks) and player_sticks <= sticks_left:
            sticks_left -= player_sticks
            return sticks_left
        else:
            print("You can't take more than there is left!")
            print("There are {} sticks left.".format(sticks_left))
            player_sticks = int(input("Please enter a valid input: "))

def no_sticks_left(total_sticks_left):
    if total_sticks_left < 1:
        return True
    else:
        return False

def two_players_game(original_number_sticks):
    total_sticks_left = original_number_sticks

    while True:
        first_player_sticks = player_takes_out_sticks('1')
        total_sticks_left = update_num_sticks(total_sticks_left, first_player_sticks)
        print("There are {} sticks left".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Player 1, you lose.")
            break

        second_player_sticks = player_takes_out_sticks('2')
        total_sticks_left = update_num_sticks(total_sticks_left, second_player_sticks)
        print("There are {} sticks left.".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Player 2, you lose.")
            break

def init_ai_list(original_number_sticks):
    ai_list = []

    # for loop from 0 to original_number_sticks - 1
    # if original_number_sticks=10, from 0 - 9
    for index in range(1, original_number_sticks):
        tup = (index, [1, 2, 3], [])
        ai_list.append(tup)

    return ai_list

def ai_takes_out_sticks(ai_list, sticks_left):
    tup = ai_list[sticks_left - 1]
    print("tup = {}".format(tup))

    content = tup[1]
    print("content = {}".format(content))
    beside = tup[2]
    print("beside = {}".format(beside))

    random_index = randrange(0, len(content))
    print("random_index = {}".format(random_index))

    random_choice = content[random_index]
    print("random_choice = {}".format(random_choice))

    content.pop(random_index)
    beside.append(random_choice)

    tup_updated = (tup[0], content, beside)
    ai_list[sticks_left - 1] = tup_updated

    return (ai_list, random_choice)

# This function will updated the ai_list when the AI wins.
# Function must look through each entry in ai_list, and check beside [].
# If beside is NOT empty, move the contents of beside [] back into content [] twice.
# Remove entry from beside [].
def update_win_ai_list(ai_list):
    updated_ai_list = ai_list

    return updated_ai_list

# This function will update the ai_list when the AI looses.
# Function must look through each entry in ai_list and check beside [].
# If beside is NOT empty, then check if beside entry is inside content [].
# If yes, drop beside entry. If no, put it back into content [].
def update_loose_ai_list(ai_list):
    updated_ai_list = ai_list

    return updated_ai_list

def player_vs_ai_game(original_number_sticks, hat_list):
    total_sticks_left = original_number_sticks
    ai_list = hat_list

    while True:
        player_sticks = player_takes_out_sticks('human')
        total_sticks_left = update_num_sticks(total_sticks_left, player_sticks)
        print("There are {} sticks left".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Human, you lose.")
            return ai_list
            #REPLACE WITH
            #return update_win_ai_list(ai_list)
            #

        # This function returns (updated_ai_list, ai_takes_sticks)
        ai_return = ai_takes_out_sticks(ai_list, total_sticks_left)
        print(ai_return)

        total_sticks_left -= ai_return[1]
        print("There are {} sticks left.".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("AI, you lose.")
            return ai_list
            #REPLACE WITH
            #return update_loose_ai_list(ai_return[0])
            #

# This is the main function where Game starts
def main():
    print("Welcome to the Game of Sticks!")

    num_sticks = amount_of_sticks_input()

    print("Options:\n  Play against a friend (1)\n  Play against the computer (2)")
    option = int(input("Which option do you take (1-2)? "))
    while option != 1 and option != 2:
        option = int(input("Please input (1) or (2) only: "))

    ai_hat_list = init_ai_list(num_sticks)
    print("Initial AI list is: {}".format(ai_hat_list))

    while True:
        if option == 1:
            two_players_game(num_sticks)
        elif option == 2:
            ai_hat_list = player_vs_ai_game(num_sticks, ai_hat_list)

        repeat = input("Would you like to play again? y/n: ").lower()

        if repeat == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    main()
