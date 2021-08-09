def conning():
    case_count = int(input())
    perchable_list = []
    for _ in range(case_count):
        row, column = map(int, input().split(' '))
        even_column, odd_column = create_matrix(column, row)
        perchable_list = compare_columns_by_perchable(even_column, odd_column, perchable_list)

    return perchable_list


def create_matrix(column, row):
    rows = []
    even_column = []
    odd_column = []
    for i in range(row):
        rows.append(list(input()))
        even_column, odd_column = split_matrix_into_columns(column, i, rows, even_column, odd_column)
    return even_column, odd_column


def split_matrix_into_columns(column, i, rows, even_column, odd_column):
    for j in range(column):
        if j % 2 == 0:
            even_column.append(rows[i][j])
        elif j % 2 == 1:
            odd_column.append(rows[i][j])
    return even_column, odd_column


def compare_columns_by_perchable(even_column, odd_column, perchable_list):
    if even_column.count('.') > odd_column.count('.'):
        perchable_list.append(even_column.count('.'))
    else:
        perchable_list.append(odd_column.count('.'))
    return perchable_list


if __name__ == '__main__':
    perchables = conning()
    for perchable in perchables:
        print(perchable)
