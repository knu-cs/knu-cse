def conning():
    case_count = int(input())
    perchable_list = []
    for _ in range(case_count):
        row, column = map(int, input().split(' '))
        rows = []
        even_column = []
        odd_column = []
        for i in range(row):
            rows.append(list(input()))
            for j in range(column):
                if j % 2 == 0:
                    even_column.append(rows[i][j])
                elif j % 2 == 1:
                    odd_column.append(rows[i][j])

        if even_column.count('.') > odd_column.count('.'):
            perchable_list.append(even_column.count('.'))
        else:
            perchable_list.append(odd_column.count('.'))

    return perchable_list


if __name__ == '__main__':
    perchables = conning()
    for perchable in perchables:
        print(perchable)
