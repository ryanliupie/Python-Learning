def count_words(words):
    '''
    A function that counts how many times each word appears in a list.
    '''

    dict_count = dict()

    for word in words: 
        dict_count[word] = dict_count.get(word, 0) + 1
    
    return dict_count

print(count_words(["apple", "banana", "apple", "orange", "banana", "apple"]))
