from sticks import number_of_original_input_sticks_check
from sticks import number_of_input_sticks_from_player_check

def test_number_of_original_sticks_input():
    input_1 = 50
    input_2 = 150

    assert number_of_original_input_sticks_check(input_1) == True
    assert number_of_original_input_sticks_check(input_2) == False

def test_number_of_sticks_input():
    input_1 = 2
    input_2 = 5

    assert number_of_input_sticks_from_player_check(input_1) == True
    assert number_of_input_sticks_from_player_check(input_2) == False
