from sticks_ai import init_ai_list
from sticks_ai import update_win_ai_list
from sticks_ai import update_loose_ai_list

def test_ai_data_structure_initiation():

    data = [(1, [1, 2, 3], []),
            (2, [1, 2, 3], []),
            (3, [1, 2, 3], []),
            (4, [1, 2, 3], []),
            (5, [1, 2, 3], []),
            (6, [1, 2, 3], []),
            (7, [1, 2, 3], []),
            (8, [1, 2, 3], []),
            (9, [1, 2, 3], [])]

    assert init_ai_list(10) == data

def test_update_ai_data_structure_after_AI_wins():

    data_before = [(1, [1, 2, 3], []),
                    (2, [1, 2, 3], []),
                    (3, [2, 3, 1], []),
                    (4, [3, 2, 2], [1]),
                    (5, [1, 3, 2], []),
                    (6, [1, 2, 3], []),
                    (7, [1, 3, 2], [2]),
                    (8, [1, 2, 3], []),
                    (9, [2, 3, 1], [1])]

    updated_data = [(1, [1, 2, 3], []),
                    (2, [1, 2, 3], []),
                    (3, [2, 3, 1], []),
                    (4, [3, 2, 2, 1, 1], []),
                    (5, [1, 3, 2], []),
                    (6, [1, 2, 3], []),
                    (7, [1, 3, 2, 2, 2], []),
                    (8, [1, 2, 3], []),
                    (9, [2, 3, 1, 1, 1], [])]

    assert update_win_ai_list(data_before) == updated_data

def test_update_ai_data_structure_after_AI_loses():

    data_before = [(1, [1, 2, 3], []),
                    (2, [1, 2], [3]),
                    (3, [1, 2, 3], []),
                    (4, [1, 2, 3], []),
                    (5, [1, 3], [2]),
                    (6, [1, 2, 3], []),
                    (7, [2, 3], [1]),
                    (8, [1, 2, 3], []),
                    (9, [1, 2, 3], [])]

    updated_data = [(1, [1, 2, 3], []),
                    (2, [1, 2, 3], []),
                    (3, [1, 2, 3], []),
                    (4, [1, 2, 3], []),
                    (5, [1, 3, 2], []),
                    (6, [1, 2, 3], []),
                    (7, [2, 3, 1], []),
                    (8, [1, 2, 3], []),
                    (9, [1, 2, 3], [])]

    assert update_loose_ai_list(data_before) == updated_data
