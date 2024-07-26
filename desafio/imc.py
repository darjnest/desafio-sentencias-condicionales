def calcular_imc(peso,altura):
    """
    Calcular el indice de masa corporal (IMC)

    Parametros: 
    peso (float): Peso de la persona en kilometros
    altura (float): Altura de la persona en metros

    Retorna: 
    float: El valor del IMC
    """

    imc = peso / (altura ** 2)
    return imc


def clasificar_imc(imc):
    """
    Clasifica el IMC según las categorías de la OMS.

    Parámetros:
    imc (float): El valor del IMC calculado.

    Retorna:
    str: La clasificación del IMC según la OMS.
    """

    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"





def main():

    """
    Funcion principal que ejecuta el programa 
    Solicita al usuario que ingrese su peso y altura , calcula el imc y muestra la clasificacion correspondiente.
    """

    peso = float(input("Ingrese su peso en kilogramos: "))

    altura = float(input("Ingrese su altura en metros: "))

    # Calcular el IMC usando la función calcular_imc
    imc = calcular_imc(peso, altura)
    
    # Obtener la clasificación del IMC usando la función clasificar_imc
    clasificacion = clasificar_imc(imc)
    
    # Mostrar el resultado al usuario
    print(f"Su IMC es: {imc:.2f}")
    print(f"Clasificación OMS: {clasificacion}")

# Ejecutar el programa llamando a la función principal
if __name__ == "__main__":
    main()