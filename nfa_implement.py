transition_table = {
    'A': {'a': {'A', 'C'}, 'b': {'A'}, 'c': {'B'}},
    'B': {'a': {'B'}, 'b': {'B'}, 'c': {'D'}},
    'C': {'a': {'B'}, 'b': {'E'}, 'c': {'C'}},
    'D': {'a': {}, 'b': {}, 'c': {}},
    'E': {'a': {}, 'b': {}, 'c': {}},
}
cur_states = {'A'}
next_states = set()
final_states = {'D'}
inp_str = input('Enter the string : ')
for ch in inp_str:
    next_states.clear()
    for state in cur_states:
        next_states = next_states.union(transition_table[state][ch])
    cur_states = next_states.copy()
    print('cs = ', cur_states)

valid = 0
for element in cur_states:
    if element in final_states:
        valid = 1
        break
if valid:
    print('Valid')
else:
    print('Invalid')
