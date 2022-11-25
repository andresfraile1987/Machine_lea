trms = {'Euro':5151.98, 'Dollar':4989.12, 'Yen':34.75, 'Rublo':80.88, 'Mxn':252.43}
divisas = {'Euro':'€', 'Dollar':'US$', 'Yen':'¥', 'Rublo':'₽', 'Mxn':'MX$'}

def captura(divisa):
    if divisa.title() in divisas:
        print("\n Desea comprar ",divisa.title(), divisas[divisa])
        
def trm(valor):
    if valor.title() in trms:
        return trms[valor]


def valor(monto, valor):
    return valor * monto

def calculo(divisa):
    divisa.title() in divisas
    val = trm(divisa)
    monto = float(input(f'\n Ingresa la cantidad de {divisa.title()} que quieres comprar: ',))
    result = valor(monto, val)
    print('\n ${} COP son {} {} {} \n'.format(monto,divisas[divisa],round(result,2),divisa.title()))

def salida():
    print('\n Hasta Pronto \n')

def error():
    print("La divisa no está en nuestra base de datos. intente de nuevo")

def menu():
    opc = 1
    while(opc != 6):
        print("Calculadora de divisas")
        print("============")
        print("1. Euro")
        print("2. Dollar")
        print("3. Yen")
        print("4. Rublo")
        print("5. Peso mexicano")
        print("6. Salir")
        opc=int(input("Digite su opción: "))
        match(opc):
            case 1:
                div = 'Euro'
                captura(div)
                calculo(div)
            case 2: 
                div = 'Dollar'
                captura(div)
                calculo(div)
            case 3: 
                div = 'Yen'
                captura(div)
                calculo(div)
            case 4: 
                div = 'Rublo'
                captura(div)
                calculo(div)
            case 5:
                div = 'Mxn'
                captura(div)
                calculo(div)
            case 6:
                salida()
            case other:
                error()

menu()