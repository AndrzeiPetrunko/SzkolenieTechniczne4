from multiprocessing import  Pool, Process


def task(a,b):
    print(a + b)


if __name__ == "__main__":
    for i in range(10):
        process = Process(target=task, args=(i, i + 1))
        process.start()
        print("process started")
    with Pool(processes=20) as pool:
        pool.starmap(task, [(a, b) for a in range(11) for b in range(1,12)])
        print("pool started")

# map(func, iterable)	1 argument	lista wyników	Najczęściej – wiele prostych zadań
# apply(func, args)	1 zadanie	1 wynik	Jednorazowe wywołanie
# starmap(func, list of tuples)	wiele argumentów	lista wyników	Gdy każda funkcja przyjmuje wiele argumentów
