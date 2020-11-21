import os
import sys

## MI PROYECTO

tamano = {"g":580, "m":430, "p":280}    # Diccionario con tamanos de pizza y precio
tamano_name = {"g":"Grande", "m":"Mediana", "p":"Personal"} # Diccionario con el nombre o palabra para incluir el nombre completo

ingrediente = {"ja": 40, "ch": 35, "pi": 30, "dq": 40, "ac": 57.5, "pe": 38.5, "sa": 62.5} # Diccionario con ingredientes y precio
ingrediente_name = {"ja": "Jamon", "ch": "Champinones", "pi": "Pimenton", "dq": "Doble_queso",  # Diccionario con el nombre o palabra
                "ac": "Aceitunas", "pe": "Pepperoni", "sa": "Salchichon"}                       # para incluir el nombre completo

num_pizza = 1       # Numero de pizzas que el usuario solicita
monto_total = 0     # Monto total final


def logo():
    '''
    El display del logo para mostrarlo cada vez que inicia el menu
    '''
    print()
    print("************************")
    print("*    PIZZERIA UCAB     *")
    print("*   La mejor Pizza !   *")
    print("************************")
    print()

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
    opcion_tamano = input("Tamaños: Grande ( g ) Mediana ( m ) Personal ( p ): ")

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
    lista_ingredientes = []  #Lista de ingredientes para guardarlo en una lista
    opcion = "1"
    print()
    print("Ingredientes: clave")
    for x,y in zip(ingrediente_name.values(), ingrediente):
        print(x, "  (", y, ")")

    print("\n")
    while opcion != "":
        opcion = input('Indique clave del ingrediente (enter para terminar): ')

        if opcion.lower() in ingrediente:
            monto = monto + ingrediente[opcion]
            lista_ingredientes.append(opcion)
        elif opcion == "":
            resumen(tamano_pizza,monto,lista_ingredientes)
        else:
            print("\t=> Debe seleccionar el tamaño correcto!!") #En caso de que se ingrese un caracter erroneo, se le notificara al usuario


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


    opcion = ""
    monto_total = monto_total + monto_pizza
    if not ingrediente_pizza:
        print("\nUsted seleccionó una pizza ", tamano_name[tamano_pizza], " Margarita")
        print("Subtotal a pagar por una pizza ", tamano_pizza, ": ", monto_pizza)
    else:
        print("Usted seleccionó una pizza ", tamano_name[tamano_pizza], " con ", *[ingrediente_name[x] for x in ingrediente_pizza], sep="-")
        print("Subtotal a pagar por una pizza ", tamano_pizza, ": ", monto_pizza)

    while opcion != "n":
        print("\n***********************")
        opcion = input("¿Desea continuar [s/n]?:")
        print("***********************\n")

        if opcion == "n":
            print("El pedido tiene un total de ", num_pizza, " pizza(s) por un monto de ", monto_total)
            print("\nGracias por su compra, regrese pronto")
            sys.exit()
        elif opcion == "s":
            num_pizza = num_pizza + 1;
            menu_opciones(num_pizza)
        else:
            print("=> Debe seleccionar una opcion valida!!")



menu_opciones(num_pizza)
