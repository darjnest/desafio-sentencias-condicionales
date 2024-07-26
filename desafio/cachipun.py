import random
import sys

def main():
    # Lista de opciones válidas
    opciones = ['piedra', 'papel', 'tijera']
    
    # Verificar que el argumento del usuario sea válido
    if len(sys.argv) != 2 or sys.argv[1] not in opciones:
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
        return
    
    # Elección del usuario
    eleccion_usuario = sys.argv[1]
    
    # Elección de la computadora
    eleccion_computadora = random.choice(opciones)
    
    # Mostrar las elecciones
    print(f'Tu jugaste {eleccion_usuario.capitalize()}')
    print(f'Computador jugó {eleccion_computadora.capitalize()}')
    
    # Determinar el resultado
    if eleccion_usuario == eleccion_computadora:
        print('Empate!')
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
        print('Ganaste!!')
    else:
        print('Perdiste!!')

if __name__ == '__main__':
    main()
