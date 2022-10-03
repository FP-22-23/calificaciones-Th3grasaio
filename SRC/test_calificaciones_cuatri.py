from termios import CS6
from calificaciones import*
def main():
    c1 = lee_real("Dame la nota del c1")
    c2 = lee_real("Dame la nota del c2")
    c3 = lee_real("Dame la nota del c3")
    pr1 = lee_real("Dame la nota del proyecto de python")
    ex1 = lee_real("Dame la nota del examen practico de python:")
    cuatrimestre1 = calcula_nota_cuestrimestre((c1, c2, c3), pr1, ex1)
    print("La nota del primer cuatrimestre es: ",cuatrimestre1)
    c4 = lee_real("Dame la nota del c4")
    c5 = lee_real("Dame la nota del c5")
    c6 = lee_real("Dame la nota del c6")
    pr2 = lee_real("Dame la nota del proyecto de python")
    ex2 = lee_real("Dame la nota del examen practico de python:")
    cuatrimestre2 = calcula_nota_cuestrimestre((c4, c5, c6), pr2, ex2)
    print("Tu nota de evaluación continua es: ", calcula_nota_evaluacion_continua)
    






if __name__ == "main":
    main()