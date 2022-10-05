import random

palabras = []
intentos = 0
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    for linea in f:
        palabras.append(linea)

def limpiar_acentos(text):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text

palabra_random = limpiar_acentos(palabras[random.randint(0, len(palabras))]).upper()


palabra_oculta = ["_" for i in range (0, len(palabra_random) - 1)]

print("¡Adivina la palabra!")
print(palabra_oculta)

def realizar_intento():
    try:
        letra = input("Ingrese una letra: ")
        if letra.isnumeric():
            raise ValueError("Solo puede ingresar números")
        estado = False
        for i in range (0 , len(palabra_random)):
            if letra.upper() == palabra_random[i]:
                palabra_oculta[i] = letra.upper()
                estado = True
                return estado
        return estado
    except ValueError as ve:
        print(ve)


intentos_fallidos = ['''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========''', '''
            +---+
            |   |
            O__ |
           /|\  |
           / \  |
                |
            =========
            
            GAME OVER !!!''']



while intentos < 7:
    a = palabra_oculta
    "".join([str(_) for _ in a])
    if realizar_intento() == True:
        print(palabra_oculta)
        if a == palabra_random:
            print(intentos_fallidos[intentos])
            print("¡¡¡ VICTORIA !!!")
        else:
            continue
    else:
        intentos += 1
        print(intentos_fallidos[intentos])
    print(palabra_oculta)


    