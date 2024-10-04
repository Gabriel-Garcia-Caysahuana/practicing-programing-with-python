import time
import threading

def print_menu_opciones():
    print("""\nElegir opción:
          1. Realizar pedido
          2. Salir del sistema\n""")
    
def print_tipo_cafe():
    print("Tipo de café:")
    for key, value in tipos_cafe.items():
        print(f"{key}. {value}")

def preparar_cafe(tipo_cafe_elegido, nombre_cliente):
    global tipos_cafe
    global lista_pedidos

    print(f"\nPreparando {tipos_cafe[tipo_cafe_elegido]} de {nombre_cliente}...\n")

    time.sleep(30)
    print("\n----------------------------------------------------------\n")
    print(f"¡{tipos_cafe[tipo_cafe_elegido]} de {nombre_cliente} listo para entregar!")
    print("\n----------------------------------------------------------\n")
    lista_pedidos.append((nombre_cliente, tipo_cafe_elegido, 5))

def realizar_pedido():
        print_tipo_cafe()
        tipo_cafe_elegido = int(input("\nIngrese opción de tipo de café: \n"))

        if 0 < tipo_cafe_elegido < 6:
            nombre_cliente = input("\nIngrese nombre del cliente: \n")
            realiza_pedido = str(input("\nRealizar pedido Y(si) o N(no): \n"))

            if realiza_pedido == 'Y':
                hilo = threading.Thread(target = preparar_cafe, args= (tipo_cafe_elegido, nombre_cliente))
                hilo.start()

            elif realiza_pedido == 'N':
                print("\nSe cancela el pedido.\n")

            else:
                print("\nIngrese una de las dos opciones Y o N.\n")

        else:
            print("\nOpción fuera de rango. Vuelva a ingresar.\n")



tipos_cafe = {1:'Café expreso',
              2:'Cappuchino',
              3:'Café negro',
              4:'Café con leche',
              5:'Late'}

fin = False
lista_pedidos = []

print("\n---Cafeteria FANBOYS.SAC---")
while not fin:
    try:
        print_menu_opciones()
        opc = int(input("\nElegir opción: \n"))
        if opc == 1:
            realizar_pedido()
     

        elif opc == 2:
            print("\nSaliendo del programa...\n")
            time.sleep(1)
            print("...")
            time.sleep(1)
            for i in lista_pedidos:
                print(f"Cliente: {i[0]}, Pedido: {tipos_cafe[i[1]]}, tiempo: 30")
            print("...")
            time.sleep(1) 
            print(f"Timpo total: {len(lista_pedidos) * 30} segundos.")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("\n¡Hasta pronto!\n")
            fin = True
        
        else:
            print("\nElija una de las dos opciones mostradas.\n")


    except ValueError:
        print("\nError de valor: Ingrese un valor correcto.\n")