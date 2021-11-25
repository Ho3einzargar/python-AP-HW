import math
entry = int(input())
butyOddNumberList = []

def primefactors(n):
    result = []
    #even number divisible
    while n % 2 == 0:
        # print (2),
        # result.append(2)
        n = n / 2

    #n became odd
    for i in range(3,int(math.sqrt(n))+1,2):
        
        while (n % i == 0):
            # print (i)
            # n = int(n)
            if not(i in result):
                result.append(i)
            n = n / i

    if n > 2:
        result.append(n)
        # print (n)

    return result



for number in range(entry):
    if len(primefactors(number+1)) in primefactors(number+1):
        # print(number+1)
        # print(primefactors(number+1))
        butyOddNumberList.append(number+1)


result = 0
for number in butyOddNumberList:
    result = result + number

if result == 0:
    print('NOT FOUND!')
else:
    print((str(result))[::-1])


        
