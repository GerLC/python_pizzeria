from data.data_option import tamano, tamano_name, ingrediente, ingrediente_name, bebida, bebida_name
from functions.logo import logo_exit
from time import sleep 
from functions.factura import factura

def menu_bebida(monto, pedido, num_pizza):
    '''
    Muestra las opciones de bebidas disponibles

    EL usuario se le presentaran una lista de bebidas
    Estas bebidas tienen una clave al lado 
    Podra agregar las bebidas que quiera escribiendo la clave
    Una vez terminado, solo debe presionar Enter sin ingresar nada para proseguir


    En caso de ingresar una opcion no valida, mostrara un mensaje indicando el error
    pero podra seguir con la seleccion de ingredientes para agregar

    '''
    lista_bebidas = []
    opcion = "1"
    monto_bebida = 0

    print("\n Desea pedir bebidas?")

    for x,y,z in zip(bebida_name.values(), bebida, bebida.values()):  # En este for, se recorre y se toman las variables para imprimir
        print(x, "  (", y, ") Precio: ", z)                              # las opciones de los ingredientes disponibles

    print("\n")
    while opcion != "":
        opcion = input('Indique clave de la bebida (enter para terminar): ')

        if opcion.lower() in bebida:
            monto_bebida = monto_bebida + bebida[opcion]
            lista_bebidas.append(opcion)
        elif opcion == "":
            
            if lista_bebidas:
                print("Bebidas: ", *[bebida_name[x] for x in lista_bebidas], sep=", ")
                print("Monto total por bebidas : ", monto_bebida)

                monto = monto + monto_bebida
                print("\n********************************************")
                print("Monto total a pagar completo total: ", monto)
                sleep(2)            
                factura(pedido,monto, [bebida_name[x] for x in lista_bebidas],monto_bebida, num_pizza)
                logo_exit()
            else:
                print("\n********************************************")
                print("Monto total a pagar completo total: ", monto)
                sleep(2)
                factura(pedido,monto, [bebida_name[x] for x in lista_bebidas],monto_bebida, num_pizza)
                logo_exit()
        else:
            print("\t=> Debe seleccionar clave correcto!!") # En caso de que se ingrese un caracter erroneo, se le notificara al usuario

