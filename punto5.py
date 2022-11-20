def funcion(num1, num2):
    porcentaje = num2 * num1 / 100
    total = num1 - porcentaje
    print('El valor del producto es => '+str(num1)+' El descuento es => '+str(num2)+' El total a pagar es => '+str(total))
   
funcion(100000,20)