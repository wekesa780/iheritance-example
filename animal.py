
class Animal:
    def fur(self):
        print("I have fur all over my body.")


class Dog(Animal):
    def bark(self):
        print("Dog barking.")


class Puppy(Dog):
    def play(self):
        print("I play all the time.")


puppy_instance = Puppy()


puppy_instance.bark()  
puppy_instance.fur()   
puppy_instance.play()   