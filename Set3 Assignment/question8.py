#WORD FREQUENCY RANKING

def rank_words(text, top_n):
    
    words = text.split()
    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    result = []

    while len(result) < top_n:

        highest_word = ""
        highest_count = 0

        for word in frequency:

            if frequency[word] > highest_count:
                highest_count = frequency[word]
                highest_word = word

        result.append((highest_word, highest_count))
        frequency[highest_word] = 0

    return result


print(rank_words("the fox and the hound and the cat", 2))