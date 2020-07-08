def search_with_memory(arr, k):
    was = set()
    ans = []
    for x in arr:
        if x in was:
            continue
        if k - x in was:
            ans.append((x, k - x))
        was.add(x)
    return ans


def search_without_memory(arr, k):
    arr.sort()
    ans = []
    prev = None
    for i, x in enumerate(arr):
        if x == prev:
            continue
        if x > k / 2 or i == len(arr) - 1:
            break
        num = k - x
        l = i + 1
        r = len(arr)
        while l + 1 < r:
            m = (l + r) // 2
            if arr[m] > num:
                r = m
            else:
                l = m
        if arr[l] == num:
            ans.append((x, num))
        prev = x
    return ans


def check_lines(field, i, j, k):
    for x in range(9):
        if x == i:
            continue
        if field[x][j] == k:
            return False
    for x in range(9):
        if x == j:
            continue
        if field[i][x] == k:
            return False
    return True


def check_square(field, i, j, k):
    x = i // 3
    y = j // 3
    for a in range(x * 3, x * 3 + 3):
        for b in range(y * 3, y * 3 + 3):
            if a == i and b == j:
                continue
            if field[a][b] == k:
                return False
    return True


def check(field, i, j, k):
    return check_square(field, i, j, k) and check_lines(field, i, j, k)


def solve_sudoku(path):
    with open(path, 'r') as file:
        field = [[int(c) for c in x.strip()] for x in file.readlines()]
    left = 0
    for line in field:
        left += line.count(0)
    while left > 0:
        for i in range(9):
            for j in range(9):
                if field[i][j] != 0:
                    continue
                good = []
                for k in range(1, 10):
                    if check(field, i, j, k):
                        good.append(k)
                if len(good) == 1:
                    field[i][j] = good[0]
                    left -= 1
    for line in field:
        print(''.join([str(x) for x in line]))


solve_sudoku('input.txt')