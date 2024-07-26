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





def main():

    """
    Funcion principal que ejecuta el programa 
    Solicita al usuario que ingrese su peso y altura , calcula el imc y muestra la clasificacion correspondiente.
    """

    peso = input(float("Ingrese su peso en kilogramos: "))

    altura = input(float("Ingrese su altura en metro: "))