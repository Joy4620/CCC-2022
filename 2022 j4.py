X = int(input())
same = [input().split() for _ in range(X)]

Y = int(input())
diff = [input().split() for _ in range(Y)]

G = int(input())
group = [input().split() for _ in range(G)]

violation = 0

# check if in same group
for i in same:
    # print(f'testing same restraint, {i}')
    for j in group:
        if i[0] in j:
            if i[1] in j:
                break
            else:
                violation += 1
                break
                # print(i[0], i[1], 'same', j)


# check if in dif group
for i in diff:
    # print(f'testing dif restraint, {i}')
    for j in group:
        if i[0] in j:
            if i[1] not in j:
                break
            else:
                violation += 1
                break
                # print(i[0], i[1], 'diff', j)

print(violation)
