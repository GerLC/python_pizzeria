from functions.logo import logo_factura
from functions.descuento import promocion
from functions.metodo_pago import metodo_pago

'''
En este modulo de factura, recibe los pedidos, monto_total, las bebidas y el monto de estas aparte, 
y el numero de pizza, para generar una simple factura con los datos.

Obtenido los datos
Genera la factura indicando los pedidos:
Pizza, tamano, ingredientes, el monto. 
Indican las bebidas y el monto de estas en caso de solicitarlas. 
Y por último el monto total de todos los productos.

'''
def factura(pedido, monto_total, bebida, monto_bebida, num_pizza):

    pago = metodo_pago()
    logo_factura()
    for x in pedido:
        print("     =>", *x, sep="   ")
        print("Bs")
    
    print( "     => Bebidas")
    for y in bebida:
        print("     =>", y, sep="   ")
    print("\n     =>Monto Bebidas = ", monto_bebida)
    print( "     =>Subtotal = ", format(monto_total,"0.2f"))

    print("\n")
    monto_descuento = promocion(num_pizza,monto_total)
    print( "     =>Descuento = ", format(monto_descuento,"0.2f"))

    print("\n     =>Metodo de pago = > ", pago)
    monto_total = monto_total - monto_descuento
    print("\n     =>Total a pagar = > ", monto_total, " Bs")


