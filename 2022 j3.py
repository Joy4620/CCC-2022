tuning = input()
current = 0
output = []

while tuning:
    if current+1 >= len(tuning):
        output.append(tuning)
        tuning = ''
    else:
        if tuning[current] in '1234567890':
            if tuning[current+1] not in '1234567890':
                output.append(tuning[:current+1])
                tuning = tuning.replace(tuning[:current+1], '')
                current = 0
        current += 1

holder = 0
tune = ''
# print(output)
for i in output:
    # print(i, 'output')
    for j in range(len(i)):
        if i[j] in '123456789':
            holder = j
            break
    # print(holder-1, i)
    if i[holder-1] == '+':
        tune = 'tighten'
    else:
        tune = 'loosen'
    print(f'{i[:j-1]} {tune} {i[j:]}')
