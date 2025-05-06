from multiprocessing import Process, Lock, Manager
from time import sleep

def przetworz_linie(index, linia, wynik, lock):
    with lock:
        print(f"Proces {index} przetwarza: {linia.strip()}")
        sleep(0.1)
        wynik[index] = linia.upper()

def main():
    with open("dane.txt", "r", encoding="utf-8") as f:
        linie = f.readlines()

    manager = Manager()
    wynik = manager.list([""] * len(linie))
    lock = Lock()
    procesy = []


    for i, linia in enumerate(linie):
        p = Process(target=przetworz_linie, args=(i, linia, wynik, lock))
        procesy.append(p)
        p.start()


    for p in procesy:
        p.join()


    with open("wynik_lock.txt", "w", encoding="utf-8") as f:
        f.writelines(wynik)

    print("Przetwarzanie zakończone – wynik zapisany w 'wynik_lock.txt'.")

if __name__ == "__main__":
    main()
