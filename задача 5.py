a = input().split()
b = []
while a != ['end']:
    a = [int(i) for i in a]
    b += [a]
    a = input().split()
B = len(b)
B0 = len(b[0])
for i in range(B):
    for j in range(B0):
        print(b[(i-1)][j]+b[(i+1)%B][j]+b[i][j-1]+b[i][(j+1)%B0],end=' ')
    print()