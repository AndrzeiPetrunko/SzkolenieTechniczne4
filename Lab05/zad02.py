def srednia_dec(func):
    def wypisz(*args):
        print("Obliczamy średnią liczb:", *args)
        func(*args)  # Call the original function here
        print("ez tutorial")
    return wypisz


@srednia_dec
def srednia(*args):
    avg = sum(args) / len(args)
    print(avg)

srednia(4, 5)