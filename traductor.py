def cargar_diccionario():
    try:
        with open('EN-ES.txt', 'r', encoding='utf-8') as archivo:
            return dict(linea.strip().split('=') for linea in archivo if '=' in linea)
    except FileNotFoundError:
        print("El archivo EN-ES.txt no existe. Se creará uno nuevo.")
        return {}

def agregar_traduccion(palabra_en, palabra_es):
    with open('EN-ES.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f'\n{palabra_en}={palabra_es}')

def traducir(codigo, palabra):
    diccionario = cargar_diccionario()
    if codigo == "EN-ES":
        return f"{codigo} {palabra} --> {diccionario.get(palabra, 'No se encontró una traducción')}"
    elif codigo == "ES-EN":
        traduccion = None
        for key, value in diccionario.items():
            if value == palabra:
                traduccion = key
                break
        if traduccion:
            return f"{codigo} {palabra} --> {traduccion}"
        else:
            return f"No se encontró una traducción para '{palabra}'"
    else:
        return "Código de idioma no válido. Utilice EN-ES o ES-EN."


while True:
    print("\nMenu:")
    print("1. Agregar nueva traducción")
    print("2. Traducir")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        palabra_en = input("Ingrese la palabra en inglés: ")
        palabra_es = input("Ingrese la traducción al español: ")
        agregar_traduccion(palabra_en, palabra_es)
        print(f"Se agregó la traducción: {palabra_en}={palabra_es}")
    elif opcion == "2":
        codigo, palabra = input("Ingrese el código y la palabra (por ejemplo: EN-ES dog): ").split()
        resultado = traducir(codigo.upper(), palabra.lower())
        print(resultado)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
