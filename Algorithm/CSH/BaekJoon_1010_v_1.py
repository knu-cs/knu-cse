def building_bridge():
    test_case_count = int(input())
    bridge_counts = []
    for _ in range(test_case_count):
        site_count = list(map(int, input().split()))
        a = factorial(site_count[0])
        b = factorial(site_count[1]) / factorial(site_count[1] - site_count[0])
        bridge_count = int(b / a)
        bridge_counts.append(bridge_count)
    return bridge_counts


def factorial(number):
    factorial_result = 1
    for n in range(1, number + 1):
        factorial_result *= n
    return factorial_result


if __name__ == '__main__':
    bridges = building_bridge()
    for bridge in bridges:
        print(bridge)
