class Dog:
    def bark(self, name):
        print("bark")
    
    def meow(self, x):
        return x + 1
    

d = Dog()
d.bark("rwemaaa")
print(type(d))
print(d.meow(3))
