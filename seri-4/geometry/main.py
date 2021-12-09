from geometry import Shape, ShapeList, Circle, EquilateralTriangle, Rectangle, RegularPantagon, Square, Triangle

print('Learn Geometry.')
print('\tWhat do you want to do?')
print('\t(1) Add new shape')
print('\t(2) Show all shapes')
print('\t(3) Show shape with the largest perimeter')
print('\t(4) Show shape with the largest area')
print('\t(5) Show formulas')
print('\t(0) Exit program')

ShapeList = ShapeList();

command = -1
while(command != 0):
    command = int(input())
    if command == 1:
        
        shapeInfo = input('enter shape name and argument:').split(' ')

        if shapeInfo[0] == 'Circle':
            newShape = Circle(shapeInfo[1])    

        if shapeInfo[0] == 'EquilateralTriangle':
            newShape = EquilateralTriangle(shapeInfo[1])    

        if shapeInfo[0] == 'Rectangle':
            newShape = Rectangle(shapeInfo[1], shapeInfo[2])    

        if shapeInfo[0] == 'RegularPantagon':
            newShape = RegularPantagon(shapeInfo[1])    

        if shapeInfo[0] == 'Square':
            newShape = Square(shapeInfo[1])    

        if shapeInfo[0] == 'Triangle':
            newShape = Triangle(shapeInfo[1], shapeInfo[2], shapeInfo[3])    


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



    