# coding=utf-8
def origen():
    """Ésta función retorna el origen de acuerdo a una longitud dada por el usuario"""

    print "Este programa muestra el origen de coordenadas MAGNA-SIRGAS para Colombia a partir de la longitud"
    print "##########################################################"
    print "Ingrese la longitud en grados decimales ej. -75.4546"
    longitud = input()
    if -81.57750792 <= longitud < -78.57750792:
        print "El origen es Oeste Oeste (EPSG = 3114)"
    elif -78.57750792 <= longitud < -75.57750792:
        print "El origen es Oeste (EPSG = 3115)"
    elif -75.57750792 <= longitud < -72.57750792:
        print "El origen es Bogota (EPSG = 3116)"
    elif -72.57750792 <= longitud < -69.57750792:
        print "El origen es Este (EPSG = 3117)"
    elif -69.57750792 <= longitud < -66.57750792:
        print "El origen es Este Este (EPSG = 3118)"
    else:
        print "La longitud ingresada esta fuera de Colombia"

origen()
