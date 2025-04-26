from abc import ABC
class absclass(ABC):
    def print(self,x):
        print("Passed value",x)
    def task(self):
        print("We are in the abstract class")
class test_class(absclass):
    def task(self):
        print("We are in the test_class.")
test_model=test_class()
test_model.task()
test_model.print(100)
