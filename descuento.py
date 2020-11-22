'''
En este modulo de promocion, calcula el monto dependiendo de la cantidad de pizzas pedidas
A partir del segundo pizza, se le otorgara un descuento del 5%
Entre mas pizza compre, mayor sera el descuento obtenido
Formula utilizada :   MONTO * (NumPizza * DESCUENTO)
No cuentan las bebidas
'''

def promocion(n, monto):
    monto_promo = lambda x,descuento: x*descuento
    if n>1:
        print("Solicito un total de ",n," pizzas posee un descuento de: ", monto_promo(monto,n*0.05))
        print("Precio actual: ", monto - monto_promo(monto,n*0.05))    
        return monto_promo(monto,n*0.05)
    else:
        return 0

