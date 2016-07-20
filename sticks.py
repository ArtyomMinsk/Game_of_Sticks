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

def no_sticks_left(total_sticks_left):
    if total_sticks_left < 1:
        return True
    else:
        return False

# This is the main function where Game starts
def main():
    print("Welcome to the Game of Sticks!")

    num_sticks = amount_of_sticks_input()
    two_players_game(num_sticks)

if __name__ == '__main__':
    main()
