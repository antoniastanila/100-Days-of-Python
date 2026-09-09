class Ama:
    a = 1

    def func1(self):
        print(getattr(self, "a"))

    def func2(self):
        print(self.a)

aaa = Ama()
aaa.func1()
aaa.func2()

