# BaekJoon 1012
# 14:34 ~ 15:40

def get_maximum_student(desc):
    sum_student = 0
    for desc_row in desc:
        sum_student += desc_row.count("o")
    return sum_student


def _print_desc(desc):
    for desc_row in desc:
        print(desc_row)


def check_cheating_possible(desc, check_matrix):
    if desc[check_matrix[0]][check_matrix[1]] == "x":
        return
    try:
        right_upper = desc[check_matrix[0] - 1][check_matrix[1] + 1]
    except IndexError as e:
        right_upper = ""
    try:
        right = desc[check_matrix[0]][check_matrix[1] + 1]
    except IndexError as e:
        right = ""
    try:
        left_upper = desc[check_matrix[0] + 1][check_matrix[1] - 1]
    except IndexError as e:
        left_upper = ""
    try:
        left = desc[check_matrix[0]][check_matrix[1] - 1]
    except IndexError as e:
        left = ""
    if right_upper == "o" or right == "o" or left_upper == "o" or left == "o":
        pass
    elif right_upper == "x" and right and "x" and left_upper and "x" and left == "x":
        desc[check_matrix[0]][check_matrix[1]] = "o"
    else:
        desc[check_matrix[0]][check_matrix[1]] = "o"
    return desc


def set_desk(row):
    desk_row = []
    for r in range(row):
        row_data = list(input())
        desk_row.append(row_data)
    return desk_row


def main():
    row, column = map(int, input().split())
    desc = set_desk(row)
    for r in range(row):
        for c in range(column):
            check_cheating_possible(desc, [r, c])
    answer = get_maximum_student(desc)
    return answer


test_cases = int(input())
answers = []
for test_case in range(test_cases):
    result = main()
    answers.append(result)
for a in answers:
    print(a)
