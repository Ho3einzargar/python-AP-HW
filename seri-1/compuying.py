#  get input and split it

firstUser = (input().split(' '))
firstUser = [int(i) for i in firstUser]

secondUser = (input().split(' '))
secondUser = [int(i) for i in secondUser]

thirdUser = (input().split(' '))
thirdUser = [int(i) for i in thirdUser]

fourthUser = (input().split(' '))
fourthUser = [int(i) for i in fourthUser]


# sort input array

firstUser.sort()
secondUser.sort()
thirdUser.sort()
fourthUser.sort()

# create array of best skills

bestPoints = []

bestPoints.append(firstUser[-1])
bestPoints.append(secondUser[-1])
bestPoints.append(thirdUser[-1])
bestPoints.append(fourthUser[-1])

holder = bestPoints[:]

bestPoints.sort()

print(holder.index(bestPoints[-1]) + 1)

# firstUserBestSkill