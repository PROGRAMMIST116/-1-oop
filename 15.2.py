class Animal:
    name = ''

    def eat(self):
        print('Вкусно')

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def makeNoise(self):
        print(self.name+' говорит гллллллл')

    def __init__(self, name):
        self.name = name
        print('Появилось животное '+self.name)

animal1 = Animal('Сарделька')
print(animal1.getName())
animal1.setName('Бобик')
print('Новое имя: '+animal1.getName())
animal1.eat()
animal1.makeNoise()