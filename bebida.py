from data_option import tamano, tamano_name, ingrediente, ingrediente_name, bebida, bebida_name
from logo import logo_exit
from time import sleep 
from factura import factura

def menu_bebida(monto, pedido, num_pizza):
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
            print("\t=> Debe seleccionar el tamaño correcto!!") # En caso de que se ingrese un caracter erroneo, se le notificara al usuario

