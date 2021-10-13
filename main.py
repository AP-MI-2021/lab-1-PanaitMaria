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

    if _name_ == '_main_':
        main()
        print(get_cmmdc_v1(8, 9))
        print (get_cmmdc_v2(8, 10))