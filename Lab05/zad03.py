import time

def srednia_dec(func):
    def wypisz(*args):
        print("Obliczamy średnią liczb:", *args)
        func(*args)  # Call the original function here
        print("ez tutorial")
    return wypisz

def time_passed_dec(func):
    def zmierzanie(*args):
        start = time.time()
        func(*args)
        print("zmierzanie ok %s" % (time.time() - start))
    return zmierzanie

@time_passed_dec
@srednia_dec
def srednia(*args):
    time.sleep(2)  # Introduce a 2-second delay to simulate a longer execution
    avg = sum(args) / len(args)  # Correct average calculation
    print(avg)

srednia(4, 5)
