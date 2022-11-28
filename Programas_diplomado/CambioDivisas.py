"""
Actividad 2
Cambio de divisas

Estudiantes: 
Alberson Johan Sánchez Garavito
Andrés Ricardo Fraile Blanco
Mar Zein Biscunda Quintana

Corporación Unificada Nacional De Educación Superior (CUN)
Ficha: 60101, 
Diplamado Machine learning en Python
Docente: Ing. Luis Enrique Camargo Camargo
Noviembre 26 del 2022

"""

# Tipos de transacciones posible
tipos = ['Compra','Venta']
# Matriz de monedas y cambios a USD
# USD es la modena base para cualquier transacción
# Tasas tomadas de Forex del día 24 de noviembre
divisas = {'Dólar estadounidense':('USD',1,'$'),
                 'Peso colombiano':('COP',4901.56, '$'),
                 'Euro':('EUR',0.96079, '€'),
                 'Libra esterlina':('GBP',0.82671, '£'),
                 'Yen':('JPY',139.23, '￥')}
# Colección de ganancias
ganancias = set()
# Tipo de transacción seleccionada
transaccion = 0
# Primera divisa seleccionada
divisa1 = ''
# Segunda divisa seleccionada
divisa2 = ''
# Cantidad de divisa objeto de la transacción
cantidadParaTransaccion = 0

# Método principal e iniciador del programa
def inicioTransaccion():
    # Se ajusta el alcance de las variables para ser usadas en el método
    global transaccion
    global cantidadParaTransaccion
    # Variables apoyo del método
    texto = ''
    counter = 1
    # Se muestra encabezado de la interacción
    print("***************************************")
    print("Que tipo de transacción desea realizar?")
    print("***************************************")
    #Se recorre los tipos para mostrarlos en pantalla
    for tipo in tipos:
        print(f"{counter}. {tipo}")
        counter += 1
    # Se adiciona la opción de obtener ganancia y terminar el programa
    print(f"{counter}. Cerrar día y salir")
    transaccion = int(input("Digite una opción: "))
    # Se revisa la selección para que se valida en caso de 
    # escoger venta o compra solicita la cantidad a cambiar
    tipoTrans = tipos[transaccion-1].lower() if transaccion == 1 else "vende"
    if transaccion == 1 or transaccion == 2:        
        i = 0 # Indicador para repetición
        while i < 1: # Se repite el código hasta que se obtenga un numero
            try:
                # Se captura el valor y se intenta convertir a float
                temp = float(input(f"\nDigite la cantidad que desea {tipoTrans}r: "))
                if isinstance(temp,float):
                    cantidadParaTransaccion = temp
                    seleccioneDivisa(1)
                    break
            # Si la conversion a float genera un error se muestra un mensaje
            # y se repite el while para solictar el valor
            except ValueError:
                print("\n**** El valor ingresado no es valido. Por favor intentelo de nuevo ****")
    elif transaccion == 3:
        calcularGananciasDia()
    else:
        print("\nLa selección es erronea, por favor intente nuevamente")
        inicioTransaccion() 

    # Esta sección es por si se tiene Python con version mayor o igual 3.10 y reemplazar
    # por el condicional previo
    # match transaccion:
    #     # En caso de compra o venta se solicita
    #     # la cantidad que desea obtener o vender según sea el caso
    #     case 1 | 2:
    #         i = 0 # Indicador para repetición
    #         while i < 1: # Se repite el código hasta que se obtenga un numero
    #             try:
    #                 # Se captura el valor y se intenta convertir a float
    #                 temp = float(input(f"\nDigite la cantidad que desea {tipos[transaccion-1].lower()}r: "))
    #                 if isinstance(temp,float):
    #                     cantidadParaTransaccion = temp
    #                     seleccioneDivisa(1)
    #                     break
    #             # Si la conversion a float genera un error se muestra un mensaje
    #             # y se repite el while para solictar el valor
    #             except ValueError:
    #                 print("\n**** El valor ingresado no es valido. Por favor intentelo de nuevo ****")     
    #     # Cuando escoge cerrar día y salir se llama la función
    #     # para calcular las ganancias del día
    #     case 3:
    #         calcularGananciasDia()
    #     # Si escoge una opción diferente, se muestra mensaje
    #     # y se inicia la transacción nuevamente
    #     case _:
    #         print("\nLa selección es erronea, por favor intente nuevamente\n")
    #         inicioTransaccion() 
    
