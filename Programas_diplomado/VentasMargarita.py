
# Listas y variable necesaria para el programa
can,val,ref,total=[],[],[],[]
max, min = [0,0],[1000000,0]
T=7
# Diccionarios para guardar los datos por día 
dia={"Lunes":[0,],"Martes":[0,],"Miércoles":[0,],"Jueves":[0,],"Viernes":[0,]}
# Inciador de las listas
def inicializar():
    for i in range(T):
        can.append(0)
        val.append(0)
        ref.append(0)
        total.append(0)

# Datos predefinidos para ingreso automatico
l0 = [6,7,8,9,10,11,12]
l1 = [1,2,3,4,5,6,7]
l2 = [2,2,2,2,2,2,2]
l3 = [7,6,5,4,3,2,1]
l4 = [3,3,3,3,3,3,3]
l5 = [2,3,2,3,2,3,8]
    
# Metodo para obtener los valores por cada referencia
def valores():
    for i in range (T):
        val[i] = l0[i] # Es para colocar los datos de la lista predefinida
        # val[i]=int(input(f"Digite el valor unitario de la referencia {i+1} de papa frita ")) # Es para colocar los datos manualmente
    return val

# Metodo para capturar los datos
def captura():
    for i in dia: # Por cada día
        can = cantidades(i) # Se obtienen las cantidades vendidas por cada referencia
        dia[i]=[can.copy()] # Se adicionan las cantidades por referencia a cada día
        ventas_dia = list(ventas(can.copy(),val)) # Se obtienen las ventas por referencia
        dia[i].append(ventas_dia.copy()) # Se adiciona el total de ventas por referencia
        dia[i].append(totaldia(ventas_dia.copy())) # Se obtiene y adiciona total de ventas del día
        referenecias(ventas_dia.copy()) # Se adicionan la ventas del día a cada referencia
        minmax(i,ventas_dia.copy()) # Se valida si el valor mínimo y máximo cambios con los datos del día
        
# Metodo para las cantidades vendidas por referencia del cada día
def cantidades(d):
    for i in range (T):
        can[i] = l1[i] if d=='Lunes' else l2[i] if d=='Martes' else l3[i] if d=='Miércoles' else l4[i] if d=='Jueves' else l5[i] # Es para colocar los datos de las listas predefinidas
        # can[i]=int(input(f"Digite la cantidad de ventas de la referencia {i+1} de papa frita para el día "+d+" ")) # Es para colocar los datos manualmente
    return can

# Metodo para obtener el acumilativo las ventas de la semana por referencia
def referenecias(valor):
    for i in range(T):
        ref[i] += valor[i]

# Metodo para obtener el valor de ventas por referencia del día
def ventas(cant,valor):
    for i in range (T):
        total[i]=cant[i]*valor[i]
    return total

# Metodo para obtener el acumilativo las ventas por día
def totaldia(venta):
    total_dia = 0
    for i in range(T):
        total_dia += venta[i]
    return total_dia
# Metodo para obtener el valor mínimo y máximo de ventas de la semana
def minmax(d,venta):
    global min # Llamado de la variable global min en el alcance del metodo
    global max # Llamado de la variable global max en el alcance del metodo
    for i in range(T): # Por cada referencia
        if venta[i] <= min[0]: # Valida si el valor de la venta de la referencia es menor al que tiene la variable almacenada
            min = [venta[i],i+1,d] # Se reemplazan los datos de la variable global (Valor, Referencia y Día)
        if venta[i] >= max[0]: # Valida si el valor de la venta de la referencia es mayor al que tiene la variable almacenada
            max = [venta[i],i+1,d] # Se reemplazan los datos de la variable global (Valor, Referencia y Día)
    

# Metodo para obtener, calcular y mostrar los datos requeridos
def mostrar():
    print("\nLas ventas de la semana por referencia fueron:")
    for i in range(T): # Por cada referencia
        print(f"Referencia {i+1}: {ref[i]}") # Se muestra el Id de la referencia y la venta total acumulada
    print("\nLas ventas de la semana por día fueron:")
    for i in dia: # Por cada día
        print(f"{i}: {dia[i][2]}") # Se muestra el Id de la referencia y la venta total acumulada
    print(f"\nLa venta mayor fue realizada el día {max[2]} por un valor de {max[0]} y para la referencia {max[1]}") # Se muestra la venta mayor junto con la referencia y el día en que se realizo
    print(f"\nLa venta menor fue realizada el día {min[2]} por un valor de {min[0]} y para la referencia {min[1]}") # Se muestra la venta menor junto con la referencia y el día en que se realizo

# Metodo para mostrar el título
def titulo():
    print("===== Ventas de productos Margarita =====")
    
# Metodo para mostrar el mensaje final
def salir():
    print("===== Fin del informe =====")
    
# Metodo para ejecutar los metodos necesarios para dar solucion al programa
def main():
    titulo()
    inicializar()
    valores()
    captura()
    #print(val)
    #print(ref)
    #print(total)
    #print(dia)
    #print(min)
    #print(max)

    mostrar()
    salir()
    
#Bloque principal
main()