# author: victorisimo
# description: hackaton

def analysis():
    # enter the words
    print('Enter the first word: ')
    word_one = input()
    print('Enter the second word: ')
    word_two = input()
    # first verification
    if len(word_one) != len(word_two):
        print('FALSE')
    else:
        if anagram(word_one, word_two):
            print('TRUE')
        else:
            print ('FALSE')

def anagram(word_one,word_two):
    first_word = list(word_one.lower())
    two_word = list(word_two.lower())
    first_word.sort()
    two_word.sort()
    first_order = "".join(first_word)
    second_order = "".join(two_word)
    return first_order == second_order

#main method
if __name__ == '__main__':
    analysis()