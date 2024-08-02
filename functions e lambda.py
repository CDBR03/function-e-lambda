##Criando uma function
def preco_imposto(preco,imposto):
    return preco * (1 + imposto)
print(preco_imposto(5,0.3))

imposto = 0.0044
##Mostrando que utilizando uma lambda, podemos encontrar o mesmo valor, com uma linha de codigo
preco_imposto2 = lambda preco: preco * (1.0 + imposto)
print(preco_imposto2(50))
