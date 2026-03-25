import sys
import time
import struct
from scapy.all import IP, ICMP, send

def enviar_ping_stealth(mensaje, ip_destino="8.8.8.8"):
    for i, char in enumerate(mensaje, start=1):
        timestamp = struct.pack("<d", time.time())
        padding_base = bytes(range(0x10, 0x37))
        
        payload_data = timestamp + char.encode('utf-8') + padding_base
        payload_data = payload_data[:56] 
        
        paquete = IP(dst=ip_destino)/ICMP(type=8, id=1000, seq=i)/payload_data
        
        send(paquete, verbose=False)
        print(f"Sent packet with seq={i}")
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"texto_a_enviar\"")
        sys.exit(1)

    texto_cifrado = sys.argv[1]
    
    enviar_ping_stealth(texto_cifrado)
    