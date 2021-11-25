entry = input()

oddNumberList = []
evenNumberList = []
upearcaseLetterList = []
lowercaseLetterList = []

def printItem(*items):
    for item in items:
        print(item, end='')

for char in entry:
    if ord(char) > 47 and ord(char) < 58:
        if int(char) % 2 == 0:
            evenNumberList.append(int(char))
        else:
            oddNumberList.append(int(char))

            
    
    if ord(char) > 64 and ord(char) < 91:
        upearcaseLetterList.append(char)

    if ord(char) > 96 and ord(char) < 123:
        lowercaseLetterList.append(char)


printItem(*sorted(lowercaseLetterList))
printItem(*sorted(upearcaseLetterList))
printItem(*sorted(oddNumberList))
printItem(*sorted(evenNumberList))