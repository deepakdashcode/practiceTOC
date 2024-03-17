transition_table = {
    'A': {'0': 'A', '1': 'B'},
    'B': {'0': 'B', '1': 'C'},
    'C': {'0': 'B', '1': 'C'}
}
transition_output = {'A': '0', 'B': '1', 'C': '0'}
inp_str = "10101"
inp_str = inp_str[::-1]
out_str = ''
present_state = 'A'
for ch in inp_str:
    out_str += transition_output[present_state]
    present_state = transition_table[present_state][ch]
out_str += transition_output[present_state]
out_str = out_str[::-1]
print(out_str)
print('Ignore the last character')