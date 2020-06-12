class Calc(object):
    _history = []
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        result = self.num1 + self.num2
        Calc._history.append("add : "+str(result))
        return self.num1 + self.num2
    def sub(self):
        result = self.num1 - self.num2
        Calc._history.append("sub : "+str(result))
        return self.num1 - self.num2

    @classmethod
    def history(cls):
        for item in Calc._history:
            print(item)

class Ref(object):
    def multi(self):
        result = self.num1 * self.num2
        Calc._history.append("multi : "+str(result))
        return self.num1 * self.num2

class Calc_Ref(Calc, Ref):
    def devide(self):
        result = self.num1 / self.num2
        Calc._history.append("devide : "+str(result))
        return self.num1 / self.num2


C3 = Calc_Ref(20,10)
print("더하기 : " + str(C3.sum()))
print("빼기 : " + str(C3.sub()))
print("곱하기 : " + str(C3.multi()))
print("나누기 : " + str(C3.devide()))