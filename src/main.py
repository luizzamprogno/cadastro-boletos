from database import *
from gui import *
import threading
import time

def agendar_lembretes(intervalo=86400):
    while True:
        verificar_boletos_proximos_vencimento()
        time.sleep(intervalo)

def main():
    criar_banco()
    threading.Thread(target=agendar_lembretes, daemon=True).start()
    init_gui()

if __name__ == '__main__':
    main()
