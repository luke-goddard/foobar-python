"""
How this algorithm works
lets say that we get the list [1, 2, 3, 4]
first we sort the list giving [4, 3, 2, 1]
then we take the sum of the list 4 + 3 + 2 + 1 = 10 
this does not equal 3 so we dont return 4321
no mater what way you arrange 4,3,2,1 the sum of it wont change so it will never divide by 3
so next we the find the lexicographical combination of the integers choosing n place 
because the array is sorted we get the combitinations in order 
we then sort of the combinations values to get the highest possible value for that given combonation
if that combonations does not add up to 3 we move to next one 
if we run out of combonations we decrease n and get more combonations until n is 0 
if n is 0 we return 0
"""

import itertools

def solution(l): 
    l.sort(reverse=True)
    if sum(l) % 3 == 0:
        return int(''.join(map(str, l)))
    for choose in range(len(l)-1, 0, -1):
        for combo in itertools.combinations(l, choose):
            if sum(combo) % 3 == 0:
                combo = list(combo)
                combo.sort(reverse=True)
                return int(''.join(map(str, combo)))
    return 0
