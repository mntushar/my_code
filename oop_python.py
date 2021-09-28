# add two number instance method with argument in class
class AddTwoNum():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addNum(self):
        return self.a+self.b


# add two number class variable be instance methode from class2
class AddTwoNum2():
    a = ''
    b = ''

    def __init__(self):
        self.a = a
        self.b = b

    def addNum(self):
        return self.a+self.b


# add two number instance methode without argument from class3
class AddTwoNum3():
    def __init__(self):
        self.a = a
        self.b = b

    def addNum(self):
        return self.a+self.b


# add two number static method from class4
class AddTwoNum4():
    @staticmethod
    def addNum(a, b):
        return a+b


# add two number in class variable from class5
class AddTwoNum5():
    a = ''
    b = ''

    @classmethod
    def addNum(cls):
        return a+b


# add two number in inner class from class6
class AddTwoNum6():
    def __init__(self):
        self.sendClass = self.TwoNumber

    class TwoNumber():
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def addNum(self):
            return self.a+self.b


# add two number inherit class from class7
class AddTwoNum7(AddTwoNum):
    def mul(self):
        return self.a*self.b


# add two number inherit with init class from class8
class AddTwoNum8(AddTwoNum):
    def __init__(self):
        super().__init__(a, b)

    def mul(self):
        return self.a*self.b


# add two number in function
def funAdd(a, b):
    return a+b


# main function
if __name__ == '__main__':
    n = 1
    a = int(input())
    b = int(input())

    # for class
    add = AddTwoNum(a, b)
    classAdd = add.addNum()
    print('Add form class:', classAdd)

    # for class 2
    add2 = AddTwoNum2()
    add2.a = a
    add2.b = b
    classAdd2 = add2.addNum()
    print('Add form class2:', classAdd2)

    # for class 3
    add3 = AddTwoNum3()
    add3.a = a
    add3.b = b
    classAdd3 = add3.addNum()
    print('Add form class3:', classAdd3)

    # for class 4
    classAdd4 = AddTwoNum4.addNum(a, b)
    print('Add form class3:', classAdd4)

    # for class 5
    AddTwoNum5.a = a
    AddTwoNum5.b = b
    classAdd5 = AddTwoNum5.addNum()
    print('Add form class3:', classAdd5)

    # for class 6
    add6 = AddTwoNum6.TwoNumber(a, b)
    classAdd6 = add6.addNum()
    print('Add form class:6', classAdd6)

    # for class 7
    mul = AddTwoNum7(a, b)
    classMul7 = mul.mul()
    print('Multipul form class7:', classMul7)

    # for class 8
    mul = AddTwoNum8()
    classMul8 = mul.mul()
    print('Multipul form class8:', classMul8)

    # for function
    funcAdd = funAdd(a, b)
    print('Add form function:', funcAdd)
