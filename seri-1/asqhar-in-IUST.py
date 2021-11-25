
dictionary = {}
taskList = []

# function to return key for any value in dic
def get_key(val):
    for key, value in dictionary.items():
         if val == value:
             return key


# get info
while True:
    entry = input()

    if entry == '.':
        break

    entry = entry.split('-')
    dictionary[entry[0]] = entry[1]


# get task
while True:
    entry = input()

    if entry == '.':
        break

    taskList.append(entry)


print('Saved information')

# show answer
for task in taskList:

    if task in dictionary:
        print(dictionary[task])
        continue
    elif task in dictionary.values():
        print(get_key(task))
        continue
    else:
        print('NOT FOUND')


print('End')
