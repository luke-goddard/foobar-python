from functools import reduce

def solution(l, t):
    # l = [4, 3, 5, 7, 8] 
    # t = 12
    possible_answers = []
    possible_indexs = []

    for x in range(len(l)):
        tot = 0 
        for y in range(x, len(l)):
            tot += l[y]
            if tot == t:
                possible_answers.append(l[x:y+1])
                possible_indexs.append((x, y))
            if tot >= t:
                break 

    if len(possible_answers) == 0:
        return -1, -1
    
    return lexicographicaly_smallest(possible_answers, possible_indexs)
    
def lexicographicaly_smallest(answers, indexes):
    # print("Ans:    " + str(answers))
    # print("Indexs: " + str(indexes))
    # print("-----------------------")
    pos = -1
    # [[1,2,3], [34,5,6], [2,5]]
    # y = answers[y]
    # pos = answers[y][pos]
    final_answer = None
    while final_answer is None:
        pos += 1 
        generator = ([answers[y][pos] if len(answers[y]) > pos else -1 for y in range(len(answers))])
        smallest = min(generator)
        reduced_answers = list()
        for x in range(len(answers)):
            if len(answers[x]) <= pos:
                final_answer = answers[x]
                break
            if answers[x][pos] == smallest:
                reduced_answers.append(answers[x])
                break
        answers = reduced_answers
        if len(reduced_answers) == 1:
            final_answer = reduced_answers[0]

    return indexes[answers.index(final_answer)]
    
print(solution([4, 3, 5, 7, 8], 12))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([1, 2, 3, 4], 15))

# lexicographicaly_smallest([[1,3,3,4], [1,2,7,8], [9,10,11,23], [1, 2], [1, 2]], [1])