# Método para seleccionar las divisas para la transacción
def seleccioneDivisa(indic):
    # Se ajusta el alcance de las variables para ser usadas en el método
    global divisa1
    global divisa2
    # Se obtiene un list de las divisas
    nombreDivisas = list(divisas.keys())
    # Variables apoyo del método
    counter = 1
    indiceDivisa1 = 0
    tipo = tipos[transaccion-1].lower() if transaccion == 1 else "vende"
    # Se muestra encabezado de la interacción
    print(f"\nQue divisa desea {tipo}r" if indic == 1 else f"\nA cambio de que divisa")
    print("********************************" if indic == 1 else "***********************************")
    # Se recorre la divisas para mostracelas al usuario
    for key in nombreDivisas:
        # Si es la segunda divisa y no es la primera seleccionada, 
        # no se muestra y se guarda el indice
        if indic == 2 and key == divisa1:
            indiceDivisa1 = counter
        # En caso contrario se muestra la divisa
        else:
            print(f"{counter}. {key}")
            counter += 1
    # se obtiene la selecci{on del usuario}
    opc = int(input("Digite su opción: "))
    
    # Se valida que la opción seleccionada se valida
    # Si no es una opción valida se muestra un mensaje 
    # y se reinicia la selección de divisa
    if opc >= counter:
        print("No es una opción válida, por favor intente nuevamente")
        seleccioneDivisa(indic)
    # Cuando la opción si es válida
    else:
        # Si es la primera divisa se guarda en la variable
        # y se solicita la segunda divisa
        if indic == 1:
            divisa1 = nombreDivisas[opc-1]
            seleccioneDivisa(2)
        # Si es la segunda divisa, se ajusta el índice si esta opción es mayor de
        # la primera selección para obtener el índice real, se guarda la selección
        #  y se llama el método para calcular el cambio
        else:
            opc = opc if opc >= indiceDivisa1 else opc-1
            divisa2 = nombreDivisas[opc]
            calcularCambio()
        
