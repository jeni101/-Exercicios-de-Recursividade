def soma_elementos(list):
    if not list:
        return 0
    else:
        return list[0] + soma_elementos(list[1:])
    
lista = [1,2,3,4,5]
print(soma_elementos(lista))