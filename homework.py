class BMW:
    def __init__(self,m):
        self.m=m
    def start(self):
        print(f"{self.m} BMW is starting with a roar!")
    def drive(self):
        print(f"{self.m} BMW is driving smoothly.")
class Ferrari:
    def __init__(self,m):
        self.m=m
    def start(self):
        print(f"{self.m} Ferrari is starting with a loud vroom!")
    def drive(self):
        print(f"{self.m} Ferrari is speeding down the highway!")
def t(c):
    c.start()
    c.drive()
a=BMW("X5")
b=Ferrari("488 Spider")
t(a)
t(b)
