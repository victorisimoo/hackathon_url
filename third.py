# author: victorisimo
# description: hackaton
from typing import List


def binary_method():

    result = int(input('Enter the result: '))
    first =  int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))

    if (first + second) == result:
        result_binary = format(result, "b")
        result_grant = result_binary.count('1')
        print('Grandma will give you: {} hazelnuts'.format(result_grant))
    else:
        print ('Error in numbers')

# main method
if __name__ == '__main__':
    binary_method()