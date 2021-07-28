#!/usr/bin/python3

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total_obtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return self.total_obtained() / 300 * 100


ram = Student("Ram", 98, 94, 99)
print(ram.percentage())


