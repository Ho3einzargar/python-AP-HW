class FruitType():
    """

    |--------------------------------------------------
    |                                                 |
    |     Fruit type Class                            |
    |                                                 |
    |--------------------------------------------------
    |                                                 |
    |   1 - initial Class                             |
    |                                                 |
    |                                                 |
    |   2 - Name property                             |
    |   3 - Name setter                               |
    |                                                 |
    |                                                 |
    |   4 - Protein property                          |
    |   5 - Protein setter                            |
    |                                                 |
    |                                                 |
    |   6 - Fat property                              |
    |   7 - Fat setter                                |
    |                                                 |
    |                                                 |
    |   8 - Carbs property                            |
    |   9 - Carbs setter                              |
    |                                                 |
    |                                                 |
    ---------------------------------------------------

    """
    # -> 1
    def __init__(self, Vname, Vprotein, Vcarbs, Vfat):
        self.fruitNameList = ['apple', 'orange', 'lemon', 'banana', 'cucumber', 'peach']

        if Vname in self.fruitNameList:
            self.Name = Vname
        else:
            raise ValueError('This fruit does not allow')
            
        self.Protein = Vprotein
        self.Carbs = Vcarbs
        self.Fat = Vfat

    # -> 2
    @property # read property
    def Name(self):
        return self._VName

    # -> 3
    @Name.setter # write property
    def Name(self, Name):
        self._VName = Name



    # -> 4
    @property # read property
    def Protein(self):
        return self._Vprotein
    
    # -> 5
    @Protein.setter # write property
    def Protein(self, protein):
        if (protein > 5):
            self._Vprotein = protein


    # -> 6
    @property # read property
    def Fat(self):
        return self._Vfat
    # -> 7
    @Fat.setter # write property
    def Fat(self, fat):
        if (fat < 2):
            self._Vfat = fat


    # -> 8
    @property # read property
    def Carbs(self):
        return self._Vcarbs
    # -> 9
    @Carbs.setter # write property
    def Carbs(self, carbs):
        if (carbs > 80):
            self._Vcarbs = carbs

class Fruit(FruitType):
    """

    |--------------------------------------------------
    |                                                 |
    |     Fruit Class                                 |
    |                                                 |
    |--------------------------------------------------
    |                                                 |
    |   1 - initial Class                             |
    |                                                 |
    |                                                 |
    |   2 - Type property                             |
    |                                                 |
    |   3 - Weight property                           |
    |                                                 |
    |   4 - Protein property                          |
    |                                                 |
    |   5 - Fat property                              |
    |                                                 |
    |   6 - Carbs setter                              |
    |                                                 |
    |   7 - __str__ func                              |
    |                                                 |
    |                                                 |
    ---------------------------------------------------

    """

    # -> 1
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

    # -> 2
    @property
    def Type(self):
        return self._type

    # -> 3
    @property
    def Weight(self):
        return self._weight

    # -> 4
    @property
    def Protein(self):
        if self.type.Protein:
            return self.self.type._Protein
        else:
            raise ValueError('protein doesent exist')

    # -> 5
    @property
    def Fat(self):
        if self.type.Fat:
            return self.self.type._Fat
        else:
            raise ValueError('Fat doesent exist')

    # -> 6
    @property
    def Carbs(self):
        if self.type.Carbs:
            return self.self.type._Carbs
        else:
            raise ValueError('Carbs doesent exist')

    # -> 7
    def __str__(self):
        return self.type.Name + ' ' + str(self.type.Protein) + ' ' + str(self.type.Fat) + ' ' + str(self.type.Carbs)

class Compare(Fruit):

    """

    |--------------------------------------------------
    |                                                 |
    |     Compare Class                               |
    |                                                 |
    |--------------------------------------------------
    |                                                 |
    |   1 - initial Class                             |
    |                                                 |
    |   2 - compare fruite func                       |
    |                                                 |
    ---------------------------------------------------

    """

    # -> 1
    def __init__(self, fruit1, fruit2):
        self.fruit1 = fruit1
        self.fruit2 = fruit2

    # -> 2
    def compare(self):
        firstFruitPoint = 0
        secondFruitPoint = 0

        if self.fruit1.type.Protein > self.fruit2.type.Protein:
            firstFruitPoint += 1
        else:
            secondFruitPoint += 1

        if self.fruit1.type.Carbs > self.fruit2.type.Carbs:
            firstFruitPoint += 1
        else:
            secondFruitPoint += 1

        if self.fruit1.type.Fat < self.fruit2.type.Fat:
            firstFruitPoint += 1
        else:
            secondFruitPoint += 1

        if firstFruitPoint > secondFruitPoint:
            print('fruit1')
        else:
            print('fruit2')

entry = input().split(' = ')
fruittype1 = eval(entry[1])

entry = input().split(' = ')
fruittype2 = eval(entry[1])

entry = input().split(' = ')
fruit1 = eval(entry[1])

entry = input().split(' = ')
fruit2 = eval(entry[1])

entry = input().split(' = ')
com = eval(entry[1])

eval(input())

# ? entry example:
""" 

fruittype1 = FruitType("banana", 6.5, 93, 0.5)
fruittype2 = FruitType("orange", 9, 90, 1)
fruit1 = Fruit(fruittype1, 110)
fruit2 = Fruit(fruittype2, 100)
com = Compare(fruit1, fruit2)
com.compare()

"""