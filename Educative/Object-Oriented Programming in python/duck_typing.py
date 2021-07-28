class Dog:
    def speak(self):
        print("Woof Woof")

class Cat:
    def speak(self):
        print("Meow Meow")


class AnimalSound:
    def Sound(self, animal):
        animal.speak()


sound = AnimalSound()

dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)
