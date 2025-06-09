
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        print('Opción no válida, ingrese una de las opciones válidas: ')
        eleccion = input('Ingresa una Opción: ').lower()
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # pueden probar con letras también para verificar su funcionamiento.
    letras = ['a','b','c','d']
    validate(letras, eleccion) 
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
