# import classes rom geometery file
from geometry import Shape, ShapeList, Circle, EquilateralTriangle, Rectangle, RegularPantagon, Square, Triangle

# command list
print('Learn Geometry.')
print('\tWhat do you want to do?')
print('\t(1) Add new shape')
print('\t(2) Show all shapes')
print('\t(3) Show shape with the largest perimeter')
print('\t(4) Show shape with the largest area')
print('\t(5) Show formulas')
print('\t(0) Exit program')

# new shape list class
ShapeList = ShapeList();

command = -1

# get commands from user
while(command != 0):
    command = int(input())
    if command == 1:
        
        shapeInfo = input('enter shape name and argument:').split(' ')

        if shapeInfo[0] == 'Circle':
            newShape = Circle(int(shapeInfo[1]))    

        if shapeInfo[0] == 'EquilateralTriangle':
            newShape = EquilateralTriangle(int(shapeInfo[1]))    

        if shapeInfo[0] == 'Rectangle':
            newShape = Rectangle(int(shapeInfo[1]), int(shapeInfo[2]))    

        if shapeInfo[0] == 'RegularPantagon':
            newShape = RegularPantagon(int(shapeInfo[1]))    

        if shapeInfo[0] == 'Square':
            newShape = Square(int(shapeInfo[1]))    

        if shapeInfo[0] == 'Triangle':
            newShape = Triangle(int(shapeInfo[1]), int(shapeInfo[2]), int(shapeInfo[3]))    


        ShapeList.add_shape(newShape)

    if command == 2:
        print(ShapeList.get_shapes_table())
    if command == 3:
        print(ShapeList.get_largest_shape_by_perimeter)
    if command == 4:
        print(ShapeList.get_largest_shape_by_area)
    if command == 5:
        shapeInfo = input('enter shape name:')
        if shapeInfo == 'Circle':
            print(Circle)
        if shapeInfo == 'EquilateralTriangle':
            print(EquilateralTriangle)

        if shapeInfo == 'Rectangle':
            print(Rectangle)

        if shapeInfo == 'RegularPantagon':
            print(RegularPantagon)

        if shapeInfo == 'Square':
            print(Square)

        if shapeInfo == 'Triangle':
            print(Triangle)

    