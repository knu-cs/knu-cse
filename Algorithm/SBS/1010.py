def factorial(number):
    factorial_result = 1
    for n in range(1, number + 1):
        factorial_result *= n
    return factorial_result


test_case = int(input())
results = []

for i in range(test_case):
    a, b = map(int, input().split())
    results.append(factorial(b) // (factorial(a) * factorial(b - a)))

for result in results:
    print(result)
