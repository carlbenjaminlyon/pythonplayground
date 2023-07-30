import json
import asyncio

class ParentClass:
    def __init__(self, param1) -> None:
        self.param1 = param1

    def parentMethod(self):
        print(f'Parent method called. : {self.param1}')


class NewClass(ParentClass):
    def __init__(self, param1, param2) -> None:
        super().__init__(param2)
        self.newClassCount = param2
        print('some self: ', self)

    def newMethod(self):
        result = self.param1 + self.newClassCount
        print('result: ', result)
        print(f'Result is: {result}')


obj = NewClass(10, 20)
obj.parentMethod()
obj.newMethod()

class Utilities():
      def loop(self, args):
          for arg in args:
              return arg
              continue