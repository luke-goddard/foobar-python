def solution(cake_str):
    for pos in range(1, len(cake_str) -1):
        pot_pattern = get_next_rep(cake_str, pos)           # Get the next repetition
        if pot_pattern is None:                             # No remaining split options found
            return 1
        if len(set(cake_str.split(pot_pattern))) == 1:      # Should only be one unique pattern 
            return len(cake_str.split(pot_pattern)) - 1     # Spliting the str by pattern gives 1 too many
    return 1

def get_next_rep(cake_str, pos):
    for x in range(pos, len(cake_str)-1):
        if cake_str[x] == cake_str[0]:
            return cake_str[0:x]                            # return the new pattern 
    return None