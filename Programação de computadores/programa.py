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

'''
fatorial = int(input("Informe um número: "))
resultado = 1
while (fatorial > 1):
    resultado *= fatorial
    fatorial -= 1
    print(resultado)
'''

'''
numeros = [3,1, 7, 9, 4]
numero_max = max(numeros)
print ('O maior número é: ', numero_max)
'''

'''
numeros = [3, 1, 7, 9, 4]
maximo = 0

for numero in numeros:
    if numero > maximo:
        maximo = numero
print (maximo)
'''

'''
qntPessoasOpiniaoExcelente = 0
qntPessoasOpiniaoRuim = 0
qntPessoasOpiniaoBom = 0
qntPessoas = 3
somaIdades = 0
maiorIdade = 0

for i in range (3):
    idade = int(input("Informe sua idade: "))
    opiniao = int(input("Informe sua opinião (1 - 4): "))
    if(idade > maiorIdade):
        maiorIdade = idade

    if (opiniao == 3):
        somaIdades += idade
        qntPessoasOpiniaoBom += 1

    if (opiniao == 1 or opiniao == 2):
        qntPessoasOpiniaoRuim += 1

    if(opiniao == 4 and idade > 30):
        qntPessoasOpiniaoExcelente += 1

print ('Média da idade opinião 3:  ', somaIdades/qntPessoasOpiniaoBom)
print ('Quantidade de pessoas com opinião ruim ou regular: ', qntPessoasOpiniaoRuim)
print ('Quantidade de pessoas com opinião excelente: ', qntPessoasOpiniaoExcelente)
print ('Maior idade: ', maiorIdade)
'''

'''
qntPessoas = 3
somaValores = 0
qntItem1827 = 0
maiorValor = 0
anoItemValioso = 0
for i in range (qntPessoas):
    valor = float(input('Digite um valor: '))
    ano = int(input('Informe o ano: '))
    if(valor > maiorValor):
        maiorValor = valor
        anoItemValioso = ano
    somaValores += valor

    if(ano < 1827):
        qntItem1827 += 1

print('Quantidade de itens produzidos antes de 1827: ', qntItem1827)
print('Valor médio: ', somaValores/qntPessoas)
print('Ano do item mais valioso: ', anoItemValioso)
'''

'''
numerador = int(input('Digite um número: '))
for i in range (11):
    print('{} x {} = {:2}'.format(numerador, i, numerador*i))
'''

'''
linhas = int(input('Quantidade de linhas: '))
colunas = int(input('Quantidade de colunas: '))

for i in range(linhas):
    print("#" * colunas)
'''

'''
for h in range(24):
    for m in range(60):
        for s in range(60)
        print(h, m, s, sep = ":")
'''

'''
n1 = int(input('Digite um número: '))
lista = []

for i in range(n1):
    n2 = int(input('Digite um número: '))
    if n2 >= 0:
        lista.append(n2)
    else:
        break

n3 = int(input('Digite o seu número: '))
if (n3 in lista):
    print('Número encontrado!')
else:
    print('Se lascou!')
'''
