class Fib():
    def __init__(self):
        self.a, self.b = 0, 1
    def _iter_(self):
        return self
    def _next_(self):
        self.a, self.b = self.b , self.b+self.a
        return self.a

fib = Fib()
for x in fib:
    if x > 10:
        break
    print(x)

