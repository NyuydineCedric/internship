from fastapi import FastAPI
app =FastAPI()
@app.get("/wordcount/{sentence}")
def count_words(sentence):
    words = sentence.split()
    result ={}
    
    for word in words:
        if word in result:
            result[word] = result[word] +1
        else:
            result[word] = 1
    return result
