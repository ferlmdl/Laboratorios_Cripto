import sys

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            
            nuevo_char = chr((ord(char) - ascii_offset + desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
        else:
            resultado += char
            
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correcto: python3 cesar.py \"texto a cifrar\" <desplazamiento>")
        sys.exit(1)

    texto_original = sys.argv[1]
    
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")
        sys.exit(1)

    texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
    print(texto_cifrado)





    