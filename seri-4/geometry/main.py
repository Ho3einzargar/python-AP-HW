from geometry import Shape

print('Learn Geometry.')
print('\tWhat do you want to do?')
print('\t(1) Add new shape')
print('\t(2) Show all shapes')
print('\t(3) Show shape with the largest perimeter')
print('\t(4) Show shape with the largest area')
print('\t(5) Show formulas')
print('\t(0) Exit program')

command = -1
while(command != 0):
    command = int(input())
    