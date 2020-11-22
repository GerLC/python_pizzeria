
from data_option import tipo_pago

def metodo_pago():
    opcion = "1"
    tipo = ""
    print("Seleccione metodo de pago\n")
    for x,y in zip(tipo_pago.values(), tipo_pago):  # En este for, se recorre y se toman las variables para imprimir
        print(x, "  (", y, ")")                              # las opciones de los ingredientes disponibles

    print("\n")
    opcion = input('Indique clave: ')
    if opcion.lower() in tipo_pago:
        tipo = tipo_pago[opcion]
        return tipo
    else:
        print("=> Debe seleccionar la opcion correcta!!")
        metodo_pago()
    return tipo
