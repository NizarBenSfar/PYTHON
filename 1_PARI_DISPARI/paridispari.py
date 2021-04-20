#numero in input determinare se pari o dispari
def paridispari():
    inp = input("inserisci un numero intero:" )
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("numero pari")
    else:
        print("numero dispari")

if __name__ == "__main__":
    paridispari()