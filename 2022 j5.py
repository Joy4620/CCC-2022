'''
Sample Input 1
5
1
2 4

Output for Sample Input 1
3

Sample Input 2
15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14

Output for Sample Input 2
7
'''

N = int(input())
T = int(input())
tree = [list(map(int, input().split())) for _ in range(T)]

Matrix = [['.' for _ in range(N)] for _ in range(N)]

for x in tree:
    Matrix[x[0]-1][x[1]-1] = '0'
# for x in Matrix:
#     print(x)

area = N
while area > 0:
    # print('area so far', area)
    current = True
    for x in range(N-area+1):
        for y in range(N-area+1):  # all locations of areas
            for i in range(area):
                for j in range(area):  # scan all items in area
                    print(i, j, x, y)
                    if Matrix[x+i][y+j] == '0':
                        # print(Matrix[x+i][y+j], x+i, y+j)
                        area -= 1
                        current = False
                        print('area couldnt fit', area)
                        continue
                        
                    # Matrix[x+i][y+j] = f'{i}{j}'
            if current is True:
                print('AREA CAN FIT!', area)
                quit()
    area -= 1

# print(area)
# for x in Matrix:
#     print(x)

