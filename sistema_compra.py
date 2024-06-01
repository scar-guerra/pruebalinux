
print('1. Agua → $ 600')
print('2. Azúcar→ $1200')
print('3. Aceite → $1500')
print('4. Arroz → $1250')
print('5. Fideos → $ 790')
print('6. Bebida→ $1780')
print('7. Chocolate → $2500')
print('8. Pan molde → $1340')

total = 0
rep = 1
while rep == 1 :

    p = int(input('¿Que producto desea comprar? Ingrese un número: '))

    if p >= 1 and p <= 8: 

   

     if p == 1:
            valor_p = 600
            producto = 'Agua'
            validar_producto = input((f'¿Está seguro de comprar {producto} por {valor_p}? si/no'))
            if validar_producto == 'si':
             cantidad = int(input('Ingrese la cantidad: '))
             subtotal = cantidad * valor_p
             total = total + subtotal
            else:
             print('Se ha eliminado del carrito')
             

     elif p == 2:
          valor_p = 1200
          producto = 'Azucar'
          validar_producto = ((f'¿Está seguro de comprar {producto} por {valor_p}? si/no'))

     elif p == 3:
          valor_p = 1500
          producto = 'Aceite'

     elif p == 4:
          valor_p = 1250
          producto = 'Arroz'

     elif p == 5:
          valor_p = 790
          producto = 'Fideos'

     elif p == 6:
          valor_p = 1780
          producto = 'Bebida'

     elif p == 7:
          valor_p = 2500
          producto = 'Chocolate'

     elif p == 8:
          valor_p = 1340
          producto = 'Pan molde'



     
    
   
     nueva_compra = input('¿desea comprar otro producto? si/no')
     if nueva_compra == 'si':
      rep = 1
     else:
        rep = 0

    else:
        print('ingrese un numero valido')
          
    
print((f'El TOTAL de compra es: {total}'))

cliente_preferente = input('¿Es cliente preferente?: si/no')

if cliente_preferente == 'si':
    print('Usted es cliente Preferente, se aplicará un dcto de 25% del total de la compra')

    total = total - (total * 0.25)
    print((f'El total a pagar es: ${total}'))
    pagar = int(input('Con cuanto dinero paga?: '))
    if pagar >= total:
        vuelto = pagar - total
        print((f'Su vuelto es: ${vuelto}'))
    else:
        print('Dinero insuficiente!')

else:
    total = total
    print((f'El total a pagar es: ${total}'))
    pagar = int(input('Con cuanto dinero paga?: '))
    if pagar >= total:
        vuelto = pagar - total
        print((f'Su vuelto es: ${vuelto}'))
    else:
        print('Dinero insuficiente!')
    






