import os
import subprocess

def scan_devices():
    """
    Escanea los dispositivos conectados a la red WiFi usando 'arp-scan'.
    """
    print("Escaneando dispositivos conectados a la red...")
    try:
        # Ejecuta el comando 'arp-scan' para listar dispositivos conectados
        result = subprocess.check_output(["arp-scan", "--localnet"], universal_newlines=True)
        print(result)
    except FileNotFoundError:
        print("Error: 'arp-scan' no está instalado. Instálalo con 'sudo apt install arp-scan'.")
    except Exception as e:
        print(f"Error al escanear dispositivos: {e}")

def block_device(mac_address):
    """
    Bloquea un dispositivo usando su dirección MAC.
    """
    try:
        # Agrega la dirección MAC a la lista de acceso denegado del router.
        print(f"Bloqueando el dispositivo con MAC: {mac_address}")
        os.system(f"iptables -A INPUT -m mac --mac-source {mac_address} -j DROP")
        print("Dispositivo bloqueado.")
    except Exception as e:
        print(f"Error al bloquear el dispositivo: {e}")

def main():
    while True:
        print("\nOpciones:")
        print("1. Escanear dispositivos conectados")
        print("2. Bloquear un dispositivo por MAC")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            scan_devices()
        elif choice == "2":
            mac_address = input("Introduce la dirección MAC del dispositivo: ")
            block_device(mac_address)
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
