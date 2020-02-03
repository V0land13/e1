import pytest
from visilica import letter_check

# Тест функции letter_check
word = 'giriotgot'
letterYes = 'i'
letterNo = 'f'
result1Pass = (True, [1, 3])
def test_lc_yes():
    result1 = letter_check(letterYes, word)
    assert result1 == result1Pass

def test_lc_no():
    result2 = letter_check(letterNo, word)
    assert result2[0] == False
