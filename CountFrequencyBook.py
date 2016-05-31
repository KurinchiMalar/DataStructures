'''
    Count the frequency of words in book
'''

def count_frequency(book):

    if book is None:
        return None

    hash_table = dict()

    for word in book:

        if word in hash_table:
            hash_table[word] = hash_table[word] + 1
        else:
            hash_table[word] = 1
    print hash_table


book = "I am a good I good stars  peacok stars am a"
book = book.split()

count_frequency(book)