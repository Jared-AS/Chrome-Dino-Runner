import threading

from components.menu import menu

if __name__ == "__main__":
    t1 = threading.Thread(target=menu(death_count=0), daemon=True)
    t1.start()
