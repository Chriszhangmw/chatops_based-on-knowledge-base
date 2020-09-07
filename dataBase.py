

class Test:
    def function1(self,age):
        global res
        if age > 20:
            res = "old"
        else:
            res = "young"
        return res
    def funtion2(self,number):
        if number == 10:
            res = "Chris"
        elif number == 20:
            res = "Damon"
        print(res)


test = Test()
res = test.function1(2)
print(res)

res = test.funtion2(3)
