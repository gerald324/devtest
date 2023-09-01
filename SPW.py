def Reemplazo(linea):
    x = 0
    for i in linea:
        if i == "*":
            valor1 = linea[:x] + "0" + linea[x+1:]
            valor2 = linea[:x] + "1" + linea[x+1:]
            return valor1, valor2
        x += 1
        
    return linea

if __name__ == "__main__":
    
    import sys

    permitidos = set("1" + "0" + "*")
    
    if len(sys.argv) == 1:
        val = str(input("Ingrese Valor:"))
    else:
        val = sys.argv[1]
    
    if set(val) <= permitidos:
        arreglo = [val]
        while "*" in arreglo[0]:
            at = []
            for a in arreglo:
                lin1, lin2 = Reemplazo(a)
                at.append(lin1)
                at.append(lin2)
            arreglo = at
        print (arreglo)
    else:
        print("Valor no valido, solo pueden haber 0, 1 y *")
