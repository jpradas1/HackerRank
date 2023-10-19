'''
For this challenge, you are given two complex numbers, and you have to 
print the result of their addition, subtraction, multiplication, division 
and modulus operations.

The real and imaginary precision part should be correct up to two decimal 
places.

Note
Methods with a double underscore before and after their name are considered 
as built-in methods. They are used by interpreters and are generally used 
in the implementation of overloaded operators or other built-in 
functionality.

    __add__-> Can be overloaded for + operation

    __sub__ -> Can be overloaded for - operation

    __mul__ -> Can be overloaded for * operation

For more information on operator overloading in Python, refer here.
    https://docs.python.org/3.2/reference/datamodel.html
'''

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, no):
        sum_real = self.real + no.real
        sum_imag = self.imaginary + no.imaginary
        if sum_imag >= 0:
            return f"{sum_real:.2f}+{sum_imag:.2f}i"
        else:
            return f"{sum_real:.2f}{sum_imag:.2f}i"
        
    def __sub__(self, no):
        sub_real = self.real - no.real
        sub_imag = self.imaginary - no.imaginary
        if sub_imag >= 0:
            return f"{sub_real:.2f}+{sub_imag:.2f}i"
        else:
            return f"{sub_real:.2f}{sub_imag:.2f}i"
        
    def __mul__(self, no):
        mul_real = self.real*no.real - self.imaginary*no.imaginary
        mul_imag = self.real*no.imaginary + self.imaginary*no.real
        if mul_imag >= 0:
            return f"{mul_real:.2f}+{mul_imag:.2f}i"
        else:
            return f"{mul_real:.2f}{mul_imag:.2f}i"
        
    def __truediv__(self, no):
        B2 = no.real**2 + no.imaginary**2
        div_real = (self.real*no.real + self.imaginary*no.imaginary)/B2
        div_imag = (-self.real*no.imaginary+self.imaginary*no.real)/B2
        if div_imag >= 0:
            return f"{div_real:.2f}+{div_imag:.2f}i"
        else:
            return f"{div_real:.2f}{div_imag:.2f}i"
    
    def mod(self):
        mod_real = math.sqrt(self.real**2 + self.imaginary**2)
        mod_imag = 0
        return f"{mod_real:.2f}+{mod_imag:.2f}i"

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')