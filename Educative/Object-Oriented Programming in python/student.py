class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber
    
    def getRollNumber(self):
        return self.__RollNumber
    
demo1 = Student()
demo1.setName('Alex')
print(f'Name: {demo1.getName()}')
demo1.setRollNumber(25253)
print(f'Roll Number: {demo1.getRollNumber()}')
