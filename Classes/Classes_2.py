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



def parse_complex(input):
    input_split = input.split("+")
    real_str = input_split[0]
    imag_str = input_split[1].strip("i")
    return int(real_str), int(imag_str)

def start():
    choice = int(input("Proszę wybrać rodzaj operacji: \n"
                      "1 - dodawanie liczb zespolonych\n"
                      "2 - odejmowanie liczb zespolonych\n"
                      "3 - mnożenie liczb zespolonych\n"
                      "4 - sprzężenie liczby zespolonej\n"
                      "5 - wartość bezwględna liczby zespolonej"))
    if choice == 1:
        re,im = parse_complex(input("Proszę wpisać pierwszą liczbę( w formace RE+IMi):"))
        complex1 = ComplexNumber(re,im)
        re,im = parse_complex(input("Proszę wpisać drugą liczbę( w formace RE+IMi):"))
        complex2 = ComplexNumber(re,im)
        complex1.addition_complex(complex2)
        print(complex1.real,"+",complex1.imag,"i")
    elif choice == 2:
        re, im = parse_complex(input("Proszę wpisać pierwszą liczbę( w formace RE+IMi):"))
        complex1 = ComplexNumber(re, im)
        re, im = parse_complex(input("Proszę wpisać drugą liczbę( w formace RE+IMi):"))
        complex2 = ComplexNumber(re, im)
        complex1.subtraction_complex(complex2)
        print(complex1.real, "+", complex1.imag, "i")
    elif choice == 3:
        re, im = parse_complex(input("Proszę wpisać pierwszą liczbę( w formace RE+IMi):"))
        complex1 = ComplexNumber(re, im)
        re, im = parse_complex(input("Proszę wpisać drugą liczbę( w formace RE+IMi):"))
        complex2 = ComplexNumber(re, im)
        complex1.multiplication_complex(complex2)
        print(complex1.real, "+", complex1.imag, "i")
    elif choice == 4:
        re, im = parse_complex(input("Proszę wpisać pierwszą liczbę( w formace RE+IMi):"))
        complex1 = ComplexNumber(re, im)
        complex1.conjugation_complex()
        print(complex1.real, "+", complex1.imag, "i")
    elif choice == 5:
        re, im = parse_complex(input("Proszę wpisać pierwszą liczbę( w formace RE+IMi):"))
        complex1 = ComplexNumber(re, im)
        print(complex1.absolute_complex())
    else:
        print("Nieprawidłowy wybór!")
        start()

start()