from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def ajustar_llave(key_input: str, key_len: int) -> bytes:
    key_bytes = key_input.encode()
    if len(key_bytes) < key_len:
        key_bytes += get_random_bytes(key_len - len(key_bytes))
    elif len(key_bytes) > key_len:
        key_bytes = key_bytes[:key_len]
    return key_bytes


def cifrar(algoritmo: str, key: bytes, iv: bytes, texto: str) -> bytes:
    if algoritmo == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError(f"Algoritmo no soportado: {algoritmo}")

    datos = pad(texto.encode(), block_size)
    return cipher.encrypt(datos)


def descifrar(algoritmo: str, key: bytes, iv: bytes, texto_cifrado: bytes) -> str:
    if algoritmo == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError(f"Algoritmo no soportado: {algoritmo}")

    datos = unpad(cipher.decrypt(texto_cifrado), block_size)
    return datos.decode()


def ejecutar_algoritmo(algoritmo):
    print(f"Algoritmo:{algoritmo}")
    texto = input("Texto a cifrar: ")

    if algoritmo == "DES":
        key_len = 8
        iv_len  = 8
    elif algoritmo == "3DES":
        key_len = 24
        iv_len  = 8
    elif algoritmo == "AES":
        key_len = 32
        iv_len  = 16

    key_input = input(f"Llave ({key_len} bytes): ")
    key = ajustar_llave(key_input, key_len)
    print(f"Llave final ({len(key)} bytes): {key}")

    iv_input = input(f"Vector de inicialización ({iv_len} bytes): ").encode()
    if len(iv_input) != iv_len:
        raise ValueError(f"El IV debe tener exactamente {iv_len} bytes.")

    texto_cifrado   = cifrar(algoritmo, key, iv_input, texto)
    print(f"Texto cifrado (bytes): {texto_cifrado}")
    print(f"Texto cifrado (hex):   {texto_cifrado.hex()}")

    texto_descifrado = descifrar(algoritmo, key, iv_input, texto_cifrado)
    print(f"Texto descifrado: {texto_descifrado}")

if __name__ == "__main__":
    print("Seleccione algoritmo:")
    print("1. DES")
    print("2. AES-256")
    print("3. 3DES")

    opcion = input("Opción: ")

    if opcion == "1":
        ejecutar_algoritmo("DES")
    elif opcion == "2":
        ejecutar_algoritmo("AES")
    elif opcion == "3":
        ejecutar_algoritmo("3DES")
    else:
        print("Opción no válida.")


        
