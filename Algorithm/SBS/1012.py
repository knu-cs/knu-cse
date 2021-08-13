# BaekJoon 1012
# 14:34 ~ 15:40

def get_maximum_student(desc: list[list]) -> int:
    sum_student = 0
    for desc_row in desc:
        sum_student += desc_row.count("o")
    return sum_student


def _print_desc(desc: list[list]) -> None:
    for desc_row in desc:
        print(desc_row)


def check_cheating_possible(desc: list[list], check_matrix: list):
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
    else:
        desc[check_matrix[0]][check_matrix[1]] = "o"
    return desc


def set_desk(row: int) -> list:
    desk_row = []
    for r in range(row):
        row_data = list(input())
        desk_row.append(row_data)
    return desk_row


def main() -> None:
    row, column = map(int, input().split())
    desc = set_desk(row)
    for r in range(row):
        for c in range(column):
            check_cheating_possible(desc, [r, c])
    answer = get_maximum_student(desc)
    print(answer)


if __name__ == "__main__":
    test_cases = int(input())
    for test_case in range(test_cases):
        main()
