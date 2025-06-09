def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= int(p_level):
      return 'basicas'
    elif n_pregunta <= 2 * p_level:
      return 'intermedias'
    else:
      return 'avanzadas'  
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias