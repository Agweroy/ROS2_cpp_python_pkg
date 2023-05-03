class Dog:
    """The dog class"""
    def __init__ (self,name,age):
        """@name refers to the dog's name
           @age refers to the dog's age"""
        self.name = name
        self.age = age
    def _talker1 (self):
        print("I'm a dog, My name is ",self.name)

    def _talker2(self):
        print("I'm ",self.age,"ears old")

dog_name = "jack"

dog = Dog(dog_name,1)
dog._talker1()