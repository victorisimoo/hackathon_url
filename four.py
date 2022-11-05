def word_analysis(str_one, str_two):
    m = [[(0, "") for _ in range(len(str_one) + 1)] for _ in range(len(str_two) + 1)]
    for row in range(1, len(str_two) + 1):
        for col in range(1, len(str_one) + 1):
            diag = 0
            match = ""
            if str_one[col - 1] == str_two[row - 1]:
                diag = 1
                match = str_one[col - 1]
            if m[row][col - 1][0] >= m[row - 1][col][0] and m[row][col - 1][0] >= m[row - 1][col - 1][0] + diag:
                m[row][col] = m[row][col - 1]
            elif m[row - 1][col][0] >= m[row - 1][col - 1][0] + diag:
                m[row][col] = m[row - 1][col]
            else:
                m[row][col] = (m[row - 1][col - 1][0] + diag, m[row - 1][col - 1][1] + match)

    print(m[len(str_two)][len(str_one)][1])

# main method
if __name__ == '__main__':
    str_one = input('Enter the fist word: ')
    str_two = input('Enter the second word: ')
    word_analysis(str_one, str_two)
