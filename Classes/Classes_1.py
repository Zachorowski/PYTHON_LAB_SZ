import math

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def addition_complex(self, complex_number):
        return ComplexNumber(self.real + complex_number.real, self.imag + complex_number.imag)

    def subtraction_complex(self, complex_number):
        return ComplexNumber(self.real - complex_number.real, self.imag - complex_number.imag)

    def multiplication_complex(self, complex_number):
        return ComplexNumber(self.real * complex_number.real - self.imag * complex_number.imag, self.real * complex_number.imag + self.imag * complex_number.real)

    def conjugation_complex(self):
        return ComplexNumber(self.real, -1*self.imag)

    def absolute_complex(self):
        return math.sqrt(self.real * self.real + self.imag * self.imag)
