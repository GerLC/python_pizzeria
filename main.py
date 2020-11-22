import sys
from time import sleep 
from logo import logo
from data_option import tamano, tamano_name, ingrediente, ingrediente_name
from bebida import menu_bebida



## MI PROYECTO

# Variables Globales
num_pizza = 1       # Numero de pizzas que el usuario solicita
monto_total = 0     # Monto total final
pedido = []

def menu_opciones(num_pizza):
    '''
    Muestra las opciones del tamaño
    EL usuario se le presentaran 3 opciones (g, m y p)
    Debera escoger uno para empezar el pedido
    Una vez escogido un tamaño guardara el monto_total el valor de la pizza escogida
    y va al siguiente procedimiento, agregar los ingredientes

    En caso de ingresar una opcion no valida, mostrara un mensaje indicando el error
    y volvera a iniciar
    '''
    logo()
    print("Pizza numero ",num_pizza)
    print("Tamaño: clave - precio")
    for x,y,z in zip(tamano_name.values(), tamano, tamano.values()):     # En este for, se recorre y se toman las variables para imprimir
        print(x, "(", y, ")",z," ", end=' ')                             # las opciones de los tamaños disponibles
    opcion_tamano = input("\nIntroduzca clave del tamaño: ")

    if opcion_tamano.lower() in tamano:
        monto = tamano[opcion_tamano]
        menu_ingredientes(opcion_tamano,monto)
    else:
        print("=> Debe seleccionar el tamaño correcto!!")
        menu_opciones(num_pizza)


def menu_ingredientes(tamano_pizza,monto):
    '''
    Muestra las opciones de los ingredientes

    EL usuario se le presentaran una lista de ingredientes
    Estos ingredientes tienen una clave al lado (ja, sa, pe, etc.)
    Podra agregar los ingredientes que quiera escribiente la clave
    Una vez terminado, solo debe presionar Enter sin ingresar nada para proseguir


    En caso de ingresar una opcion no valida, mostrara un mensaje indicando el error
    pero podra seguir con la seleccion de ingredientes para agregar
    '''
    lista_ingredientes = []      # Lista de ingredientes para guardarlo en una lista
    opcion = "1"                 # Opcion es una variable para no salirse del loop sin que se cumpla la condicion
    print()
    print("Ingredientes: clave")
    for x,y,z in zip(ingrediente_name.values(), ingrediente,ingrediente.values()):       # En este for, se recorre y se toman las variables para imprimir
        print(x, "  (", y, ") ",z)                                                        # las opciones de los ingredientes disponibles

    print("\n")
    while opcion != "":
        opcion = input('Indique clave del ingrediente (enter para terminar): ')

        if opcion.lower() in ingrediente:
            monto = monto + ingrediente[opcion]
            lista_ingredientes.append(opcion)
        elif opcion == "":
            resumen(tamano_pizza,monto,lista_ingredientes)
        else:
            print("\t=> Debe seleccionar el tamaño correcto!!") # En caso de que se ingrese un caracter erroneo, se le notificara al usuario
            sleep(1)


def resumen(tamano_pizza,monto_pizza,ingrediente_pizza):
    '''
    Muestra el resumen del orden de la pizza con sus ingredientes y monto y
    le pregunta al usuario si desea otra pizza o no

    El sistema carga los datos de la pizza muestra la pizza con sus ingredientes y monto
    Se le presente una opcion [s,n]
    s: O si para pedir otra pizza, iniciara otra vez la funcion menu_opcion(num_pizza) para pedir una nueva pizza
       num_pizza sumara un valor para indicar el numero de pizza de la orden
    n: O no para terminar la transaccion, mostrara al usuario final la cantidad de pizzas pedidas y el monto total.
       Calcula el monto de todas las pizzas con sus ingredientes solicitados.
    '''

    # Las variables global, son necesarios para modificar una variable global que hayamos definino anteriormente
    global num_pizza
    global monto_total
    global pedido


    opcion = ""
    monto_total = monto_total + monto_pizza # Monto total, es una variable global que ira guardando el monto. Cada vez que se agregue una pizza nueva
                                            # se le sumara al monto_total con el monto_pizza la cual es el valor de la pizza individual actual.
    monto_descuento = 0

    # En esta seccion se lista la pizza actual con sus ingredientes, y el monto o subtotal solo de esa pizza
    # En caso de no haber ingredientes, la pizza se le llamara Margarita.
    
    if not ingrediente_pizza:
        print("\nUsted seleccionó una pizza ", tamano_name[tamano_pizza], " Margarita")
        print("\nSubtotal a pagar por una pizza ", tamano_name[tamano_pizza], ": ", monto_pizza)
        pedido.append([tamano_name[tamano_pizza],'Sin ingredientes',monto_pizza])
    else:
        print("\nUsted seleccionó una pizza ", tamano_name[tamano_pizza], " con ", 
        *[ingrediente_name[x] for x in ingrediente_pizza], sep="-")                                # List Compression de ingredientes,
        print("\nSubtotal a pagar por una pizza ", tamano_name[tamano_pizza], ": ", monto_pizza)   # aqui en el dictionary defini los valores para obtener el nombre completo del objeto
        pedido.append([tamano_name[tamano_pizza],*[ingrediente_name[x] for x in ingrediente_pizza],monto_pizza])

    while opcion != "n":
        print("\n***********************")
        opcion = input("¿Desea continuar [s/n]?:")
        print("***********************\n")

        if opcion == "n":
            print("El pedido tiene un total de ", num_pizza, " pizza(s) por un monto de ", monto_total)
            print("Cargando...")
            sleep(3)
            menu_bebida(monto_total, pedido, num_pizza)

            print("\nGracias por su compra, regrese pronto")
            sleep(1)
            sys.exit()
        elif opcion == "s":
            sleep(1)
            num_pizza = num_pizza + 1    # En caso de solicitar otra pizza, se le suma la variable global +1
            menu_opciones(num_pizza)     # Seguido de eso, se llama la funcion inicial, indicando el num_pizza como parametro
        else:
            print("=> Debe seleccionar una opcion valida!!")

menu_opciones(num_pizza)
