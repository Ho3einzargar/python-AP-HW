entry = input().split()
mylist = []
for i in range(int(entry[0])):mylist.append(list(map(lambda x: int(x), input().split())))
sortIndex = int(input())
print(*('%d %d %d' % tuple(r) for r in sorted(mylist, key=lambda x: x[sortIndex])), sep='\n')