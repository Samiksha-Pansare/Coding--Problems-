class Test:
    def __init__(self,name):
        self.name = name;
        pass
    def one(self):
        print("One Method",self.name)
    def two(self):
        self.one()
        print("Two Method",self.name)

obj = Test("Sam")
obj.one()
    