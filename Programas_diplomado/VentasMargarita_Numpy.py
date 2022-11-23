

# Nota: Instalar la libreria Numpy antes de correr el programa
import numpy as np

# Listas y variable ques se usaran
can,val,ref,total=[],[],[],[]
T=7
dia=["Lunes","Martes","Miércoles","Jueves","Viernes"]

# Datos predefinidos para ingreso automatico
# l0 = [6,7,8,9,10,11,12]
# l1 = [1,2,3,4,5,6,7]
# l2 = [2,2,2,2,2,2,2]
# l3 = [7,6,5,4,3,2,1]
# l4 = [3,3,3,3,3,3,3]
# l5 = [2,3,2,3,2,3,8]

# Iniciador de las listas
for i in range(T):
    can.append(0)
    val.append(0)
    ref.append(0)
    total.append(0)

# Iniciador de arrays
cant = np.array([can])
valo = np.array([can])

# Medoto para capturar los datos
def captura():
    global cant
    global valo
    x = 0
    for i in dia: # En cada día
        canti = cantidades(i) # Se obtienes las cantidades vendidas por referencia
        cant = np.insert(cant, x, canti.copy(),axis=0) # Se adiciona las cantidades obtenidas al array de cantidades
        valo = np.insert(valo, x,ventas(canti.copy()),axis=0) # Se obtiene y adiciona las ventas obtenidas al array de ventas
        x += 1
    if cant.shape == (len(dia)+1,T): # Se remueve la lista con el que se inicializó el array 
        cant = np.delete(cant,len(dia),axis=0)
    if valo.shape == (len(dia)+1,T): # Se remueve la lista con el que se inicializó el array 
        valo = np.delete(valo,len(dia),axis=0)
    

# Metodo para obtener las cantidades por referencia de un día
def cantidades(d):
    for i in range (T):
        # can[i] = l1[i] if d=='Lunes' else l2[i] if d=='Martes' else l3[i] if d=='Miércoles' else l4[i] if d=='Jueves' else l5[i] # Es para colocar los datos de las listas predefinidas
        can[i]=int(input(f"Digite la cantidad de ventas de la referencia {i+1} de papa frita para el día "+d+" ")) # Es para colocar los datos manualmente
    return can

# Metodo para obtener los valores unitarios de cada referencia
def valores():
    for i in range (T):
        # val[i] = l0[i] # Es para colocar los datos de la lista predefinida
        val[i]=int(input(f"Digite valor unitario de la referencia {i+1} de papa frita ")) # Es para colocar los datos manualmente
    return val

# Metodo para calcular las ventas totales por cada referencia
def ventas(cant):
    for i in range (T):
        total[i]=cant[i]*val[i]
    return total

# Metodo para mostrat los resultados del programa
def mostrar():
    suma_dia = np.sum(valo, axis=1) # Suma de valores por día
    suma_ref = np.sum(valo, axis=0) # Suma de valores por referencia
    print("\nLas ventas de la semana por referencia fueron:")
    for i in range(T):
        print(f"Referencia {i+1}: {suma_ref[i]}") # Muestra el total por referecia
    print("\nLas ventas de la semana por día fueron:")
    n = 0 # Contador para los días
    for i in dia:
        print(f"{i}: {suma_dia[n]}") # Muestra totales por día
        n += 1
    maxi = np.max(valo) # Obtiene el valor máximo de las ventas en todas las referencias en todos los días
    mini = np.min(valo) # Obtiene el valor mínimo de las ventas en todas las referencias en todos los días
    loc_maxi = np.where(valo == maxi) # Obtiene la(s) ubicación(es) de valor máximo
    loc_mini = np.where(valo == mini) # Obtiene la(s) ubicación(es) de valor mínimo
    if len(loc_maxi[0]) == 1: #Cuando solo se obtiene la ubicación de un valor máximo 
        print(f"\nLa venta mayor fue por un valor de {maxi} realizada el día {dia[loc_maxi[0][0]]} y para la referencia {loc_maxi[1][0]+1}") # Se muestra la informacion de valor máximo
    else: # Cuando se encuentra más de un valor máximo en el array
        dias = ""
        refs = ""
        for i in range(len(loc_maxi[0])): # Para cada localización
            dias += f" {dia[loc_maxi[0][i]]}," # Se obtiene el día y de concatena
            refs += f" {loc_maxi[1][i]+1}," # Se obtiene la referencia y se concatena
        dias = "(" + dias[1:-1] + ")"
        refs = "(" + refs[1:-1] + ")"
        print(f"\nLa venta mayor fue por un valor de {maxi} realizada los dias {dias} y para las referencias {refs}") # Se muestra la informacion de los valores máximos
        
    if len(loc_mini[0]) == 1: #Cuando solo se obtiene la ubicación de un valor mínimo
        print(f"\nLa venta menor fue por un valor de {mini} realizada el día {dia[loc_mini[0][0]]} y para la referencia {loc_mini[1][0]+1}\n") # Se muestra la informacion de valor mínimo
    else: # Cuando se encuentra más de un valor mínimo en el array
        dias = ""
        refs = ""
        for i in range(len(loc_mini[0])): # Para cada localización
            dias += f" {dia[loc_mini[0][i]]}," # Se obtiene el día y de concatena
            refs += f" {loc_mini[1][i]+1}," # Se obtiene la referencia y se concatena
        dias = "(" + dias[1:-1] + ")"
        refs = "(" + refs[1:-1] + ")"
        print(f"\nLa venta menor fue por un valor de {mini} realizada los dias {dias} y para las referencias {refs} respectivamente\n") # Se muestra la informacion de los valores mínimos

# Metodo para mostrar el título
def titulo():
    print("===== Ventas de productos Margarita =====")
    
# Metodo para mostrar el mensaje final
def salir():
    print("===== Fin del informe =====")

# Metodo main del programa para ejecutar los diferentes que se necesitan para mostrar el resultado
def main():
    titulo()
    valores()
    captura()
    #print(val)
    #print(dia)
    #print(cant)
    #print(valo)
    mostrar()
    salir()   

# Iniciador del metodo main
main()