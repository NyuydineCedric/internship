def count_words(sentence):
    words = sentence.split()
    result ={}
    
    for word in words:
        if word in result:
            result[word] = result[word] +1
        else:
            result[word] = 1
    return result

sentence = "the cat sat on the mat the cat ran"
print(count_words(sentence))