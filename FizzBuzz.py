if __name__ == "__main__":
    # Itera sobre los valores del 1 al 100
    for i in range(1, 101):
        # Revisa si es divisible por 3 y 5
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        # Revisa si es divisible por 3
        elif i % 3 == 0:
            i = "Fizz"
        # Revisa si es divisible por 5
        elif i % 5 == 0:
            i = "Buzz"
        # Imprime el valor correspondiente
        print(i)
        
