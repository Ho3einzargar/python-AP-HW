entry = input()

A = entry.split(' + ')[0]
B = (entry.split(' + ')[1]).split(' = ')[0]
C = (entry.split(' + ')[1]).split(' = ')[1]

# print(A)
# print(B)
# print(C)

if '#' in entry:
    if '#' in A:
        equalNumber = str(int(C) - int(B))

        print(equalNumber)
        print(A)

        if A[0] == '#':
            # print('first')
            holder = equalNumber[0:len(equalNumber)-len(A)+1]
            if equalNumber == (holder + A.replace('#', '')):
                print(equalNumber, '+', B, '=', C)
            else:
                print('-1')



        elif A[-1] == '#':
            # print('last')
            holder = equalNumber[(len(equalNumber)-len(A)+1)*-1:]
            if equalNumber == (A.replace('#', '') + holder):
                print(equalNumber, '+', B, '=', C)
            else:
                print('-1')


        else:
            print('middle')

            removeFromLast = len(A) - A.index('#') - 1
            removeFromFirst = A.index('#')
            # print(removeFromFirst)
            # print(removeFromLast)

            # holder = equalNumber[removeFromLast * -1:]
            holder = equalNumber[0:removeFromLast]
            holder = holder[removeFromFirst:]

            print(A[0:removeFromFirst])
            print(holder)
            print(A[(removeFromFirst+1) * -1:])

            
            if equalNumber == (A[0:removeFromFirst] + holder + A[(removeFromFirst+1) * -1:]):
                print(equalNumber, '+', B, '=', C)
            else:
                print('-1')


            # print(holder)



        # A + x

        # print(int(C) - int(B))
        # x = C - B
        
    # elif '#' in B:

    # elif '#' in C:

else:
    if (int(A) + int(B)) == int(C):
        print(entry)
    else:
        print('-1')

