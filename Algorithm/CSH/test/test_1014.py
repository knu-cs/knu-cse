import timeit
from unittest.mock import patch

from CSH.BJ1014 import conning


def test_quitting():
    try:
        ans_right = [4, 1, 2, 46]
        with patch('builtins.input', side_effect=[
            '4',
            '2 3',
            '...',
            '...',
            '2 3',
            'x.x',
            'xxx',
            '2 3',
            'x.x',
            'x.x',
            '10 10',
            '....x.....',
            '..........',
            '..........',
            '..x.......',
            '..........',
            'x...x.x...',
            '.........x',
            '...x......',
            '........x.',
            '.x...x....'
        ]):
            assert conning() == ans_right;
            print('Success')
    except AssertionError:
        print('Failed')


t = timeit.timeit('test_quitting()', setup='from __main__ import test_quitting', number=1)
print(t)
