from sticks import valid_sticks_check
from sticks import valid_input_from_player
from sticks import update_num_sticks
from sticks import no_sticks_left


def test_valid_sticks_check():
    input_0 = 0
    input_1 = 50
    input_2 = 150

    assert valid_sticks_check(input_0) == False
    assert valid_sticks_check(input_1) == True
    assert valid_sticks_check(input_2) == False


def test_valid_input_from_player():
    input_0 = 0
    input_1 = 2
    input_2 = 5

    assert valid_input_from_player(input_0) == False
    assert valid_input_from_player(input_1) == True
    assert valid_input_from_player(input_2) == False


def test_update_num_sticks():
    sticks_left = 5
    player_sticks = 3

    assert update_num_sticks(sticks_left, player_sticks) == 2


def test_no_sticks_left():
    assert no_sticks_left(0) == True
    assert no_sticks_left(-1) == True
    assert no_sticks_left(1) == False
