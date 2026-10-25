def count_words(texts):
    new = texts.split()
    result = {}
    for text in new:
        text = text.lower()
        if text in result:
            result[text] += 1
        else:
            result[text] = 1
       
    return result 

print(count_words("python is fun and python is powerful"))