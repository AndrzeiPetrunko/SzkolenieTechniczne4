import ray

ray.init()

@ray.remote
class KontoBankowe:
    def __init__(self):
        self.kasa = 0

    def wplac(self, pieniadze):
        self.kasa += pieniadze
        return f"Wpłaciłeś {pieniadze} zł."

    def wyplac(self, pieniadze):
        if self.kasa >= pieniadze:
            self.kasa -= pieniadze
            return f"Wypłaciłeś {pieniadze} zł."
        else:
            return "Niewystarczająca ilość środków."

    def saldo(self):
        return f"Na koncie masz {self.kasa} zł."

konto = KontoBankowe.remote()
print(ray.get(konto.wplac.remote(100)))    # "Wpłacono 100"
print(ray.get(konto.wyplac.remote(40)))    # "Wypłacono 40"
print(ray.get(konto.saldo.remote()))



