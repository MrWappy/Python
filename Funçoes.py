
def separador():
    print("******************")


separador()


# 1. Uma função que imprima “Hello World!”
def hello():
    print("Hello World!")


hello()

separador()


# 2. Uma função que receba um argumento, e imprima uma mensagem com esse argumento.

def argumento():
    arg = input("Introduza argumento: ")
    print("Bom dia, " + arg)


argumento()
separador()


# 3. Uma função que receba dois números como argumentos, calcule a soma e imprima esse resultado.
def soma(x, y):
    print(x + y)


soma(4, 7)
separador()


# 4. Uma função que receba dois números como argumentos, e devolva a soma ao programa principal. Imprima o resultado no programa principal
def soma2(x, y):
    res = x + y
    return res


print(f"{soma2(5, 7)}")
separador()


# 5. Uma função que receba 3 argumentos, e na chamada da função os argumentos sejam passados por uma ordem diferente
def menu(ent, ref, sob):
    print("o menu é: " + ref, ent, sob)


menu(ref="sopa", sob="mousse", ent="croquetes")
separador()


# 6. Uma função que receba uma lista como argumento e imprima todos os elementos dessa lista
def lista(lst):
    for x in lst:
        print(x)


lista(["João", "Inês", "José", "Carlos"])
separador()


# 7. Uma função que receba um número e devolva a soma desse número com os remanescentes até zero. (ex. recebe 5, devolve 5+4+3+2+1). (Sem recorrer a recursividade)

def soma(x):
    res = 0
    while x > 0:
        res = res + x
        x -= 1
    return res


print(soma(5))
separador()


# 8. Uma função que receba um número e devolva a soma desse número com os remanescentes até zero. (ex. recebe 5, devolve 5+4+3+2+1). (Com recursividade)
def soma_rec(x):
    if x == 1:
        return 1
    return (x + soma_rec(x - 1))


print(soma_rec(5))
separador()


# 9Utilizando recursividade desenvolva uma função que calcule o factorial de um dado número.
def fatorial_rec(x):
    if x == 1:
        return 1
    return (x * fatorial_rec(x - 1))


print(fatorial_rec(5))
# 10 Uma função que receba uma lista e devolva soma de todos os números dessa lista
soma = [2, 3, 7]


def lista(soma):
    for i in range(0, len(soma)):
        b = sum(soma)
    return b


print(lista(soma))


# 11 Uma função que receba uma string e devolva a string invertida (ex. “abcd” ->“dcba”)
def inverter(x):
    return x[::-1]


print(inverter("gosto de laranjas"))


# 12. Escreva uma função que aceita um número e verifica se esse número está entre 1000 e 1000000.
def verificar(x):
    if x > 1000 and x < 1000000:
        return True
    return False


print(verificar(2121))


# 13. Uma função que receba uma string e que calcule e imprima o número total de caracteres grandes e pequenos. (nota: tente utilizar uma estrutura de dados do tipo dicionário)

def n_upper_chars(string):
    dic = {
        "peq": "",
        "gra": ""
    }
    dic["peq"] = sum(map(str.islower, string))
    dic["gra"] = sum(map(str.isupper, string))
    dic.values()
    return dic.values()


print(n_upper_chars("Gosto buè de Um CHimapanzé"))


# 14 Uma função que receba uma lista e devolve uma lista com os elementos únicos da lista fornecida. (ex. [1,2,3,3,4,1] -> [1,2,3,4])
def unico(x):
    unico = list(dict.fromkeys(x))
    return unico


print(unico([1, 2, 3, 3, 4, 6, 6, 7]))


# 15. Uma função que receba uma lista e duas posições dessa lista para trocar os elementos dessa mesma lista (ex. a[2] -> a[3] e a[3] -> a[2])
def posições(x, p1, p2):
    temp = x[p1]
    x[p1] = x[p2]
    x[p2] = temp
    return x


print(posições([2, 6, 90, 312, 31], 2, 4))


# 16. Uma função que receba uma string e uma posição e devolva essa string sem o caracter da posição indicada.
def semcaracter(texto, posicação):
    p1 = texto[posicação]
    nova = texto.replace(texto[posicação], "")
    return nova


print(semcaracter("Ola Sou o João", 5))


# 17. Uma função que receba uma string e imprima as palavras que têm um número par de letras.
def parletras(x):
    nova_string = x.split()
    for i in range(0, len(nova_string)):
        if len(nova_string[i]) % 2 == 0:
            print(nova_string[i])


parletras("Bom Dia lola para imprimir")

# 18. Um script que tenha duas funções. Uma para calcular a área de um retângulo e outra para calcular o volume.
# A fórmula do cálculo de volume deverá utilizar a função do cálculo da área.
area = 0
vol = 0


def area_retangulo(c, l):
    area = c * l
    return area


print(area_retangulo(5, 9))


def vol_retangulo(c, l, h):
    vol = area_retangulo(c, l) * h
    return vol


print(vol_retangulo(5, 9, 7))

# 19. Uma função que imprima a hora e o dia
from datetime import datetime


def hora_dia():
    return datetime.now()


print(hora_dia())
