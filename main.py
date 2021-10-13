'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    div = 2
    while div * div <= n:
        if n % div == 0:
            return False
        div = div + 1
    return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    prod = 1
    for i in lst:
        prod = prod * i
    return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    r = x % y
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x != y:
    if(x > y):
        x = x - y
    else:
        y = y - x
  return x
  
  
def main():
  # interfata de tip consola aici
    while True:
        print ("1. Verifica daca un nr este prim.")
        print ("2. Calculeaza produsul numerelor dintr-o lista de nr naturale.")
        print ("3. Afiseaza cel mai mare divizor comun a doua nr naturale.")
        print ("x. Iesire")

        optiune = input("Selectati optiunea din cele de mai sus: ")

        if optiune == "1":
            nrString = input ("Dati numarul: ")
            nr = int(nrString)
            print (is_prime(nr))

        elif optiune == "2":
            l = []
            givenString = input ("Dati lista, cu elemente separate prin virgula: ")
            numbersAsString = givenString.split(",")
            for x in numbersAsString:
                l.append(int(x))
            print (get_product (l))

        elif optiune == "3":
            givenString = input ("Dati numerele, separate prin spatiu: ")
            numbersAsString = givenString.split(" ")
            x = int(numbersAsString[0])
            y = int(numbersAsString[1])
            print ('Cu modalitatea 1, cmmdc = ' + str(get_cmmdc_v1(x, y)))
            print ('Cu modalitatea 2, cmmdc = ' + str(get_cmmdc_v2(x, y)))

        elif optiune == "x":
            break

        else:
            print ("Optiune gresita. Reincercati!")

main()