def building_bridge():
    test_case_count = int(input())
    bridge_counts = []
    for _ in range(test_case_count):
        site_count = list(map(int, input().split()))
        mul_M = 1
        mul_N = 1
        for M_site_num in range(site_count[1], site_count[1]-site_count[0], -1):
            mul_M *= M_site_num
        for N_site_num in range(1, site_count[0]+1):
            mul_N *= N_site_num
        bridge_counts.append(int(mul_M / mul_N))
    for bridge_count in bridge_counts:
        print(bridge_count)
    return bridge_counts

#building_bridge()

from unittest.mock import patch
import timeit

def test_quitting():
    try:
        ans_right = [1, 5, 67863915]
        with patch('builtins.input', side_effect=["3",
                                                  "2 2",
                                                  "1 5",
                                                  "13 29"]):
            assert building_bridge() == ans_right; print('Success')
    except AssertionError:
        print('Failed')


t = timeit.timeit('test_quitting()', setup='from __main__ import test_quitting', number=1)
print(t)