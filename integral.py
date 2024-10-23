from fractions import Fraction

class Integral:
    def __init__(self):
        pass 

    def indefinite_integral(self):
        raise NotImplementedError("This method should be implemented in subclasses.")


class PolynomialIntegral(Integral):#полиномный интеграл к примеру x^2
    def __init__(self, power,l1):
        super().__init__()  #super() – это встроенная функция в Python, которая возвращает объект родительского класса. Она полезна, когда тебе нужно вызвать методы родительского класса внутри дочернего.
        self.power = power
        self.l1 = l1

    def indefinite_integral(self):
        if self.power == -1:
            return 
            f"ln|x| + C"
        
        new_power = self.power + 1
        coefficient = Fraction(1, new_power) #fractional это приводит вид к дробной

        return f"({self.l1}*{coefficient}) * x^{new_power} + C"


class ExponentialIntegral(Integral):
    def __init__(self, k):
        super().__init__()
        self.k = k  #k это коэфицент перед e^kx

    def indefinite_integral(self):
        if self.k != 0:
            return f"({Fraction(1, self.k)}) * e^( {self.k} * x ) + C"
        else:
            return f"x + C"


class PowerIntegral(Integral):
    def __init__(self, a):
        super().__init__()
        self.a = a 

    def indefinite_integral(self):
        if self.a > 0 and self.a != 1:  # если а будет 1 или 0 интеграл будет не определен
            return f"(1/ln({self.a})) * {self.a}^u + C"
        else:
            return 
            f"не определен"


class SinIntegral(Integral):
    def __init__(self, l):
        super().__init__()
        self.l = l  # l это коэфицент sin(l*a)

    def indefinite_integral(self):
        if self.l != 0:
            return f"-({Fraction(1, self.l)}) * cos({self.l} * u) + C"
        else:
            return "Integral of sin(0 * u) is 0 + C"  


class CosIntegral(Integral):
    def __init__(self, m):
        super().__init__()
        self.m = m  #коэфицнт  cos(m * u)

    def indefinite_integral(self):
        if self.m != 0:
            return f"({Fraction(1, self.m)}) * sin({self.m} * u) + C"
        else:
            return f"Integral of cos(0 * u) is u + C"  


class sec_sqare_Integral(Integral):
    def __init__(self,b):
        super().__init__
        self.b = b# b это коэфицент sec(k*u)

    def indefinite_integral(self):
        if self.b != 0:
            return f"({Fraction(1,self.b)})*tan({self.b}*u)+C"
        else:
            return
            f"НЕ определен"

class csc_square_Integral(Integral):
    def __init__(self,c):
        super().__init__
        self.c = c
    def indefinite_integral(self):
        if self.c != 0:
            return f"-({Fraction(1,self.c)}*cot({self.c}*u) +C)"
        else:
            f"не определен"

class sec_u_tan_u(Integral):
    def __init__(self,d):
        super().__init__
        self.d = d
    def indefinite_integral(self):
        if self.d != 0:
            return f"({Fraction(1,self.d)}*sec({self.d}*u))+C"
        else:
            f"не определено"

class csc_u_cot_u(Integral):
    def __init__(self,e):
        super().__init__
        self.e = e
    def indefinite_integral(self):
        if self.e != 0:
            return f"-({Fraction(1,self.e)}*csc({self.e}*u))+C"
        else:
            f"не определен"

class tanu_integral(Integral):
    def __init__(self,f):
        super().__init__
        self.f = f
    def indefinite_integral(self):
        if self.f != 0:
            return f"-({Fraction(1,self.f)}*ln(|cos({self.f}*u)|)+C"
        else:
            f"не определен"


class cotu_integral(Integral):
    def __init__(self,g):
        super().__init__
        self.g = g
    def indefinite_integral(self):
        if self.g != 0:
            return f"({Fraction(1,self.g)}*ln(|sin({self.g}*u)|)+C"
        else:
            f"не определен"

class sec_u_integral(Integral):
    def __init__(self,h):
        super().__init__
        self.h = h
    def indefinite_integral(self):
        if self.h >= 1:
            return f"{Fraction(1,self.h)} * log|sec({self.h}*u)+tan({self.h}*u)|+C"

        else:
            f"не определен"

class csc_u_integral(Integral):
    def __init__(self,i):
        super().__init__
        self.i = i
    def indefinite_integral(self):
        if self.i >= 1:
            return f"-{Fraction(1,self.i)}*log|csc({self.i}*u)-cot({self.i}*u)|+C"
        else:
            f"Не определено"

class a_square_plus_u_square(Integral):
    def __init__(self,j):
        super().__init__
        self.j = j
    def indefinite_integral(self):
        if self.j > 0:
            return f"{Fraction(1,self.j)} * arctan(u/{self.j})+C"
        else:
            return f"Эээ зачем ноль поставил"
        


class cossquareu(Integral):
    def __init__(self, k):
        super().__init__
        self.k = k
    
    def indefinite_integral(self):
        if self.k != 0:
            return f"(1/2) * u + (1/{2*self.k}) * sin(2*{self.k} * u) + C"
        else:
            return f"не ставь ноль пж"


class sqrt_asquare_minus_usquare(Integral):
    def __init__(self,l):
        super().__init__
        self.l = l
    def indefinite_integral(self):
        if self.l >0:
            return f"arcsin(u/{self.l})+C"
        else:
            return f"не определен"
