from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
r=human()
r.move()
s=snake()
s.move()
k=dog()
k.move()
a=lion()
a.move()
