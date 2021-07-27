def factorial(number):
    factorial_result = 1
    for n in range(1, number + 1):
        factorial_result *= n
    return factorial_result


test_case = int(input())
results = []

for i in range(test_case):
    left_site, right_site = map(int, input().split())
    results.append(factorial(right_site) // (factorial(left_site) * factorial(right_site - left_site)))

for result in results:
    print(result)
