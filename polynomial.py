class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    def evaluate(self, x):
        return(x)

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Mul, Div)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Mul, Div)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " - " + p2_repr

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, value):
      return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Mul)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Mul)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " / " + p2_repr
    
    def evaluate(self, value):
        denominator = self.p2.evaluate(value)
        if denominator == 0:
            raise ValueError("There is division by zero!")
        return self.p1.evaluate(value) / self.p2.evaluate(value)
