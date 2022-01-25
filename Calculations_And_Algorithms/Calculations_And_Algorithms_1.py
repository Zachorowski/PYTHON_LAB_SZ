import math

def check_if_number(input):
    try:
        val = float(input)
    except ValueError:
        print("Wartości nie są poprawne, wpisz jeszcze raz: ")
        start()

def start():
    input_data = input("Proszę podać oddzielone spacją współczynniki a, b i c równania kwadratowego: ")
    input_data_split = input_data.split()

    for i in range (len(input_data_split)):
        check_if_number(input_data_split[i])

    a = float(input_data_split[0])
    b = float(input_data_split[1])
    c = float(input_data_split[2])

    delta = b**2 - 4 * a * c
    if (delta == 0):
        x0 = -b / (2 * a)
        print("Funkcja ma jeden pierwiastek: ", x0)
    elif (delta > 0):
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Funkcja ma dwa pierwiastki: ", x1,"  ", x2)
    else:
        print("Funkcja nie ma rozwiązania w dziedzinie rzeczywistej")
start()



