entry = input()

a = int(entry.split()[0])
b = int(entry.split()[1])
c = int(entry.split()[2])

half_perimeter = (a + b + c) / 2

space = (half_perimeter * (half_perimeter-a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5

print("{:.3f}".format(space))