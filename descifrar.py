import sys

VERDE = '\033[92m'
RESET = '\033[0m'

PALABRAS_ESPANOL = ["y", "en", "de", "la", "el", "que", "los", "las", "un", "una", 
                    "redes", "seguridad", "criptografia", "informacion", "datos"]

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            if char.islower():
                resultado += chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a'))
            else:
                resultado += chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado

def evaluar_probabilidad(texto):
    palabras = texto.lower().split()
    coincidencias = sum(1 for palabra in palabras if palabra in PALABRAS_ESPANOL)
    return coincidencias

def main():
    if len(sys.argv) < 2:
        print("Uso correcto: python descifrar.py \"texto cifrado\"")
        return

    texto_cifrado = sys.argv[1]
    mejor_desplazamiento = 0
    max_coincidencias = -1
    
    for desp in range(1, 27):
        texto_prueba = descifrar_cesar(texto_cifrado, desp)
        coincidencias = evaluar_probabilidad(texto_prueba)
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_desplazamiento = desp

    print("\n--- INICIANDO ATAQUE DE FUERZA BRUTA ---\n")
    for desp in range(1, 27):
        texto_descifrado = descifrar_cesar(texto_cifrado, desp)
        
        if desp == mejor_desplazamiento:
            print(f"{VERDE}Desplazamiento {desp:2d}: {texto_descifrado}{RESET}")
        else:
            print(f"Desplazamiento {desp:2d}: {texto_descifrado}")

if __name__ == "__main__":
    main()