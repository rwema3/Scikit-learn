class Computer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def config(self):
        print("Configuration is", self.name, self.age)

com1 = Computer("Dominque", 21)
com2 = Computer("Dominque", 31)

com1.configcom2.config(
