import random
print("----------COMENZAMOS----------")
print()

#Paso 1: pedimos al usuario el numero de jugadores.

numero_jugadores : int = int(input("Escribe el numero de jugadores: "))
print("------------------------------")
print()

#Paso 2: Crear diccionario de jugadores.

listado_jugadores : dict = {}

for jugador in range(numero_jugadores):
    
    listado_jugadores.update({f"JUGADOR{jugador+1}": [-1, -1, -1, -1, -1, -1]})
   
print(listado_jugadores)
print("------------------------------")
print()

#Paso 3: Super bucle.

for turno in range(6):
    for nombre_jugador,value in listado_jugadores.items():
        
        print(f"Turno de {nombre_jugador}")
        print("------------------------------")
        print()
        
        cara_dados : list = [1, 2, 3, 4, 5, 6]
        cara = 0
        dados_iniciales = 5
        dados = dados_iniciales
 
        for tirada in range(3):
            tirada_1_lista = []
            for d in range(dados):
                tirada_1 = random.choice(cara_dados)
                tirada_1_lista.append(tirada_1)
        
            print(f"Dados = {tirada_1_lista}")
            print("------------------------------")
            print()

            
#Aqui si eliges la cara equivocada puedes repetir solo 3 veces ya que el bucle de tiradaes range(3)
            
            if tirada == 0:

                eleccion_cara = int(input("Elige la cara del 1 al 6: "))
                                      
                while eleccion_cara not in [1,2,3,4,5,6] or listado_jugadores[nombre_jugador][eleccion_cara -1] != -1:
                    print(f"Esta cara ya ha sido elegida, prueba otra.")
                    print("------------------------------")
                    print()
                    
                    eleccion_cara = int(input("Elige la cara del 1 al 6: "))
                
                print(f"La cara elegida es: {eleccion_cara}")
                print("------------------------------")
                print()

            cara = tirada_1_lista.count(eleccion_cara)
            print(f"Número de caras: {cara}")
            print("------------------------------")
            print()

            dados = dados - cara

            caras_validas = dados_iniciales - dados
            print(f"Total de caras: {caras_validas}")
            print("------------------------------")
            print()

#Elegimos la cara con la que jugamos y añadimos al diccionario del jugador.
        
        listado_jugadores[nombre_jugador][eleccion_cara -1] = caras_validas * eleccion_cara
        
        print(listado_jugadores)
        print("------------------------------")
        print()

#Paso 4: Aqui se suma todos los valores de cada jugador.
        
nombre_ganador = ""
total_ganador = 0

for jugador, puntuaciones in listado_jugadores.items():
    valores = sum(puntuaciones)

    print(f"La puntuacion total del: {jugador} es: {valores}")
    print("------------------------------")
    print()

    if valores > total_ganador:
        nombre_ganador = jugador
        total_ganador = valores

print(f"EL GANADOR DE LA PARTIDA ES: {nombre_ganador} CON UN TOTAL DE: {total_ganador} ")
print()

print("------------------------------")
print()

print("----------¡¡ENHORABUENA!!----------")
print()
print()
