transition_table = {
    'A': {'0': ('0', 'A'), '1': ('1', 'B')},
    'B': {'0': ('1', 'B'), '1': ('0', 'B')}
}
present_state = 'A'
inp_str = "10101"
inp_str = inp_str[::-1]
out_str = ''
for ch in inp_str:
    out_str += transition_table[present_state][ch][0]
    present_state = transition_table[present_state][ch][1]
out_str = out_str[::-1]
print(out_str)
