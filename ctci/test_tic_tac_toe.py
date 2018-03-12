from tic_tac_toe import *

def test_winner():
    winner = '111      '
    assert won(winner)

def test_diagonal():
    winner = '1   1   1'
    assert won(winner)

def test_loser():
    loser = '1 1  1 2 '
    assert not won(loser)

