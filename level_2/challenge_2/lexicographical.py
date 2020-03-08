from functools import reduce

def solution(l, t):
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
    pos = -1
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