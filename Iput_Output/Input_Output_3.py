
correct_code = input("Proszę ustawić szyfr: ")

def check_code ():
    code = input("Proszę wpisać szyfr: ")
    if (code == correct_code):
        print("Zamek otwarty")
    else:
            print("Błędny szyfr")
            check_code()

check_code()
