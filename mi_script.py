# Script para mostrar información del sistema operativo y la fecha actual
import platform
import datetime

def main():
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Fecha y hora con Python: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()

