'''
En este modulo de promocion, calcula el monto dependiendo de la cantidad de pizzas pedidas
A partir del segundo pizza, se le otorgara un descuento del 5%
Entre mas pizza compre, mayor sera el descuento obtenido
Formula utilizada :   MONTO * (NumPizza * DESCUENTO)
Incluye las bebidas
'''

def promocion(n, monto):
    monto_promo = lambda x,descuento: x*descuento
    if n>1:
        print("     =>Solicito un total de ",n," pizzas")
        print("     =>Posee un descuento de: ", format(monto_promo(monto,n*0.05),"0.2f"))
        print("     =>Precio actual: \n")    
        return monto_promo(monto,n*0.05)
    else:
        return 0