# Método para calcular
def calcularCambio():
    resultado = 0
    ganancia = 0
    # Cuando alguna de las divisas es USD solo se hace una operación
    if divisas.get(divisa1)[0] == 'USD' or divisas.get(divisa2)[0] == 'USD':
        # Para calculos cuando la segunda divisa es USD
        if divisas.get(divisa1)[0] == 'USD':
            # Calculo de venta de UDS desde otra moneda donde  
            # el costo de USD es 2% menor a la tasa definida
            # Se calcula la ganancia y se convierte en USD
            if tipos[transaccion-1] == 'Venta':
                resultado = round(cantidadParaTransaccion * divisas.get(divisa2)[1] * 0.98)
                ganancia = (cantidadParaTransaccion * divisas.get(divisa2)[1] - resultado)/divisas.get(divisa2)[1]
            # Calculo de compra de UDS a otra moneda donde  
            # el costo de USD es 2% mayor a la tasa definida
            # Se calcula la ganancia y se convierte en USD
            else:
                resultado = round(cantidadParaTransaccion * divisas.get(divisa2)[1] * 1.02)
                ganancia = (resultado - (cantidadParaTransaccion * (divisas.get(divisa2)[1])))/divisas.get(divisa2)[1]
        # Para calculos cuando la primera divisa es USD
        else:
            # Calculo de venta de otra moneda desde USD donde 
            # el costo de USD es 2% menor a la tasa definida
            # Se calcula la ganancia en USD
            if tipos[transaccion-1] == 'Venta':
                resultado = round((cantidadParaTransaccion / divisas.get(divisa1)[1])*0.98)
                ganancia = (cantidadParaTransaccion / divisas.get(divisa1)[1]) - resultado
            # Calculo de compra de UDS a otra moneda donde  
            # el costo de USD es 2% mayor a la tasa definida
            # Se calcula la ganancia en USD
            else:
                resultado = round((cantidadParaTransaccion / (divisas.get(divisa1)[1])*1.02))
                ganancia = resultado - (cantidadParaTransaccion / (divisas.get(divisa1)[1]))
    # Cuando ninguna de las divisas es USD
    else:
        # Cálculo de venta de entre monedas diferentes a USD donde 
        # se realiza el cambio de la primera divisa a USD y 
        # de USD a la segunda moneda y el costo de la segunda 
        # divisa es 2% menor a la tasa definida
        # Se calcula la ganancia en USD
        if tipos[transaccion-1] == 'Venta':
            resultado = round(((cantidadParaTransaccion / divisas.get(divisa1)[1]) * divisas.get(divisa2)[1]) * 0.98)
            ganancia = (((cantidadParaTransaccion / divisas.get(divisa1)[1]) * divisas.get(divisa2)[1]) - resultado) / divisas.get(divisa2)[1]
        # Calculo de compra de entre monedas diferentes a USD donde 
        # se realiza el cambio de la segunda divisa a USD y 
        # de USD a la primera moneda y el costo de la primera 
        # divisa es 2% mayor a la tasa definida
        # Se calcula la ganancia en USD
        else:
            resultado = round(((cantidadParaTransaccion / divisas.get(divisa1)[1]) * divisas.get(divisa2)[1]) * 1.02)
            ganancia = (resultado - ((cantidadParaTransaccion / divisas.get(divisa1)[1]) * divisas.get(divisa2)[1])) / divisas.get(divisa2)[1]
    # Se muestra el encabezado del resultado de la transacción
    print(f"\nEl resutado de la {tipos[transaccion-1].lower()}")
    print("====================================")
    # Cuando la transacción es venta se muestra el resultado con los datos calculados
    if tipos[transaccion-1] == 'Venta':
        print(f"Entregó {divisas.get(divisa1)[2]}{cantidadParaTransaccion:,.2f} {divisa1} ({divisas.get(divisa1)[0]})")
        print(f"Se cambió por {divisas.get(divisa2)[2]}{resultado:,.2f} {divisa2} ({divisas.get(divisa2)[0]})")
    # Cuando la transacción es compra se muestra el resultado con los datos calculados
    else:
        print(f"Va a recibir {divisas.get(divisa1)[2]}{cantidadParaTransaccion:,.2f} {divisa1} ({divisas.get(divisa1)[0]})")
        print(f"Debe entregar {divisas.get(divisa2)[2]}{resultado:,.2f} {divisa2} ({divisas.get(divisa2)[0]})")
    print("\nFin de la transacción!!\n")
    # se adiciona la ganancia a la colección
    ganancias.add(ganancia)
    # print(ganancias)
    inicioTransaccion()
    ganancia = 0

# Método para calcular y mostrar las ganancias del día
def calcularGananciasDia():
    total = 0
    for transaccion in ganancias:
        total += transaccion
    print("\nCierre del día")
    print("===============")
    print("Se realizaron {} transacciones".format(len(ganancias)),)
    print("El total de las ganancias fue de {}{:,.2f} {} ({}).\n".format(divisas.get(list(divisas.keys())[0])[2], total, list(divisas.keys())[0],divisas.get(list(divisas.keys())[0])[0]))
    
# Llamada del m{etodo para iniciar el programa
inicioTransaccion()
