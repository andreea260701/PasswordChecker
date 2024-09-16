from passwordchecker.checker import evaluate_strength

if __name__ == '__main__':
    password = input("Introduceți parola pentru a verifica puterea: ")
    print(evaluate_strength(password))
