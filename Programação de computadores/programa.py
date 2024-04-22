'''
numero = int(input("Digite um número de 1 a 10: "))
while (numero > 10 or numero < 0):
    print('Valor inválido')
    numero = int(input("Digite um número válido: "))
else:
    print("Número válido: ", numero)
'''
'''
populacaoa = 80000
taxaa = 0.03

populacaob = 200000
taxab = 0.015

anos = 0

while populacaoa < populacaob:
    populacaoa = populacaoa + (populacaoa + taxaa)
    populacaob = populacaob + (populacaob + taxab)
    anos = anos + 1
print ('Anos necessários para A ultrapassar B: ', anos)
'''

fatorial = int(input("Informe um número: "))
resultado = 1
while (fatorial > 1):
    resultado *= fatorial
    fatorial -= 1
    print(resultado)