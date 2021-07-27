import timeit
from unittest.mock import patch

from CSH.BaekJoon_1010_v_1 import building_bridge


def test_quitting():
    try:
        ans_right = [1, 5, 67863915]
        with patch('builtins.input', side_effect=[
            "3",
            "2 2",
            "1 5",
            "13 29"
        ]):
            assert building_bridge() == ans_right;
            print('Success')
    except AssertionError:
        print('Failed')


t = timeit.timeit('test_quitting()', setup='from __main__ import test_quitting', number=1)
