import os
## MI PROYECTO

tamano = {"Grande":580, "Mediana":430, "Personal":280} # Diccionario con tamanos de pizza y precio
ingrediente = {"Jamon": 40, "Champinones": 35, "Pimenton": 30, "Doble_queso": 40, # Diccionario con ingredientes
              "Aceitunas": 57.5, "Pepperoni": 38.5, "Salchichon": 62.5}           # y precio
prefijo_ingrediente = ["ja", "ch", "pi", "dq", "ac", "pe", "sa"]
num_pizza = 1       # Numero de pizzas
monto_total = 0     # monto total

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

    if opcion_tamano.lower() == 'g':
        monto = tamano.get('Grande')
        menu_ingredientes("Grande",monto)
    elif opcion_tamano.lower() == 'm':
        monto = tamano.get(('Mediana'))
        menu_ingredientes('Mediana',monto)
    elif opcion_tamano.lower() == 'p':
        monto = tamano.get(('Personal'))
        menu_ingredientes('Personal',monto)
    else:
        print("=> Debe seleccionar el tamaño correcto!! ('g', 'm' o 'p')")
        menu_opciones()


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
    for x,y in zip(ingrediente, prefijo_ingrediente):
        print(x, "  (", y, ")")

    print("")
    while opcion != "":
        opcion = input('Indique clave del ingrediente (enter para terminar): ')
        if opcion == "ja":
            monto = monto + ingrediente.get("Jamon")
            lista_ingredientes.append("Jamon")
        elif opcion == "ch":
            monto = monto + ingrediente.get("Champinones")
            lista_ingredientes.append("Champinones")
        elif opcion =="pi":
            monto = monto + ingrediente.get("Pimenton")
            lista_ingredientes.append("Pimenton")
        elif opcion =="dq":
            monto = monto + ingrediente.get("Doble_queso")
            lista_ingredientes.append("Doble_queso")
        elif opcion =="ac":
            monto = monto + ingrediente.get("Aceitunas")
            lista_ingredientes.append("Aceitunas")
        elif opcion == "pe":
            monto = monto + ingrediente.get("Pepperoni")
            lista_ingredientes.append("Pepperoni")
        elif opcion == "sa":
            monto = monto + ingrediente.get("Salchichon")
            lista_ingredientes.append("Salchichon")
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
    '''

    # Las variables global, son necesarios para modificar una variable global que hayamos definino anteriormente
    global num_pizza
    global monto_total


    opcion = ""
    monto_total = monto_total + monto_pizza
    if not ingrediente_pizza:
        print("Usted seleccionó una pizza ", tamano_pizza, " Margarita")
        print("Subtotal a pagar por una pizza ", tamano_pizza, ": ", monto_pizza)
    else:
        print("Usted seleccionó una pizza ", tamano_pizza, " con", *ingrediente_pizza,sep="-")
        print("Subtotal a pagar por una pizza ", tamano_pizza, ": ", monto_pizza)

    while opcion != "n":
        print("***********************")
        opcion = input("¿Desea continuar [s/n]?:")
        print("***********************")

        if opcion == "n":
            print("El pedido tiene un total de ", num_pizza, " pizza(s) por un monto de ", monto_total)
        elif opcion == "s":
            num_pizza = num_pizza + 1;
            menu_opciones(num_pizza)



menu_opciones(num_pizza)
