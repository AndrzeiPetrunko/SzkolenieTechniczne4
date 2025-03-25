data_structure = {
    'Osoba': ['imię', 'nazwisko', 'wiek'],
    'Pojazd': ['marka', 'model', 'rocznik']
}

global_namespace = globals()

for class_name, attributes in data_structure.items():
    class_dict = {attr: None for attr in attributes}
    global_namespace[class_name] = type(class_name, (), class_dict)

osoba = Osoba()
osoba.imię = "Jan"
osoba.nazwisko = "Kowalski"
osoba.wiek = 30

pojazd = Pojazd()
pojazd.marka = "Toyota"
pojazd.model = "Corolla"
pojazd.rocznik = 2020

print(f"Osoba: {osoba.imię} {osoba.nazwisko}, Wiek: {osoba.wiek}")
print(f"Pojazd: {pojazd.marka} {pojazd.model}, Rocznik: {pojazd.rocznik}")