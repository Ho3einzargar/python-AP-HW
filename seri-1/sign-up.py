userCount = int(input())
userList = []
authenticatedUserList = []

for number in range(userCount):
    userList.append(input())

for user in userList:
    userName = user.split(' ')[0]
    passWord = user.split(' ')[1]
    phoneNumber = user.split(' ')[2]

    if 'Admin' in userName or 'User' in userName:
        continue
    if len(userName) < 4:
        continue
    if not(any(map(str.isdigit, passWord))):
        continue
    if len(passWord) < 6:
        continue
    if len(phoneNumber) != 11:
        continue
    if phoneNumber[0] != '0' or phoneNumber[1] != '9':
        continue
    haveStrig = False
    for char in phoneNumber:
        if ord(char) < 48 or ord(char) > 57:
            haveStrig = True
            break
    if haveStrig:
        continue
        

    authenticatedUserList.append(user)

for index in range(99):
    for user in authenticatedUserList:
        lastTwoNumberOfPhoneNumber = (user.split(' ')[2])[-2:]
        if index == int(lastTwoNumberOfPhoneNumber):
            print(user.split(' ')[0], end=' ')