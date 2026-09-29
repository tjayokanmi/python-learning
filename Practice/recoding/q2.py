# Return every score greater than or equal to 50, in the original order. Inputs are lists of integers from 0 to 100. An empty list must return an empty list.
# def passing_scores(scores):
#     passed = []
#     for index in range(len(scores)):
#         if scores[index] >= 50:
#             passed.append(scores[index])
#     return passed
# # print(passing_scores([49, 50, 80, 65]))

# assert passing_scores([49,50,80,65]) == [50, 80, 65]
# assert passing_scores([]) == []
# assert passing_scores([50]) == [50]
# assert passing_scores([23, 80, 34]) == [80]

def passing_scores(scores):
    passed = []
    for index in range(len(scores) - 1):
        if scores[index] > 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))