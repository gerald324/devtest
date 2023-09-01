import sys

def reemplazo(linea):
    """
    Reemplaza el primer asterisco (*) de la cadena recibida por 0 y 1
    """
    x = 0
    for i in linea:
        if i == "*":
            valor1 = linea[:x] + "0" + linea[x+1:]
            valor2 = linea[:x] + "1" + linea[x+1:]
            return valor1, valor2
        x += 1
        
    return linea

if __name__ == "__main__":
    
    # Set de valores permitidos
    permitidos = set("1" + "0" + "*")
    
    # Reconoce si el valor fue ingresado por consola o por input
    if len(sys.argv) == 1:
        val = str(input("Ingrese Valor:"))
    else:
        val = sys.argv[1]
    
    # Transforma el valor ingresado en un set para validarlo
    if set(val) <= permitidos:
        lista = [val]
        # Por cada iteracion, valida que el primer elemento de la lista contenga un asterisco
        while "*" in lista[0]:
            at = []
            # Por cada elemento de la lista, reemplaza el primer asterisco encontrado
            # y añade las dos posibles soliciones a la lista
            for a in lista:
                lin1, lin2 = reemplazo(a)
                at.append(lin1)
                at.append(lin2)
            # Reemplaza la lista anterior por la solucion de la iteracion actual
            lista = at
        # Imprime la lista con la solucion final 
        print (lista)
    else:
        print("Valor no valido, solo pueden haber 0, 1 y *")
