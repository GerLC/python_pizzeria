from logo import logo_factura
from descuento import promocion
from metodo_pago import metodo_pago

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

    monto_descuento = promocion(num_pizza,monto_total)
    print( "     =>Descuento = ", format(monto_descuento,"0.2f"))

    print("\n     =>Metodo de pago = > ", pago)
    monto_total = monto_total - monto_descuento
    print("\n     =>Total a pagar = > ", monto_total)


