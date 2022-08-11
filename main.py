# Defino la varible 'futbolistas' como un diccionario. No es necesario declarar que tipo de dato es

futbolistas = {
    1: "Casillas", 15: "Ramos",
    3: "Pique", 5: "Puyol",
    11: "Capdevila", 14: "Xabi Alonso",
    16: "Busquets", 8: "Xavi Hernandez",
    18: "Pedrito", 6: "Iniesta",
    7: "Villa"
}

verfutbolistas = int(input('Que futbolista quieres ver := '))

if futbolistas.get(verfutbolistas):
    print(futbolistas.get(verfutbolistas))
else:
    print('Ese jugador aun no se encuentra en nuestra lista')
