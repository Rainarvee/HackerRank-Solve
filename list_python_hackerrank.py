auv = []

N = int(raw_input())

for i in range(0, N):
    check = raw_input().split()

    if check[0] == 'insert':
        auv.insert(int(check[1]), int(check[2]))
    elif check[0] == 'print':
        print auv
    elif check[0] == 'remove':
        auv.remove(int(check[1]))
    elif check[0] == 'append':
        auv.append(int(check[1]))
    elif check[0] == 'sort':
        auv.sort()
    elif check[0] == 'pop':
        auv.pop()
    elif check[0] == 'reverse':
        auv.reverse()
