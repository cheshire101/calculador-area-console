import math

base=0
base2=0
altura=0
lado=0
raio=0
diagonalMaior=0
diagonalMenor=0
resultado=0
calculo=''

def triangulo():
    base=float(input('Digite a base: '))
    altura=float(input('Digite a altura: '))
    resultado = (base*altura)/2
    print(str(base) + ' * ' + str(altura) + ' / 2' + ' = ' + str(resultado))
    print('a altura do triangulo é: ' + str(resultado))

def retangulo():
    base=float(input('Digite a base: '))
    altura=float(input('Digite a altura: '))
    resultado = (base*altura)
    print(str(base) + ' * ' + str(altura) + ' = ' + str(resultado))
    print('a altura do retangulo é: ' + str(resultado))

def quadrado():
    lado=float(input('digite o lado: '))
    resultado = lado * lado
    print(str(lado) + ' * ' + str(lado) + ' = ' + str(resultado))
    print('a area do quadrdo é: ' + (str(resultado)))

def trapezio():
    base=float(input('Digite a primeira base: '))
    base2=float(input('Digite a sugunda base: '))
    altura=float(input('Digite a altura: '))
    resultado = (base + base2)*altura/2
    print(str(base) + '+' + str(base2) + ' * ' + str(altura) + ' / 2 ' + ' = ' + str(resultado)) 
    print('a area do trapezio é: ' + (str(resultado)))

def losango():
    diagonalMaior=float(input('Digite a diagonal maior: '))
    diagonalMenor=float(input('Digite a diagonal menor: '))
    resultado=(diagonalMaior*diagonalMenor)/2
    print(str(diagonalMaior) + ' * ' + str(diagonalMenor) + ' / 2 ' + ' = ' + str(resultado))
    print('A area do losango é: ' + (str(resultado)))

def  circulo():
    raio=float(input('Digite o valor do raio: '))
    resultado = (raio ** 2) * math.pi  # Calcula a área do círculo
    # Exibe a fórmula de cálculo com o valor
    print(f'pi * {raio} ^ 2 = {resultado:.2f}')
    # Exibe o resultado formatado com duas casas decimais
    print(f'A área do círculo é: {resultado:.2f}')
    print(f'pi * {raio} ^ 2 = {resultado:.2f}')
    print(f'A área do círculo é: {resultado:.2f}')
        #peguei no chat pq nao funcionou com as funcoes anteriores.  

calculo=input(str('Digite a Operacao (1-Triangulo, 2-Retangulo, 3-Quadrado, 4-Trapezio, 5-Losango, 6-Circulo): '))

if calculo == '1':
    triangulo()

elif calculo == '2':
     retangulo()

elif calculo == '3':
    quadrado()

elif calculo == '4':
    trapezio()

elif calculo == '5':
    losango()

elif calculo == '6':
    circulo()

else:
    print('erro, digite uma operação valida.')